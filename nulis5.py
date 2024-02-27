import csv
import itertools
import keyword as acak
import logging
import os
import random
import subprocess
import time
from datetime import datetime

import openai
import pandas as pd
import requests
import telebot
from googlesearch import search

from autopdf import generate_html

# Ganti dengan token bot Telegram Anda
last_update_time = None
keywords_list = []
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
api_key = ''
openai.api_key = api_key

def send_formatted_message(chat_id, formatted_message):
    bot.send_message(chat_id=chat_id, text=formatted_message)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": message.Chat.id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Telegram bot: {response.text}")
        
def scan_subdomain(domain):
    subdomains = []
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)
        except requests.RequestException:
            pass
    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")
    return domain_results

def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        return None
    return domain

def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []
        
        # Menyimpan hasil pencarian dalam list
        search_results = list(itertools.islice(search(keyword), num_results))
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        for url in search_results:
            print(f"Found URL: {url}")
            domain = extract_domain(url)
            result = None
            if domain:
                result = {
                    'keyword': keyword,
                    'URL': url,
                    'Domain': domain,
                }
            if result:
                results.append(result)

            time.sleep(10)  # Penundaan 10 detik
            
        return results
    except Exception as e:
        print(f"Error in scrape_domain: {str(e)}")
        return []  # Return an empty list to handle the error


def get_dns_info(hostname):
    try:
        # Scanning CNAME
        cname_result = subprocess.check_output(['nslookup', '-type=CNAME', hostname], universal_newlines=True)
        cname_values = [line.split(':')[-1].strip() for line in cname_result.splitlines() if 'canonical name' in line.lower()]
    except subprocess.CalledProcessError:
        cname_values = None

    try:
        # Scanning IPv4
        ipv4_result = subprocess.check_output(['nslookup', '-type=A', hostname], universal_newlines=True)
        ipv4_addresses = [line.split(':')[-1].strip() for line in ipv4_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv4_addresses = None

    try:
        # Scanning IPv6
        ipv6_result = subprocess.check_output(['nslookup', '-type=AAAA', hostname], universal_newlines=True)
        ipv6_addresses = [line.split(':')[-1].strip() for line in ipv6_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv6_addresses = None

    return cname_values, ipv4_addresses, ipv6_addresses


def create_prompt_from_file(input_file, output_file, message):
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Menggunakan OpenAI untuk mendapatkan respons
    openai_response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=150
    )

    # Memeriksa apakah openai_response.choices tidak kosong
    if openai_response.choices:
        # Menyimpan output dari OpenAI ke file
        with open(output_file, 'w') as file:
            file.write(openai_response.choices[0].text)

        # Mengirimkan output file ke pengguna
        with open(output_file, 'r') as file:
            output_text = file.read()

        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id, "Tidak ada respons dari OpenAI.")

# Fungsi untuk mengupdate skrip
def update_scripts(message):
    try:
        subprocess.run(['bash', 'run.sh'], check=True)
        bot.reply_to(message, "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

# Fungsi untuk mengupdate keyword
def update_keywords():
    global keywords_list

    try:
        with open('keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
        return True
    except Exception as e:
        print(f"Error updating keywords: {e}")
        return False
        
# Fungsi untuk membuat prompt
def create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword):
    # Membaca file skrip.txt untuk mendapatkan prompt
    with open("skrip.txt", "r") as skrip_file:
        skrip_options = skrip_file.readlines()
        prompt = random.choice(skrip_options).strip()
    
    # Membaca file keyword1_file dan keyword2_file untuk mendapatkan keyword
    with open(keyword1_file, "r") as keyword1_file, open(keyword2_file, "r") as keyword2_file:
        keyword1_options = keyword1_file.readlines()
        keyword2_options = keyword2_file.readlines()
        
        # Memilih keyword secara acak dari file keyword1_file dan keyword2_file
        keyword1 = random.choice(keyword1_options).strip()
        keyword2 = random.choice(keyword2_options).strip()
    
    # Menambahkan jumlah_keyword ke dalam prompt
    prompt += " " + jumlah_keyword
    
    # Menambahkan command_option ke dalam prompt jika prompt_type adalah 'C'
    if prompt_type == 'C':
        prompt += " " + command_option
    
    # Menambahkan specification_option ke dalam prompt jika prompt_type adalah 'S'
    if prompt_type == 'S':
        prompt += " " + specification_option
    
    # Menambahkan keyword1 dan keyword2 ke dalam prompt
    prompt += " " + keyword1 + " " + keyword2
    
    # Menyimpan prompt ke dalam output_file
    with open(output_file, "w") as output_file:
        output_file.write(prompt)
    
    return prompt

# Fungsi untuk menghasilkan file keyword
def generate_keyword_file(filename, num_keywords):
    keyword_list = []
    with open("keyword.txt", "r") as keyword_file:
        keyword_list = keyword_file.readlines()
    
    keyword_list = [keyword.strip() for keyword in keyword_list]
    
    # Memilih beberapa keyword secara acak dari keyword_list
    selected_keywords = random.sample(keyword_list, num_keywords)
    
    with open(filename, "w") as file:
        file.write("\n".join(selected_keywords))
        

# Fungsi untuk menangani command /ai_prompt
def handle_prompt(message):
    args = message.text.split("/")[1:]
    
    if len(args) == 7:
        keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword = args
        
        # Membuat file keyword
        generate_keyword_file(keyword1_file, 500)
        generate_keyword_file(keyword2_file, 500)
        
        # Membuat prompt
        prompt = create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword)
        
        bot.send_message(message.chat.id, prompt)
    else:
        bot.send_message(message.chat.id, "Format prompt tidak valid.")        
    

Berikut ini adalah skrip yang telah diperbarui sesuai dengan permintaan Anda:

```python
import csv
import itertools
import logging
import os
import random
import subprocess
import time
from datetime import datetime

import openai
import pandas as pd
import requests
import telebot
from googlesearch import search

from autopdf import generate_html

# Ganti dengan token bot Telegram Anda
last_update_time = None
keywords_list = []
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
api_key = ''
openai.api_key = api_key

def send_formatted_message(chat_id, formatted_message):
    bot.send_message(chat_id=chat_id, text=formatted_message)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": message.Chat.id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Telegram bot: {response.text}")
        
def scan_subdomain(domain):
    subdomains = []
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code in [200, 301, 400, 409, 502, 401]:
                server_info = response.headers.get('Server', 'N/A')
                print(f"Subdomain found: {url} | Status Code: {response.status_code} | Server: {server_info}\n")
                domain_results.append(url)
        except requests.RequestException:
            pass
    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")
    return domain_results

def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        return None
    return domain

def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []
        
        # Menyimpan hasil pencarian dalam list
        search_results = list(itertools.islice(search(keyword), num_results))
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        for url in search_results:
            print(f"Found URL: {url}")
            domain = extract_domain(url)
            result = None
            if domain:
                result = {
                    'keyword': keyword,
                    'URL': url,
                    'Domain': domain,
                }
            if result:
                results.append(result)

            time.sleep(10)  # Penundaan 10 detik
            
        return results
    except Exception as e:
        print(f"Error in scrape_domain: {str(e)}")
        return []  # Return an empty list to handle the error



def get_dns_info(hostname):
    try:
        # Scanning CNAME
        cname_result = subprocess.check_output(['nslookup', '-type=CNAME', hostname], universal_newlines=True)
        cname_values = [line.split(':')[-1].strip() for line in cname_result.splitlines() if 'canonical name' in line.lower()]
    except subprocess.CalledProcessError:
        cname_values = None

    try:
        # Scanning IPv4
        ipv4_result = subprocess.check_output(['nslookup', '-type=A', hostname], universal_newlines=True)
        ipv4_addresses = [line.split(':')[-1].strip() for line in ipv4_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv4_addresses = None

    try:
        # Scanning IPv6
        ipv6_result = subprocess.check_output(['nslookup', '-type=AAAA', hostname], universal_newlines=True)
        ipv6_addresses = [line.split(':')[-1].strip() for line in ipv6_result.splitlines() if 'address' in line.lower()]
    except subprocess.CalledProcessError:
        ipv6_addresses = None

    return cname_values, ipv4_addresses, ipv6_addresses


def create_prompt_from_file(input_file, output_file, message):
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Menggunakan OpenAI untuk mendapatkan respons
    openai_response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=150
    )

    # Memeriksa apakah openai_response.choices tidak kosong
    if openai_response.choices:
        # Menyimpan output dari OpenAI ke file
        with open(output_file, 'w') as file:
            file.write(openai_response.choices[0].text)

        # Mengirimkan output file ke pengguna
        with open(output_file, 'r') as file:
            output_text = file.read()

        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id, "Tidak ada respons dari OpenAI.")

# Fungsi untuk mengupdate skrip
def update_scripts(message):
    try:
        subprocess.run(['bash', 'run.sh'], check=True)
        bot.reply_to(message, "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

# Fungsi untuk mengupdate keyword
def update_keywords():
    global keywords_list

    try:
        with open('keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
        return True
    except Exception as e:
        print(f"Error updating keywords: {e}")
        return False
        
# Fungsi untuk membuat prompt
def create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword):
    # Membaca file skrip.txt untuk mendapatkan prompt
    with open("skrip.txt", "r") as skrip_file:
        skrip_options = skrip_file.readlines()
        prompt = random.choice(skrip_options).strip()
    
    # Membaca file keyword1_file dan keyword2_file untuk mendapatkan keyword
    with open(keyword1_file, "r") as keyword1_file, open(keyword2_file, "r") as keyword2_file:
        keyword1_options = keyword1_file.readlines()
        keyword2_options = keyword2_file.readlines()
        
        # Memilih keyword secara acak dari file keyword1_file dan keyword2_file
        keyword1 = random.choice(keyword1_options).strip()
        keyword2 = random.choice(keyword2_options).strip()
    
    # Menambahkan jumlah_keyword ke dalam prompt
    prompt += " " + jumlah_keyword
    
    # Menambahkan command_option ke dalam prompt jika prompt_type adalah 'C'
    if prompt_type == 'C':
        prompt += " " + command_option
    
    # Menambahkan specification_option ke dalam prompt jika prompt_type adalah 'S'
    if prompt_type == 'S':
        prompt += " " + specification_option
    
    # Menambahkan keyword1 dan keyword2 ke dalam prompt
    prompt += " " + keyword1 + " " + keyword2
    
    # Menyimpan prompt ke dalam output_file
    with open(output_file, "w") as output_file:
        output_file.write(prompt)
    
    return prompt

# Fungsi untuk menghasilkan file keyword
def generate_keyword_file(filename, num_keywords):
    keyword_list = []
    with open("keyword.txt", "r") as keyword_file:
        keyword_list = keyword_file.readlines()
    
    keyword_list = [keyword.strip() for keyword in keyword_list]
    
    # Memilih beberapa keyword secara acak dari keyword_list
    selected_keywords = random.sample(keyword_list, num_keywords)
    
    with open(filename, "w") as file:
        file.write("\n".join(selected_keywords))
        

# Fungsi untuk menangani command /ai_prompt
def handle_prompt(message):
    args = message.text.split("/")[1:]
    
    if len(args) == 7:
        keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword = args
        
        # Membuat file keyword
        generate_keyword_file(keyword1_file, 500)
        generate_keyword_file(keyword2_file, 500)
        
        # Membuat prompt
        prompt = create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, jumlah_keyword)
        
        bot.send_message(message.chat.id, prompt)
    else:
        bot.send_message(message.chat.id, "Format prompt tidak valid.")        
    

@bot.message_handler(commands=['chat'])
def write_document(message):
    inputs = message.text[len('/chat '):].split(';')
    if len(inputs) != 3:
        bot.reply_to(message, "Format salah, silakan ikuti format ini: /chat pesan1;pesan2;pesan3")
        return

    judul = inputs[0].strip()
    subjudul_list = inputs[1].strip().split(',')
    keywords_list = inputs[2].strip().split(',')  # Perhatikan perubahan di sini

    # membuat prompt 
    prompt = f"Judul: {judul}\n\n"

    for idx, sub_judul in enumerate(subjudul_list, start=1):
        prompt += f"Sub_{idx}: {sub_judul}\n"
    prompt += "Keywords: " + ', '.join(keywords_list) + "\n\n"
    
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,  # Perhatikan perubahan di sini
        max_tokens=10
    )

    bot.reply_to(message, response.choices[0].text.strip())
    
def create_prompt_from_file(input_file, output_file, message):
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Menggunakan OpenAI untuk mendapatkan respons
    openai_response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=150
    )

    # Memeriksa apakah openai_response.choices tidak kosong
    if openai_response.choices:
        # Menyimpan output dari OpenAI ke file
        with open(output_file, 'w') as file:
            file.write(openai_response.choices[0].text)

        # Mengirimkan output file ke pengguna
        with open(output_file, 'r') as file:
            output_text = file.read()

        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id, "Tidak ada respons dari OpenAI.")

@bot.message_handler(commands=['ai'])
def handle_prompt_from_file(message):
    args = message.text.split('/')[1:]

    if len(args) == 2:
        input_file, output_file = args

        # Membuat prompt dari file dan mengirimkan outputnya ke pengguna
        create_prompt_from_file(input_file, output_file, message)
        bot.send_message(message.chat.id, f"hasil sudah ada di {output_file} silahkan /download2")
    else:
        bot.send_message(message.chat.id, "Format prompt dari file tidak valid. Gunakan format /ai ai.txt/output.txt")

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))


@bot.message_handler(commands=['ai_prompt'])
def handle_prompt(message):
    args = message.text.split('/')[1:]

    if len(args) == 7:
        keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, additional_input = args

        # Generate keyword files
        generate_keyword_file(keyword1_file, 500)
        generate_keyword_file(keyword2_file, 500)

        # Create prompt
        create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, additional_input, message)

        # Send the output file to the user
        with open(output_file, 'r') as file:
            output_text = file.read()

        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id, "Format prompt tidak valid. Gunakan format /ai_prompt fitur.txt/objek.txt/ai.txt/kata_perintah/specification_option/prompt_type/jumlah")


# Mengupdate skrip saat command /update dijalankan
@bot.message_handler(commands=['update'])
def handle_update_scripts(message):
    update_scripts(message)

# Mengupdate keyword saat command /keyword dijalankan
@bot.message_handler(commands=['keyword'])
def handle_update_keywords(message):
    update_keywords()
    bot.reply_to(message, "Database keyword berhasil diperbarui.")
        
@bot.message_handler(commands=['dnsinfo'])
def handle_dnsinfo(message):
    domain = message.text.split()[1]
    cname_values, ipv4_addresses, ipv6_addresses = get_dns_info(domain)
    bot.send_message(message.chat.id, f"CNAME: {cname_values}\nIPv4: {ipv4_addresses}\nIPv6: {ipv6_addresses}")
    time.sleep(10)  # Add a delay of 10 seconds

@bot.message_handler(commands=['dork'])
def handle_dork(message):
    try:
        # Memisahkan argumen menggunakan "/" sebagai pemisah
        _, keywords_line, domain_extensions_line = message.text.split('/')

        # Mendapatkan daftar kata kunci dan ekstensi domain
        keywords = keywords_line.split(',')
        domain_extensions = domain_extensions_line.split(',')

        # Menyimpan hasil pencarian dari setiap kombinasi kata kunci dan ekstensi domain
        all_results = []

        for keyword in keywords:
            for domain_extension in domain_extensions:
                keyword_with_extension = f"{keyword}{domain_extension}"
                results = scrape_domain(keyword_with_extension)
                all_results.extend(results)

        if all_results:
            # Mengirim hasil pencarian ke pengguna
            bot.send_message(message.chat.id, f"Results: {str(all_results)}")
        else:
            # Memberikan pesan jika tidak ada hasil yang ditemukan
            bot.reply_to(message, "No results found.")
    
    except ValueError:
        # Menangani kesalahan jika format perintah tidak sesuai
        bot.reply_to(message, "Invalid format. Use /dork <keywords>;<domain_extensions>")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, welcome to my Bot! Please format your message as follows: /chat for chat me and /write or /ai then /update or /keyword\n /dork for seraching and /scan for scanning subdomains")


@bot.message_handler(commands=['scan'])
def handle_subdomain_query(message):
    domain = message.text.split()[-1]  # assuming the domain is the last text after the command
    results = scan_subdomain(domain)
    bot.reply_to(ext=f"Subdomain scan results: {results}")

def check_cover_png():
    file_path = 'cover.png'
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        return True
    return False

@bot.message_handler(commands=['write'])
def get_random_text(message):
    global last_update_time, keywords_list

    # Periksa apakah file keyword.csv perlu diperbarui
    current_time = datetime.now()
    if last_update_time is None or (current_time - last_update_time).days >= 1:
        if update_keywords():
            last_update_time = current_time
        else:
            bot.reply_to(message, f"Maaf admin lupa mengupdate database untuk penulisan. \n Silahkan upload keyword.txt berupa bahan tulisan \n dan Coba lagi nanti.")
            return

    # Example data
    data = {
        'Logo': ['Logo Value'],
        'Bab': ['Bab Value'],
        'Subjudul 1': ['Subjudul 1 Value'],
        'Opsional 1': ['Opsional 1 Value'],
        'Opsional 2': ['Opsional 2 Value'],
        'Opsional 3': ['Opsional 3 Value'],
        'Opsional 4': ['Opsional 4 Value'],
        'Opsional 5': ['Opsional 5 Value'],
        'Opsional 6': ['Opsional 6 Value'],
        'Opsional 7': ['Opsional 7 Value'],
        'Opsional 8': ['Opsional 8 Value'],
        'Opsional 9': ['Opsional 9 Value'],
        'Opsional 10': ['Opsional 10 Value'],
        'Opsional 11': ['Opsional 11 Value'],
        'Opsional 12': ['Opsional 12 Value'],
        'Opsional 13': ['Opsional 13 Value'],
        'Opsional 14': ['Opsional 14 Value'],
        'Opsional 15': ['Opsional 15 Value'],
        'Opsional 16': ['Opsional 16 Value'],
        'Opsional 17': ['Opsional 17 Value'],
        'Opsional 18': ['Opsional 18 Value'],
        'Opsional 19': ['Opsional 19 Value'],
        'Opsional 20': ['Opsional 20 Value'],
        'Opsional 21': ['Opsional 21 Value'],
        # Add more columns as needed
    }

    # Create a DataFrame
    your_dataframe = pd.DataFrame(data)

    # Ganti fungsi pencarian Google dengan generate_html
    # Assuming your_dataframe contains the data you need
    generated_keyword = generate_html(your_dataframe)

    # Process the generated_keyword as needed

    bot.reply_to(message, f"Intruksi!!: {generated_keyword} \n list file bahan: \n 1. keyword.csv \n 2. keyword.txt \n 3. cover.xlsx \n 4. auto.xlsx \n 5. skrip.txt \n DAPATKAN DI https://github.com/miftah06/izmiftah/ \n")

@bot.message_handler(commands=['download3'])
def download_html(message):
    try:
        with open('ai.txt', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading txt output file: {e}")
        bot.reply_to(message, "Gagal mengunduh file txt. Coba lagi nanti.")


@bot.message_handler(commands=['download-cover'])
def download_keywords(message):
    global keywords_list

    try:
        with open('beauty-cover.pdf', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, "Gagal mengunduh file pdf. Coba lagi nanti.")

@bot.message_handler(commands=['download-final'])
def download_keywords(message):
    try:
        with open('final_output.pdf', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, "Gagal mengunduh file pdf. Coba lagi nanti.")

@bot.message_handler(commands=['download-hasil'])
def download_keywords(message):
    try:
        with open('hasil.txt', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, "Gagal mengunduh file txt. Coba lagi nanti.")

@bot.message_handler(commands=['download'])
def download_keywords(message):
    try:
        with open('output_novel.pdf', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading keywords: {e}")
        bot.reply_to(message, "Gagal mengunduh file pdf. Coba lagi nanti.")

@bot.message_handler(commands=['download_html'])
def download_html(message):
    try:
        with open('output.html', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, "Gagal mengunduh file HTML. Coba lagi nanti.")

@bot.message_handler(commands=['download2'])
def download_html(message):
    try:
        with open('output.txt', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading txt output file: {e}")
        bot.reply_to(message, "Gagal mengunduh file txt. Coba lagi nanti.")

@bot.message_handler(commands=['download_html1'])
def download_html(message):
    try:
        with open('cover.html', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, "Gagal mengunduh file HTML. Coba lagi nanti.")

@bot.message_handler(commands=['download_html2'])
def download_html(message):
    try:
        with open('pdf.html', 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading HTML: {e}")
        bot.reply_to(message, "Gagal mengunduh file HTML. Coba lagi nanti.")

@bot.message_handler(commands=['upload'])
def update_keywords(message):
    global keywords_list

    try:
        # Set a larger field size limit
        max_field_size = int(1e6)
        csv.field_size_limit(max_field_size)

        # Read the entire CSV file with Pandas
        df = pd.read_csv('keyword.txt', header=None)

        # Convert the first column to lowercase and extend the keywords list
        keywords_list.extend(df.iloc[:, 0].str.lower().tolist())

        return True
    except Exception as e:
        print(f"Error updating keywords: {e}")
        return False

    if check_cover_png():
        bot.reply_to(message, "cover.png kosong. Silahkan upload cover.png sebagai logo atau cover karya tulis atau novel Anda.")
    else:
        bot.reply_to(message, "Terima kasih! File cover.png sudah diunggah.")

def process_uploaded_file(file_path):
    # Implement your logic to process the uploaded file
    # For example, you can read the contents of the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Process the content as needed
            print(f"Content of the uploaded file:\n{content}")
            return True
    except Exception as e:
        print(f"Error processing uploaded file: {e}")
        return False

@bot.message_handler(content_types=['document'])
def handle_uploaded_file(message):
    global keywords_list

    if message.document.file_name not in ['keyword.csv', 'keyword.txt', 'skrip.txt', 'auto.xlsx', 'input.txt', 'subdomains.txt', 'cover.png']:
        bot.reply_to(message, "Mohon kirim file dengan nama 'keyword.csv', 'keyword.txt', 'skrip.txt', 'auto.xlsx', 'input.txt', 'cover.png', 'subdomains.txt'. ")
        return

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    if update_keywords():
        bot.reply_to(message, f"File {message.document.file_name} berhasil diunggah dan database diperbarui.")
    else:
        bot.reply_to(message, "Gagal memperbarui database. Coba lagi nanti.")

@bot.message_handler(commands=['update'])
def update_scripts(message):
    try:
        subprocess.run(['bash', 'run.sh'], check=True)
        bot.reply_to(message, "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['keyword'])
def update_scripts(message):
    try:
        subprocess.run(['bash', 'key.sh'], check=True)
        bot.reply_to(message, "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

def update_keywords():
    global keywords_list

    try:
        with open('keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
        return True
    except Exception as e:
        print(f"Error updating keywords: {e}")
        return False

# Logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # File auto.xlsx tidak ada, download atau generate
    try:
        subprocess.run(['wget', "https://example.com/auto.xlsx"], check=True)
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, "Gagal mengunduh file auto.xlsx. Coba lagi nanti.")
        
# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # File auto.xlsx tidak ada, download atau generate
    try:
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/bab-generator/input_data.xlsx'])
        subprocess.run(['wget', 'https://github.com/miftah06/skripsi/raw/master/cover-generator/cover.xlsx'])
        subprocess.run(['mv', 'input_data.xlsx', 'auto.xlsx'])
        print("File auto.xlsx berhasil di-download dan diubah namanya.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Gagal mendownload atau mengubah nama file auto.xlsx.")
        # Tambahkan logika untuk menghasilkan file auto.xlsx

def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html><body><h1> ganti bagian sini... untuk mengedit file htmlnya </h1></body></html>"
    return generated_html

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            time.sleep(10)