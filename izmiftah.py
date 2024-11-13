import asyncio
import csv
import datetime
import json
import keyword as acak
import logging
import os
from urllib.parse import urlparse
from telebot import types
import random
import sqlite3
import subprocess
import threading
import time
import openai
import requests
import telebot
from telebot import TeleBot
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from telebot import types
from PIL import Image, ImageOps
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm
import re
from dotenv import load_dotenv
from nulis1 import generate_keywords_pdf_pdfkit, generate_keywords_pdf_fpdf, generate_keywords_pdf_reportlab
from deep_translator import GoogleTranslator

load_dotenv('/root/izmiftah/.env')
TOKEN = os.getenv('token')
passnya = os.getenv('password')
# Load environment variables from .env
api_key = os.getenv('openai')
# Ganti dengan token bot Telegram Anda
API_KEY = 'api-key-search-engine-kamu'
keywords_list = []
bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
email_kamu = os.getenv('email') #tolong modifikasi se>
openai.api_key = api_key
admin = os.getenv('idtelegram')
link_jualan = os.getenv('link')
google_apikey = 'AIzaSyCfEbq1hzg3wjnUhq_3-skMnRlWb5MVeX4'
openai.api_key = api_key
api_key_path = 'api.json'
# dapatkan di https://t.me/username_to_id_bot
### JANGAN DI UBAH #####
# ini penentu jumlah jumlah_koinny
# tolong sesuaikan
# Menggunakan nilai jumlah_jumlah_koin untuk menginisialisasi jumlah_credit
# Mengubah nilai jumlah_credit menjadi -1 (jika itu yang Anda inginkan)
### JANGAN DI UBAH #####
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
global jumlah_credit
jumlah_koin_awal = 0  # ini penentu jumlah jumlah_koinnya secara terbalik
jumlah_koin = 15 --15
jumlah_kredit = 0 # ini
# ini penentu jumlah jumlah_koinny
# Inisialisasi variabel-variabel
credit = jumlah_koin_awal
isi_jumlah_koin = +jumlah_koin_awal # tolong sesuaikan
# Menggunakan nilai jumlah_jumlah_koin untuk menginisialisasi jumlah_credit
# Mengubah nilai jumlah_credit menjadi -1 (jika itu yang Anda inginkan)
credit_jumlah_koin = 1  # Ini penentu jumlah jumlah_koinnya
jumlah_koinnya = 10 + jumlah_koin
isi_saldo = jumlah_koinnya
jumlah_jumlah_koin = 15 + +jumlah_koin_awal
saldo_nol = 15
saldonya = saldo_nol
credit_saldo = jumlah_koin_awal
saldo = 100
new_saldo = jumlah_koin_awal
# Inisialisasi identitas
identitas = "mif , seorang peneliti yang penuh dengan rasa penasaran"
midtrans_url = 'https://api.sandbox.midtrans.com/v1/payment-links'
# Fungsi untuk mengambil jawaban dari OpenAI
# Fungsi lainnya dan pengaturan bot dapat dipertahankan
# Handle Command /start
# Diubah menjadi jumlah_koin awalnya
# Variabel jumlah_koin_awal seharusnya dideklarasikan tanpa "global" karena ini adalah variabel biasa
### JANGAN DI UBAH #####
########### UBAH di bagian passnya UNTUK NGATUR
## dan jangan sekali kali ubah baris "Jumlah saldo Anda: " di skrip ini:
# Membuat dictionary passwords untuk menyimpan kata sandi pengguna
# Menonaktifkan pengecekan thread untuk melakukan reset
import telebot
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

GROUP_ID = int(os.getenv("GROUP_ID"))
JOIN_LINK = os.getenv("JOIN_LINK")

# Fungsi untuk memeriksa apakah pengguna berada dalam whitelist
def is_whitelisted(user_id):
    with open('/root/izmiftah/whitelist.json', 'r') as file:
        whitelist = json.load(file)
    return user_id in whitelist

# Fungsi untuk menambahkan pengguna ke whitelist
def add_to_whitelist(user_id):
    with open('/root/izmiftah/whitelist.json', 'r') as file:
        whitelist = json.load(file)
    if user_id not in whitelist:
        whitelist.append(user_id)
        with open('/root/izmiftah/whitelist.json', 'w') as file:
            json.dump(whitelist, file)
    
class UserManagement:
    def __init__(self):
        self.blocked_file = 'blocked.json'
        self.whitelist_file = 'whitelist.json'
        self.ensure_files()

    def ensure_files(self):
        if not os.path.exists(self.blocked_file):
            with open(self.blocked_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(self.whitelist_file):
            with open(self.whitelist_file, 'w') as f:
                json.dump([], f)

    def load_json(self, file):
        with open(file, 'r') as f:
            return json.load(f)

    def save_json(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    def is_blocked(self, user_id):
        blocked_users = self.load_json(self.blocked_file)
        return user_id in blocked_users

    def block_user(self, user_id):
        blocked_users = self.load_json(self.blocked_file)
        if user_id not in blocked_users:
            blocked_users.append(user_id)
            self.save_json(self.blocked_file, blocked_users)

    def is_whitelisted(self, user_id):
        whitelisted_users = self.load_json(self.whitelist_file)
        return user_id in whitelisted_users

    def whitelist_user(self, user_id):
        whitelisted_users = self.load_json(self.whitelist_file)
        if user_id not in whitelisted_users:
            whitelisted_users.append(user_id)
            self.save_json(self.whitelist_file, whitelisted_users)

    def generate_token(self):
        return secrets.token_urlsafe(16)

    def hide_token(self, user_id, token):
        token_file = f'token_{user_id}.json'
        with open(token_file, 'w') as f:
            json.dump({"token": token}, f, indent=4)

    def delete_user_from_whitelist(self, user_id):
        whitelisted_users = self.load_json(self.whitelist_file)
        if user_id in whitelisted_users:
            whitelisted_users.remove(user_id)
            self.save_json(self.whitelist_file, whitelisted_users)
            token_file = f'token_{user_id}.json'
            if os.path.exists(token_file):
                os.remove(token_file)

user_mgmt = UserManagement()

passwords = new_saldo

# Data saldo pengguna (contoh data dummy)
saldo_pengguna = jumlah_koin
# Inisialisasi variabel-variabel
file_skrip = 'skrip.txt'
keyword1_skrip = 'fitur.txt'
keyword2_skrip = 'objek.txt'

import telebot

# Dictionary to store the locked status of each feature
locked_features = {
    '/acak': 'untuk mengacak ringkas suatu kalimat',
    '/artikan': 'untuk terjemahkan media/pesan',
    '/terjemahkan': 'untuk menerjemahkan pesan',
    '/ddos': 'untuk fitur banned wa',
    '/video': 'untuk menghasilkan link video',
    '/koding': 'untuk memembantu membuat skrip sebanyak mungkin',
    '/yt': 'untuk mendownload video dari youtube',
    '/unduh': 'untuk mengunduh link berisikan video',
    '/pdf': 'untuk mengubah dengan reply pesan ke pdf',
    '/warna': 'untuk menghasilkan pallet warna untuk mendesain gambar',
    '/apk': 'generate random ide apk',
    '/newapk': 'generate random link for new apk',
    '/musik': 'untuk memutar/mendownload musik YT',
    '/tulis': 'untuk menulis ke file text',
    '/ai': 'untuk menulis dengan secara otomatis ke output_novel.pdf',
    '/ai_prompt': 'yakni untuk mengisi prompt sebelum di ubah ke prompt ke text',
    '/bukablokir': 'untuk membuka blokir saat saldo 0',
    '/reset': 'untuk mereset saldo',
    '/passwordku': 'untuk melihat password yang berlaku',
    '/help': 'untuk melihat bantuan',
    '/start': 'untuk memulai ulang',
    '/link': 'untuk menampilkan link seputar pembayaran',
    '/upload': 'yakni untuk mengupload file tersebut',
    '/keyword': 'untuk update database untuk generate ai prompt nya',
    '/my_id': 'untuk melihat id user bot kamu',
    '/pembayaran': 'untuk melakukan pembayaran',
    '/bayar': 'untuk pembayaran alternatif',
    '/write': 'yakni untuk menulis secara otomatis ke file output.html nya',
    '/dnsinfo': 'untuk mendapatkan info seputar hosting domain tersebut',
    '/dork': 'untuk menjejahi domain dan url dengan dua katakunci misal: google/.com',
    '/dorking': 'dorking katakunci/ domain untuk cara memakainya',
    '/scan': 'untuk scanning domain dan url',
    '/payment': 'untuk melakukan pembayaran dengan password',
    '/saldo': 'untuk melihat sisa saldo',
    '/cek_saldo': 'untuk melihat saldo user kamu',
    '/berbagi': 'untuk berbagi saldo ke yang lain',
    '/reset_saldo': 'untuk mereset saldo nya ke nilai tertentu',
    '/topup': 'untuk melakukan top-up',
    '/blokir_koin': 'yakni untuk mengganti penggunaan saldo kamu dengan memblokir saldo yang lain',
    '/blokir': 'yakni untuk blokir fungsi bot untuk di gunakan',
    '/download_html': 'yakni untuk mendownload hasil tulisan versi output.html',
    '/download_final': 'yakni untuk mendownload file final karya tulis pdfnya',
    '/download_hasil': 'gunakan ini untuk mendapatkan ai promptnya',
    '/download_novel': 'gunakan ini untuk mendapatkan pdf output_novel nya',
    '/download2': 'yakni untuk mendownload file output.txt nya berupa hasil scan bug atau bisa juga hasil ai promt',
    '/download3': 'yakni untuk mendownload file ai.txt nya berupa hasil dari ai promt',
    '/download_cover2': 'yakni untuk mendownload file cover pdfnya',
    '/download_cover': 'yakni untuk mendownload file cover.png nya',
    '/download_html1': 'yakni untuk mendownload hasil tulisan versi cover.html',
    '/download_html2': 'yakni untuk mendownload hasil tulisan versi pdf.html',
    '/berbagi_saldo': 'untuk berbagi saldo',
    '/update_pdf': 'untuk mengupdate file pdf nya',
    '/jadwal' : 'untuk membuat sebuah jadwal'
}

import telebot
import random

# Fungsi untuk melakukan pengacakan teks
def shuffle_text(text):
    # Acak kata-kata dalam teks
    shuffled_text = ' '.join(random.sample(text.split(), len(text.split())))
    return shuffled_text

# Handler untuk perintah /acak
@bot.message_handler(commands=['acak'])
def acak(message):
    try:
        # Ambil pesan yang ingin diacak
        text_to_shuffle = message.reply_to_message.text
        # Assert bahwa pesan yang dijawab tidak kosong
        assert text_to_shuffle, "Tidak ada pesan yang dijawab. Mohon balas ke pesan yang ingin Anda acak dengan perintah /acak."
        # Acak kata-kata dalam pesan
        shuffled_text = shuffle_text(text_to_shuffle)
        # Kirim pesan yang diacak ke pengguna
        bot.reply_to(message, shuffled_text)
    except AssertionError as e:
        # Tangani jika tidak ada pesan yang dijawab
        bot.reply_to(message, str(e))
    except Exception as e:
        # Tangani kesalahan umum
        bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')


# Fungsi untuk membuat koneksi ke database SQLite
def create_db_connection():
    return sqlite3.connect('kunci.db')

# Koneksi ke database SQLite
conn = sqlite3.connect('kunci.db')
c = conn.cursor()

# Membuat tabel untuk menyimpan status kunci dan kata sandi
c.execute('''CREATE TABLE IF NOT EXISTS locked_commands (
                command TEXT PRIMARY KEY,
                description TEXT,
                password TEXT
             )''')

# Commit perubahan dan tutup koneksi
conn.commit()
conn.close()


# Fungsi untuk menutup koneksi ke database saat bot dimatikan
def close_db_connection(conn):
    conn.close()

# Fungsi untuk membaca perintah yang terkunci dari database dan menyimpannya dalam sebuah list
def get_locked_commands():
    conn = create_db_connection()  # Memanggil fungsi untuk membuat koneksi ke database
    c = conn.cursor()
    c.execute('''SELECT command FROM locked_commands''')
    locked_commands = [f"/{row[0]}" for row in c.fetchall()]
    close_db_connection(conn)  # Memanggil fungsi untuk menutup koneksi ke database
    return locked_commands

# Menginisialisasi daftar perintah yang terkunci
locked_commands = get_locked_commands()

# Menginisialisasi fitur yang terkunci dengan daftar perintah yang terkunci
locked_features = locked_commands

# Set blokir_aktif ke True secara default
blokir_aktif = None
# Variabel untuk menyimpan perintah yang terkunci
locked_commands = get_locked_commands()

import os
import sqlite3
import telebot
import json
import subprocess
from dotenv import load_dotenv
from threading import local
from time import sleep

# Thread-local storage for database connections
thread_local = local()
db_name = 'miftah'


def handle_commands(message):
    user_id = message.from_user.id
    if not user_manager.is_whitelisted(user_id):
        bot.reply_to(message, "You are blacklisted and cannot use this bot.")
        return

    if user_manager.is_whitelisted(user_id):
        command = message.text.lstrip('+')
        output = run_system_command(command)
        bot.reply_to(message, f"Output of {command}:\n{output}")
    else:
        bot.reply_to(message, "You are not authorized to use this bot. Please register first.")

def get_db_connection(db_name):
    if not hasattr(thread_local, db_name):
        conn = sqlite3.connect(f'{db_name}.db', check_same_thread=False)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        setattr(thread_local, db_name, (conn, cursor))
    return getattr(thread_local, db_name)
    
# Fungsi untuk membuat dan menginisialisasi database admin
def init_db():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        admin_id INTEGER NOT NULL
                      )''')
    conn.commit()
    conn.close()

# Fungsi untuk menyimpan admin_id ke database
def save_admin_id(admin_id):
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO admin (admin_id) VALUES (?)', (admin_id,))
    conn.commit()
    conn.close()

# Fungsi untuk memuat admin_id dari database
def load_admin_id():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT admin_id FROM admin ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Inisialisasi database
init_db()

# Ambil admin_id dari environment variable atau database
admin_id = os.getenv('adminnya')
if admin_id is None:
    admin_id = load_admin_id()
    if admin_id is None:
        raise Exception("Admin ID tidak ditemukan. Set environment variable 'adminnya' atau simpan admin_id di database.")


def generate_token(user_id):
    import uuid
    return str(uuid.uuid4())

tokennya = generate_token(new_saldo)
tokenmu = generate_token(admin_id) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    pengguna = message.from_user.username
    result = inisial
    user_id = message.from_user.id
    bot.send_message(admin_id, text=f"Token to confirm: {tokennya} for user: {tokenmu} \nUser ID: {user_id}")
    if message.chat.id:
        bot.send_message(message.chat.id, f"Welcome back, {pengguna}!")
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
        terblokir(user_id)
        hadeh.add(user_id)
        blokir_aktif = True
    if blokir_nonaktif(message):
        unblock_user(id)
        bot.send_message(message.chat.id, f"Anda sudah terblokir silahkan buka dengan /bukablokir")
        if record_unblocked_user:
            bot.send_message(message.chat.id, f"Anda sudah terblokir silahkan buka dengan /bukablokir dengan passswordnya")
    if result:
        bot.send_message(message.chat.id, "Selamat datang di AI bot buatan saya. silahkan ketik @(passwordnya) atau silakan pilih menu yang tersedia:", reply_markup=main_menu_markup())
    else:
        #user_mgmt.block_user(new_saldo)
        #user_mgmt.is_blocked(user_id)
        token = user_mgmt.generate_token()
        user_mgmt.hide_token(user_id, token)
        bot.send_message(user_id, f"silahkan melakukan pembayaran pada link: {link_jualan} yang tersedia")
        bot.reply_to(message, "You are not whitelisted. Please register with #daftar.")
        
# Handler untuk pesan dengan hanya satu kata
@bot.message_handler(func=lambda message: len(message.text.split('/')) > 1 and message.text.split()[0].replace('/', '@/') in locked_commands)
def handle_single_word_message(message):
    user_id = message.from_user.id
    global blokir_aktif
    command = message.text.split()[0].replace('@@', '/')  # Mengambil hanya perintah dari pesan dan mengganti '/' menjadi '@'

    if not user_manager.is_whitelisted(user_id) and command and blokir_aktif in locked_commands:
        bot.reply_to(message, "Maaf, bot ini disita hingga beberapa abad.")
        return 
    if user_mgmt.block_user(user_id):
        bot.reply_to(message, "Maaf, bot ini telah di hapuskan dari peradaban")
        return 
    else:
        if command in locked_commands:
            bot.reply_to(message, "Fitur ini telah dihapus dari peradaban. Silakan jalankan ulang dan coba lagi.")
        else:
            bot.reply_to(message, f"Perintah {command} tidak terkunci. Silakan gunakan dengan bebas.")

# Handler untuk perintah yang terkunci dengan sandi
@bot.message_handler(func=lambda message: len(message.text.split(' ')) > 1 and message.text.split()[0].replace('@/', '@@') in locked_commands)
def handle_locked_command(message):
    user_id = message.from_user.id
    global blokir_aktif
    command = message.text.split()[0].replace('@@', '/')  # Mengambil hanya perintah dari pesan dan mengganti '/' menjadi '@'

    if blokir_aktif:
        bot.reply_to(message, "Maaf, bot ini disita hingga beberapa abad, silahkan #daftar terlebih dahulu.")
        return 
    if terblokir and command and blokir_aktif in locked_commands:
        bot.reply_to(message, "Maaf, bot ini disita hingga beberapa abad.")
        return 
    if terblokir and new_saldo and blokir_aktif in user_mgmt.block_user(user_id):
        bot.reply_to(message, "Maaf, bot ini telah di hapuskan dari peradaban")
        return 
    else:
        if command in locked_commands:
            bot.reply_to(message, "Fitur ini telah dihapus dari peradaban. Silakan jalankan ulang dan coba lagi.")
        else:
            bot.reply_to(message, f"Perintah {command} tidak terkunci. Silakan gunakan dengan bebas.")

# Fungsi untuk mengaktifkan/menonaktifkan fitur blokir
@bot.message_handler(func=lambda message: message.text.startswith(f'/{passnya}'))
def blokir_aktif_command(message):
    global blokir_aktif
    command_parts = message.text.split()
    if len(command_parts) >= 2:
        status = command_parts[1].lower()
        response = toggle_block_mode(status, message)
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Format perintah salah. Gunakan 'login' atau 'keluar' sebagai tambahan")

# Fungsi untuk mengaktifkan/menonaktifkan fitur blokir
def toggle_block_mode(status, message):
    global blokir_aktif
    user_id = message.from_user.id
    if status == 'keluar':
        bot.reply_to(message, "Fitur ini telah dihapus dari peradaban. Silakan jalankan ulang dan coba lagi.")
        blokir_aktif = True
        hadeh.add(new_saldo)
        user_id = message.from_user.id
        raise PermissionError(f"User {user_id} is blocked from accessing this bot.")
        if message.chat.id != GROUP_ID and not is_whitelisted(message.from_user.id):
        	send_join_group_message(message.chat.id)
        blokir_aktif(message.from_user.id)
        if not user_mgmt.is_blocked(user_id):
            user_mgmt.block_user(user_id)
            user_mgmt.delete_user_from_whitelist(user_id)
            bot.reply_to(message, "Welcome to the bot!")
            return "maaf bot ini telah di hilangkan dari perdaban manusia."
        return "Blokir telah diaktifkan."
    elif status == 'login':
        terbuka = True
        blokir_nonaktif = False
        if terbuka == False:
            blokir_aktif = False
        if user_id in hadeh:
            hadeh.remove(user_id)
        else:
            print(f"User ID {user_id} not found in hadeh.")
        return "Blokir telah dinonaktifkan."
    else:
        return "Format perintah salah. Gunakan '/passwordnya lalu keluar' atau 'login'"

# Modifikasi fungsi ban_command
# Modifikasi fungsi miftah_command
@bot.message_handler(commands=['unity'])
def miftah_command(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_aktif != True and blokir_nonaktif != False and terbuka == True:         
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")
    else:
        conn = create_db_connection()  # Membuat koneksi ke database
        c = conn.cursor()
        command_parts = message.text.split()
        if len(command_parts) >= 2:
            feature_name = command_parts[1]
            
            # Periksa apakah perintah ada dalam daftar yang terkunci
            locked_command = f"/{feature_name}"
            if locked_command in locked_commands:
                c.execute('''DELETE FROM locked_commands WHERE command = ?''', (feature_name,))
                conn.commit()
                locked_commands.remove(locked_command)
                message.text = message.text.replace('/', '/@')
                bot.reply_to(message, f"Fitur {feature_name} telah dibuka.")
            else:
                bot.reply_to(message, f"Perintah {locked_command} tidak terkunci.")
        else:
            bot.reply_to(message, "Format perintah salah. Gunakan: '/unity [command]'")
        close_db_connection(conn)  # Menutup koneksi ke database setelah selesai


# Modifikasi fungsi izma_command
@bot.message_handler(commands=['U8'])
def izma_command(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_aktif:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")
    else:
        command_parts = message.text.split()
        if len(command_parts) >= 2:
            feature_name = command_parts[1]
            locked_command = f"/{feature_name}"

            conn = create_db_connection()
            c = conn.cursor()
            c.execute('''INSERT INTO locked_commands (command) VALUES (?)''', (feature_name,))
            conn.commit()
            close_db_connection(conn)

            if locked_command not in locked_commands:
                locked_commands.append(locked_command)
                bot.reply_to(message, f"Perintah {locked_command} telah berhasil diblokir.")
            else:
                bot.reply_to(message, f"Perintah {locked_command} sudah terblokir sebelumnya.")
        else:
            bot.reply_to(message, "Format perintah salah. Gunakan: '/U8 [command]'")

import telebot
import numpy as np
import pandas as pd
import urllib3
from bs4 import BeautifulSoup
import time

# Initialize libraries
http = urllib3.PoolManager(timeout=10)

# Function to perform Google search across multiple pages
def google_search(keyword, num_pages=10):
    results = []
    for page in range(num_pages):
        query = '+'.join(keyword.split())
        url = f"https://www.google.com/search?q={query}&start={page * 10}"
        try:
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, 'html.parser')
            for item in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
                title = item.get_text()
                results.append(title)
        except urllib3.exceptions.HTTPError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
    return results

# Command handler for '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use the command 'DORKING {keyword1>keyword2}' to search for keywords.")

# Command handler for 'DORKING'
@bot.message_handler(func=lambda message: message.text.startswith('/DORKING'))
def handle_dorking(message):
    try:
        keywords = message.text.replace('/DORKING', '').strip().split('>')
        if len(keywords) != 2:
            bot.reply_to(message, "Please use the format: /DORKING {keyword1>keyword2}")
            return
        keyword1, keyword2 = keywords
        result1 = google_search(keyword1)
        result2 = google_search(keyword2)
        
        # Ensure both lists are of the same length
        max_length = max(len(result1), len(result2))
        result1.extend([''] * (max_length - len(result1)))
        result2.extend([''] * (max_length - len(result2)))
        
        result_df = pd.DataFrame({
            'Keyword1': result1,
            'Keyword2': result2
        })
        
        # Save DataFrame to text file
        result_str = result_df.to_string(index=False)
        with open('/root/izmiftah/dork_hasil.txt', 'w') as file:
            file.write(result_str)
        
        bot.reply_to(message, "Silahkan jalankan /download  dork_hasil.txt/n untuk melihat hasilnya")
    
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")
        

import telebot
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import numpy as np
import os

GOOGLE_FONTS_API_URL = 'https://fonts.googleapis.com/css2?family='

class TextToLogoGenerator:
    def __init__(self, font_name, text, image):
        self.font_name = font_name
        self.text = text
        self.image = image
        self.font = self.download_font()

    def download_font(self):
        font_url = f'{GOOGLE_FONTS_API_URL}{self.font_name.replace(" ", "+")}&display=swap'
        font_response = requests.get(font_url)
        if font_response.status_code != 200:
            raise Exception(f"Font {self.font_name} tidak ditemukan.")

        css_text = font_response.text
        ttf_url_start = css_text.find('url(') + 4
        ttf_url_end = css_text.find(')', ttf_url_start)
        ttf_url = css_text[ttf_url_start:ttf_url_end].strip('\'"')

        ttf_response = requests.get(ttf_url)
        if ttf_response.status_code != 200:
            raise Exception(f"Tidak dapat mengunduh file TTF untuk font {self.font_name}.")

        font_ttf = BytesIO(ttf_response.content)
        font_ttf.seek(0)
        return ImageFont.truetype(font_ttf, 100)

    def generate_logo(self):
        draw = ImageDraw.Draw(self.image)
        text_bbox = draw.textbbox((0, 0), self.text, font=self.font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Create a new image with the text size
        text_image = Image.new('L', (text_width, text_height), 0)
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((0, 0), self.text, fill=255, font=self.font)

        # Create a mask from the text image
        mask = np.array(text_image)
        mask = np.stack([mask] * 3, axis=-1)  # Convert to RGB

        # Resize the input image to fit the text
        resized_image = self.image.resize((text_width, text_height))

        # Composite the text mask onto the resized image
        logo = Image.fromarray(np.where(mask, resized_image, 0).astype('uint8'))

        return logo

@bot.message_handler(commands=['Logo'])
def handle_logo_command(message):
    try:
        command_parts = message.text.split(' ', 3)
        if len(command_parts) < 4:
            bot.reply_to(message, "Format command tidak valid. Gunakan format: Logo {bahasa} {nama font} {tulisan}")
            return

        language = command_parts[1]
        font_name = command_parts[2]
        text = command_parts[3]

        if message.reply_to_message and message.reply_to_message.photo:
            file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            image = Image.open(BytesIO(downloaded_file))

            generator = TextToLogoGenerator(font_name, text, image)
            logo = generator.generate_logo()

            output = BytesIO()
            logo.save(output, format='PNG')
            output.seek(0)

            bot.send_photo(message.chat.id, output, caption="Berikut adalah logo Anda")

    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

import telebot
from PIL import Image, ImageEnhance, ImageOps
import requests
from io import BytesIO
import removebg
import os
from dotenv import load_dotenv

REMOVE_BG_API_KEY = os.getenv('bgremover')

def remove_background(image_path):
    rmbg = removebg.RemoveBg(REMOVE_BG_API_KEY, "error.log")
    rmbg.remove_background_from_img_file(image_path)
    bg_removed_path = image_path.replace(".jpg", ".jpg_no_bg.png").replace(".jpeg", ".jpeg_no_bg.png").replace(".png", ".png")
    return bg_removed_path

def sharpen_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Sharpness(image)
    sharpened_image = enhancer.enhance(2.0)  # Increase sharpness
    sharpened_image_path = image_path.replace(".png", "_sharpened.png")
    sharpened_image.save(sharpened_image_path)
    return sharpened_image_path

def not_image(image_path):
    image = Image.open(image_path)
    inverted_image = ImageOps.invert(image.convert("RGB"))
    inverted_image_path = image_path.replace(".png", "_inverted.png")
    inverted_image.save(inverted_image_path)
    return inverted_image_path

@bot.message_handler(commands=['bg'])
def handle_bg_command(message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            image_path = file_info.file_path.split('/')[-1]
            with open(image_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            
            bg_removed_path = remove_background(image_path)
            sharpened_image_path = sharpen_image(bg_removed_path)

            with open(bg_removed_path, 'rb') as photo:
                bot.send_document(message.chat.id, photo, reply_to_message_id=message.message_id)
            
            os.remove(image_path)
            if os.path.exists(bg_removed_path):
                os.rename(sharpened_image_path, 'BG.png')
            else:
                bot.reply_to(message, "Failed to rename the file. BG.png not found.")
        else:
            bot.reply_to(message, "Reply to a photo with the command '/bg'")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['Bg'])
def handle_sharpen_command(message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            image_path = file_info.file_path.split('/')[-1]
            with open(image_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            
            sharpened_image_path = sharpen_image(image_path)

            with open(sharpened_image_path, 'rb') as photo:
                bot.send_document(message.chat.id, photo, reply_to_message_id=message.message_id)
            
            if os.path.exists(sharpened_image_path):
                os.rename(sharpened_image_path, 'BG_sharpened.png')
            else:
                bot.reply_to(message, "Failed to rename the file. BG_sharpened.png not found.")
        else:
            bot.reply_to(message, "Reply to a photo with the command '/Bg'")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['BG'])
def handle_not_command(message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            image_path = file_info.file_path.split('/')[-1]
            with open(image_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            
            inverted_image_path = not_image(image_path)

            with open(inverted_image_path, 'rb') as photo:
                bot.send_document(message.chat.id, photo, reply_to_message_id=message.message_id)
            
            if os.path.exists(inverted_image_path):
                os.rename(inverted_image_path, 'BG_inverted.png')
            else:
                bot.reply_to(message, "Failed to rename the file. BG_inverted.png not found.")
        else:
            bot.reply_to(message, "Reply to a photo with the command '/BG'")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

import telebot
import paramiko

# Data server
SERVER = "indo.akademiku.site"
USERNAME = "root"
PASSWORD = "alive4545"

@bot.message_handler(commands=['VPN'])
def create_vpn(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise ValueError("Format salah. Gunakan: /VPN username password")
        
        _, username, password = parts
        
        # Membuat koneksi SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(SERVER, username=USERNAME, password=PASSWORD)
        
        # Membuat user baru
        command = f"sudo -S adduser --disabled-password --gecos '' {username}"
        stdin, stdout, stderr = client.exec_command(command)
        
        # Mengatur password
        command = f"sudo -S echo '{username}:{password}' | sudo chpasswd"
        stdin, stdout, stderr = client.exec_command(command)
        
        # Restart layanan SSH
        client.exec_command('sudo systemctl restart sshd')
        
        # Informasi akun
        response = (
            f"🎉 Akun VPN SSH berhasil dibuat di {SERVER}! 🎉\n\n"
            f"🧑‍💻 User: {username}\n"
            f"🔒 Password: {password}\n\n"
            f"🔧 Service & Port:\n"
            f"  - sslh: 443\n"
            f"  - stunnel4: 4443, 445\n"
            f"  - openvpn: 1194\n"
            f"  - apache2: 81\n"
            f"  - sshd: 443, 22\n"
            f"  - dropbear: 143, 123, 110, 109\n"
            f"  - UDP: 1-65535\n"
            f"  - Squid: 8080, 3128\n"
        )
        
    except Exception as e:
        response = f"❌ Gagal membuat akun: {str(e)}"
    
    bot.send_message(message.chat.id, response)


import requests
from PIL import Image
import numpy as np
from io import BytesIO
import telebot
import pyfiglet

def get_font_options():
    # Mendapatkan daftar font yang tersedia
    try:
        figlet = pyfiglet.Figlet()
        return figlet.getFonts()
    except Exception as e:
        return f"Terjadi kesalahan saat mendapatkan daftar font: {str(e)}"

FONT_OPTIONS = get_font_options()

def generate_ascii_logo(text, font_name):
    try:
        # Membersihkan teks dari spasi ekstra
        text = text.strip()
        
        # Memeriksa apakah font yang dipilih tersedia dalam daftar
        if font_name not in FONT_OPTIONS:
            return f"Font '{font_name}' tidak tersedia. Pilih dari: {', '.join(FONT_OPTIONS)}"
        
        # Memeriksa panjang teks agar sesuai dengan ukuran font
        if len(text) > 10:
            return "Teks terlalu panjang untuk dihasilkan dengan font ASCII."
        
        ascii_art = pyfiglet.figlet_format(text, font=font_name)
        return ascii_art
        
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

def generate_ascii_art(image, font_name, text):  
    try:
        # Karakter yang akan digunakan untuk menggambarkan teks
        ascii_chars = "@%#*+=-:. "
        # Menghitung skala konversi dari nilai piksel ke karakter ASCII
        scale = len(ascii_chars) / 256
        # Mengubah gambar menjadi grayscale
        image_gray = image.convert("L")
        # Mengubah gambar menjadi array numpy
        image_array = np.array(image_gray)
        # Mengonversi nilai piksel menjadi karakter ASCII
        ascii_art = "\n".join(["".join([ascii_chars[int(pixel * scale)] for pixel in row]) for row in image_array])
        return ascii_art
        
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

@bot.message_handler(commands=['logo'])
def process_logo(message):
    try:
        # Memeriksa apakah pesan memiliki teks (tanpa memeriksa apakah itu merupakan balasan)
        if message.text:
            # Memeriksa apakah pesan memiliki argumen yang sesuai
            command_parts = message.text.split(' ', 2)
            if len(command_parts) < 3:
                bot.reply_to(message, f"Format command tidak valid. Gunakan format: /logo [font] [teks]. Pilih font dari: {', '.join(FONT_OPTIONS)}")
                return
            
            font_name = command_parts[1]
            text = command_parts[2]
            
            # Membuat logo ASCII
            ascii_art = generate_ascii_logo(text, font_name)
            
            # Mengirim ASCII art sebagai pesan
            bot.reply_to(message, ascii_art)

    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

@bot.message_handler(content_types=['photo'])
def process_photo(message):
    try:
        if message.reply_to_message and message.reply_to_message.photo:
            file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            image = Image.open(BytesIO(downloaded_file))

            # Anda dapat mengganti "font_name" dengan nama font yang diinginkan dan "Sample text" dengan teks yang diinginkan
            font_name = "standard"  # Ganti dengan nama font yang sesuai
            ascii_art = generate_ascii_art(image, font_name, "Sample text")  # Ganti "Sample text" dengan teks yang diinginkan

            # Simpan ASCII art ke dalam file teks
            with open("ascii_art.txt", "w") as file:
                file.write(ascii_art)

            # Mengirim file ASCII art sebagai pesan
            bot.send_document(message.chat.id, open("ascii_art.txt", "rb"))

    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

@bot.message_handler(commands=['LOGO'])
def handle_photo_command(message):
    process_photo(message)

@bot.message_handler(commands=['logo'])
def handle_logo_command(message):
    process_logo(message)

import telebot
from datetime import datetime, timedelta
import random
import os
import csv

# Define weather options
weather_options = ['Mendung', 'Berawan', 'Suram', 'Bencana', 'Hujan', 'Tidak Beratur', 'Hujan Rintik', 'Hujan Deras', 'Hujan Berangin', 'Cerah', 'Gelap', 'Badai']

def load_weather_data(user_id):
    filename = f'cuaca_{user_id}.csv'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return [row for row in reader]
    return []

def save_weather_data(user_id, weather_data):
    filename = f'cuaca_{user_id}.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Tanggal', 'Cuaca'])
        writer.writerows(weather_data)

@bot.message_handler(commands=['cuaca'])
def cuaca(message):
    user_id = message.from_user.id
    try:
        words = message.text.split()
        if len(words) != 4:
            bot.send_message(message.chat.id, 'Perintah tidak valid. Contoh: /cuaca (tanggal-tanggal dari) (cuaca kemarin) (target hari)')
            return

        tanggal_dari = datetime.strptime(words[1], '%d/%m/%Y')
        tanggal_kemarin = datetime.strptime(words[2], '%d/%m/%Y')
        target_hari = datetime.strptime(words[3], '%d/%m/%Y')

        if tanggal_kemarin < tanggal_dari:
            bot.send_message(message.chat.id, 'Tanggal kemarin tidak boleh lebih kecil dari tanggal dari')
            return

        # Generate random weather data for the past month
        weather_data_last_month = [random.choice(weather_options) for _ in range(21)]

        # Calculate average weather score for the past month
        average_weather_score = sum(weather_options.index(weather) for weather in weather_data_last_month) / len(weather_data_last_month)

        # Predict weather for the next month
        predicted_weather_next_month = []
        for i in range(30):
            if average_weather_score > 6:
                predicted_weather_next_month.append('Cerah')
            elif average_weather_score < 2:
                predicted_weather_next_month.append('Hujan')
            else:
                predicted_weather_next_month.append(random.choice(weather_options))

        # Send predicted weather for the next month
        bot.send_message(message.chat.id, 'Perkiraan cuaca untuk bulan kemudian:')
        for i, weather in enumerate(predicted_weather_next_month, 1):
            bot.send_message(message.chat.id, f'Hari {i}: {weather}')

    except Exception as e:
        bot.send_message(message.chat.id, 'Terjadi kesalahan: ' + str(e))

@bot.message_handler(commands=['Cuaca'])
def save(message):
    user_id = message.from_user.id
    try:
        words = message.text.split()
        if len(words) != 2:
            bot.send_message(message.chat.id, 'Perintah tidak valid. Contoh: /Cuaca (cuaca)')
            return

        cuaca_hari_ini = words[1]
        cuaca_database = load_weather_data(user_id)
        cuaca_database.append([datetime.now().strftime("%d/%m/%Y"), cuaca_hari_ini])

        save_weather_data(user_id, cuaca_database)
        bot.send_message(message.chat.id, 'Cuaca telah disimpan')

    except Exception as e:
        bot.send_message(message.chat.id, 'Terjadi kesalahan: ' + str(e))

@bot.message_handler(commands=['CUACA'])
def terapkan(message):
    user_id = message.from_user.id
    try:
        cuaca_database = load_weather_data(user_id)
        if len(cuaca_database) < 21:
            bot.send_message(message.chat.id, 'Data cuaca tidak cukup untuk membuat prediksi. Simpan data cuaca setidaknya selama 21 hari.')
            return

        # Calculate average weather score for the past 21 days
        average_weather_score = sum(weather_options.index(row[1]) for row in cuaca_database[-21:]) / 21

        # Predict weather for the next month
        predicted_weather_next_month = []
        for i in range(30):
            if average_weather_score > 6:
                predicted_weather_next_month.append('Cerah')
            elif average_weather_score < 2:
                predicted_weather_next_month.append('Hujan')
            else:
                predicted_weather_next_month.append(random.choice(weather_options))

        # Send predicted weather for the next month
        bot.send_message(message.chat.id, 'Perkiraan cuaca untuk bulan kemudian:')
        for i, weather in enumerate(predicted_weather_next_month, 1):
            bot.send_message(message.chat.id, f'Hari {i}: {weather}')

    except Exception as e:
        bot.send_message(message.chat.id, 'Terjadi kesalahan: ' + str(e))


import os
import telebot
import cv2
from pydub import AudioSegment
from PyPDF2 import PdfFileReader, PdfFileWriter
import requests
from telebot.types import Message

source_dir = '/root/izmiftah/'

@bot.message_handler(commands=['convert'])
def handle_convert(message: Message):
    try:
        _, *args = message.text.split(' ')
        if len(args) < 3:
            raise ValueError("Invalid number of arguments. Please provide a /convert (source file), (ekstensi: mp4), and (output name).")
        
        source_file, file_type, output_name = args
        source_file = os.path.join(source_dir, source_file)  # Mendapatkan direktori kerja saat ini dan menggabungkannya dengan nama file sumber
        
        if not os.path.exists(source_file):
            raise ValueError("File not found. Please provide a valid file path.")
        
        output_file = convert_file(source_file, file_type, output_name)
        send_converted_file(message, output_file)
        cleanup_files([output_file])
    except ValueError as ve:
        bot.reply_to(message, str(ve))
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

def convert_file(source_file, file_type, output_name):
    ext = file_type.lower()
    output_file = f"hasil/{output_name}.{ext}"
    os.makedirs('hasil', exist_ok=True)
    
    if ext in ['mp4', 'avi', 'mov']:
        convert_video(source_file, output_file)
    elif ext in ['mp3', 'wav', 'ogg']:
        audio = AudioSegment.from_file(source_file)
        audio.export(output_file, format=ext)
    elif ext in ['pdf']:
        pdf_reader = PdfFileReader(open(source_file, 'rb'))
        pdf_writer = PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        with open(output_file, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
    elif ext in ['zip']:
        import zipfile
        with zipfile.ZipFile(output_file, 'w') as zipf:
            zipf.write(source_file)
    elif ext in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
        convert_image(source_file, output_file, ext)
    elif ext in ['txt', 'doc', 'docx', 'rtf']:
        # Lakukan konversi dokumen teks
        pass
    else:
        raise ValueError(f"Unsupported file extension type: {file_type}")
    
    return output_file

def convert_video(source_file, output_file):
    cap = cv2.VideoCapture(source_file)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def convert_image(source_file, output_file, ext):
    # Lakukan konversi gambar ke format yang diinginkan
    img = cv2.imread(source_file)
    cv2.imwrite(output_file, img)

def send_converted_file(message: Message, output_file: str):
    with open(output_file, 'rb') as f:
        bot.send_document(message.chat.id, f)

def cleanup_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

import os
import telebot
import cv2
from pydub import AudioSegment
from PyPDF2 import PdfFileReader, PdfFileWriter
from telebot.types import Message, InputFile
import zipfile

# Utility functions
def is_supported_file_type(file_type):
    return file_type in ['mp4', 'avi', 'mov', 'mp3', 'wav', 'ogg', 'pdf', 'zip', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'txt', 'doc', 'docx', 'rtf']

def convert_video(source_file, output_file):
    cap = cv2.VideoCapture(source_file)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def convert_image(source_file, output_file):
    img = cv2.imread(source_file)
    cv2.imwrite(output_file, img)

def convert_file(source_file, file_type, output_name):
    ext = file_type.lower()
    output_file = f"hasil/{output_name}.{ext}"
    os.makedirs('hasil', exist_ok=True)
    
    if ext in ['mp4', 'avi', 'mov']:
        convert_video(source_file, output_file)
    elif ext in ['mp3', 'wav', 'ogg']:
        audio = AudioSegment.from_file(source_file)
        audio.export(output_file, format=ext)
    elif ext == 'pdf':
        pdf_reader = PdfFileReader(open(source_file, 'rb'))
        pdf_writer = PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        with open(output_file, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
    elif ext == 'zip':
        with zipfile.ZipFile(output_file, 'w') as zipf:
            zipf.write(source_file)
    elif ext in ['png', 'jpg', 'jpeg', 'gif', 'bmp']:
        convert_image(source_file, output_file)
    elif ext in ['txt', 'doc', 'docx', 'rtf']:
        # Text document conversion can be added here
        pass
    else:
        raise ValueError(f"Unsupported file extension type: {file_type}")
    
    return output_file

def send_converted_file(message: Message, output_file: str):
    with open(output_file, 'rb') as f:
        bot.send_document(message.chat.id, InputFile(f))

def cleanup_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

@bot.message_handler(commands=['Convert'])
def handle_convert(message: Message):
    try:
        reply_message = message.reply_to_message
        if not reply_message or not reply_message.document:
            raise ValueError("Please reply to a message containing the file to convert.")
        
        _, *args = message.text.split(' ')
        if len(args) < 2:
            raise ValueError("Invalid number of arguments. Please provide a file extension and output name ex: /Convert png hasil.")
        
        file_type, output_name = args
        if not is_supported_file_type(file_type):
            raise ValueError(f"Unsupported file type: {file_type}")
        
        file_info = bot.get_file(reply_message.document.file_id)
        file_path = bot.download_file(file_info.file_path)
        source_file = os.path.join(source_dir, reply_message.document.file_name)
        
        with open(source_file, 'wb') as f:
            f.write(file_path)
        
        output_file = convert_file(source_file, file_type, output_name)
        send_converted_file(message, output_file)
        cleanup_files([source_file, output_file])
    except ValueError as ve:
        bot.reply_to(message, str(ve))
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

import os
import subprocess
import socket
import json
import telebot
from ipaddress import ip_address, ip_network

# Fungsi untuk menjalankan subfinder
def run_subfinder(domain, chat_id):
    command = ['./subfinder', '-d', domain, '-o', 'hasil_scan.txt']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode != 0:
        bot.send_message(chat_id, f"Error: {error.decode('utf-8')}")
    else:
        bot.send_message(chat_id, f"Pemindaian selesai untuk domain {domain}. Mengirim hasil pemindaian...")
        send_file('hasil_scan.txt', chat_id)
        bot.send_message(chat_id, "Mengolah hasil pemindaian...")
        process_results('hasil_scan.txt', chat_id)

# Fungsi untuk mendapatkan IP dari host
def host2ip(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None

# Fungsi untuk memeriksa apakah IP berada dalam subnet tertentu
def ip_in_subnet(ip, cidr):
    try:
        return ip_address(ip) in ip_network(cidr)
    except ValueError:
        return False

# Fungsi untuk memeriksa penyedia layanan berdasarkan IP
def detect_provider(ip):
    cloudflare_ips = [
        "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22",
        "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18",
        "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22",
        "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/12",
        "172.64.0.0/13", "131.0.72.0/22"
    ]
    nginx_ips = ["192.0.64.0/13", "199.27.128.0/19", "198.51.100.0/24"]
    apache_ips = ["207.46.236.0/23", "216.58.192.0/19"]
    akamai_ips = ["23.0.0.0/8", "2620:119:35::/40"]
    
    if any(ip_in_subnet(ip, cidr) for cidr in cloudflare_ips):
        return "Cloudflare"
    elif any(ip_in_subnet(ip, cidr) for cidr in nginx_ips):
        return "Nginx"
    elif any(ip_in_subnet(ip, cidr) for cidr in apache_ips):
        return "Apache"
    elif any(ip_in_subnet(ip, cidr) for cidr in akamai_ips):
        return "Akamai"
    else:
        return "Tidak dikenal"

# Fungsi untuk memproses hasil subfinder dan mendapatkan informasi IP
def process_results(file_path, chat_id):
    try:
        with open(file_path, 'r') as file:
            try:
                results = json.load(file)  # Coba baca sebagai JSON
            except json.JSONDecodeError:
                file.seek(0)  # Kembalikan ke awal file
                lines = file.readlines()
                results = [line.strip() for line in lines if line.strip()]  # Baca sebagai plain text

        detailed_results = []
        for domain in results:
            if domain:
                # Mendapatkan IP dari domain
                ip = host2ip(domain)
                if not ip:
                    detailed_results.append({"Domain": domain, "IP": "Tidak ditemukan"})
                    continue
                
                provider = detect_provider(ip)
                detailed_results.append({"Domain": domain, "IP": ip, "Provider": provider})
        
        # Simpan hasil dalam JSON
        output_path = 'output.json'
        with open(output_path, 'w') as output_file:
            json.dump(detailed_results, output_file, indent=4)

        bot.send_message(chat_id, "Hasil analisis selesai. Mengirim hasil analisis...")
        send_file(output_path, chat_id)

    except FileNotFoundError:
        bot.send_message(chat_id, "File hasil pemindaian tidak ditemukan.")
    except Exception as e:
        bot.send_message(chat_id, f"Error saat memproses hasil: {e}")

# Fungsi untuk mengirim file
def send_file(file_path, chat_id):
    try:
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id, file)
    except Exception as e:
        bot.send_message(chat_id, f"Error saat mengirim file: {e}")

# Command handler untuk memulai pemindaian
@bot.message_handler(commands=['Scan'])
def scan_command(message):
    try:
        domain = message.text.split()[1]
        run_subfinder(domain, message.chat.id)
    except IndexError:
        bot.send_message(message.chat.id, "Usage: /Scan {domain}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

# Command handler untuk mengirim tangkapan layar ke Telegram
@bot.message_handler(commands=['SS'])
def screenshot_command(message):
    try:
        os.system('screencapture -u screenshot.png')
        bot.send_message(message.chat.id, "Mengirim tangkapan layar...")
        send_file('screenshot.png', message.chat.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


import telebot
import csv
import os
import time
from datetime import datetime

# Directory to store CSV files
DIR_PATH = 'tulisan'
if not os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)

# Command to handle 'tulisan {tabel} {bahasa} {catatan}'
@bot.message_handler(commands=['Tulis'])
def handle_tulisan(message):
    try:
        # Split the message text to get the components
        parts = message.text.split(' ', 3)
        if len(parts) != 4:
            bot.reply_to(message, "Format pesan salah. Gunakan: /Tulis {tabel} {bahasa} {catatan}")
            return
        
        tabel, bahasa, catatan = parts[1], parts[2], parts[3]
        user_id = message.from_user.id
        
        # Prepare the CSV file path
        file_path = os.path.join(DIR_PATH, f'{user_id}.csv')
        
        # Write to the CSV file
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp, tabel, bahasa, catatan])
        
        bot.reply_to(message, f"Tulisan disimpan pada perintah !{tabel}")
    
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    
    finally:
        bot.reply_to(message, "Operasi 'tulisan' selesai.")

# Command to handle '!{tabel}'
@bot.message_handler(func=lambda message: message.text.startswith('!'))
def handle_retrieve(message):
    try:
        tabel = message.text[1:]
        user_id = message.from_user.id
        
        # Prepare the CSV file path
        file_path = os.path.join(DIR_PATH, f'{user_id}.csv')
        
        if not os.path.exists(file_path):
            bot.reply_to(message, f"Tidak ada tulisan ditemukan untuk tabel '{tabel}'")
            return
        
        # Read the CSV file and filter rows by the specified table
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[1] == tabel]
        
        if not rows:
            bot.reply_to(message, f"Tidak ada tulisan ditemukan untuk perintah !{tabel}")
            return
        
        # Format the output
        response = f"Tulisan pada tabel '{tabel}':\n"
        for row in rows:
            response += f"{row[0]} - {row[2]} - {row[3]}\n"
        
        bot.reply_to(message, response)
    
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    
    finally:
        bot.reply_to(message, f"Operasi pengambilan tulisan untuk perintah !{tabel} selesai.")

# Command to handle '!{tabel}'
@bot.message_handler(func=lambda message: message.text.startswith('! 0'))
def handle_retrieve(message):
    try:
        user_id = message.from_user.id
        
        # Prepare the CSV file path
        file_path = os.path.join(DIR_PATH, f'0.csv')
        
        if not os.path.exists(file_path):
            bot.reply_to(message, f"Tidak ada tulisan ditemukan untuk tabel 0'")
            return
        
        # Read the CSV file and filter rows by the specified table
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[1] == tabel]
        
        if not rows:
            bot.reply_to(message, f"Tidak ada tulisan ditemukan untuk perintah !0")
            return
        
        # Format the output
        response = f"Tulisan pada tabel '0':\n"
        for row in rows:
            response += f"{row[0]} - {row[2]} - {row[3]}\n"
        
        bot.reply_to(message, response)
    
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    
    finally:
        bot.reply_to(message, f"Operasi pengambilan tulisan untuk perintah !0 selesai.")

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='message.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_message(user_id, message):
    """
    Log the message sent to the Telegram bot along with the user_id and timestamp.

    :param user_id: ID of the user sending the message
    :param message: The message content sent by the user
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"User ID: {user_id} | Message: {message} | Timestamp: {timestamp}"
    logging.info(log_entry)
    print(log_entry)
    with open('/root/izmiftah/message.txt', 'a') as log:
        log.write(f"{log_entry}\n")# Optionally print to console for real-time monitoring

def handle_telegram_message(user_id, message):
    """
    Handle incoming messages to the Telegram bot and log them.

    :param user_id: ID of the user sending the message
    :param message: The message content sent by the user
    """
    # Log the incoming message
    log_message(user_id, message)

def default_response(user_id, message):
    """
    Default response for messages that are not commands.

    :param user_id: ID of the user sending the message
    :param message: The message content sent by the user
    """
    response = f"Default response to user {user_id}: {message}"
    log_message(user_id, response)
    print(response)
    with open('/root/izmiftah/message.txt', 'a') as tes:
        tes.write(f"{response}\n")    # You would replace this with sending a response to the user via the bot API

def check_keyword_in_message(message, keyword):
    """
    Check if a keyword is present in the message using the 'in' keyword.

    :param message: The message content
    :param keyword: The keyword to search for
    :return: True if the keyword is found in the message, False otherwise
    """
    return keyword

import os
import csv
import pandas as pd
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from datetime import datetime

MIN_SHARE_COUNT = 10
password_csv = 'tulisan'

hadeh = set()
share_count = {}
terblokir = set()
blokir_aktif = False
os.makedirs(password_csv, exist_ok=True)

def terblokir(hadeh): 
   if blokir_nonaktif:
        blokir_aktif = True
        return user_id
   else:
        print(user_id, "bypass ?")
   global diblok
   diblok = terblokir(user_id)

if terblokir:
   user_id = new_saldo
   new_saldo = user_id 
   blokir_aktif
   
def get_current_password_and_link(user_id):
    try:
        # Load the CSV file
        df = pd.read_csv(os.path.join(DIR_PATH, f'0.csv'))

        # Get the last row (assuming it contains the latest password and link)
        latest_row = df.iloc[-1]

        # Extract the password from the third column and the link from the fourth column
        current_password = latest_row.iloc[1]
        current_link = latest_row.iloc[2]

        return current_password, current_link
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None
        
@bot.message_handler(func=lambda message: message.text.startswith(f'*{passnya}'))
def lock_chat(message): 
    command_parts = message.text.split(' ')
    if len(command_parts) != 2:
        bot.send_message(message.chat.id, "Invalid command format. Use: *password {chat id}")
        return
    chat_id = command_parts[1]
    terblokir(chat_id)
    hadeh.add(chat_id)
    blokir_aktif = True
    bot.send_message(message.chat.id, f"Chat {chat_id} has been locked.")

@bot.message_handler(func=lambda message: message.text.startswith(f'#{passnya}'))
def lock_chat(message):
    global terbuka, blokir_aktif, blokir_nonaktif, terblokir
    
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(message.chat.id, "Invalid command format. Use: #password {chat id}")
        return
    
    chat_id = command_parts[1]
    
    if not blokir_aktif:
        terblokir.discard(chat_id)
        blokir_aktif = False
        blokir_nonaktif = True
        hadeh.remove(new_saldo)
    elif user_manager.is_whitelisted(tokenmu, user_id):
        bot.send_message(message.chat.id, "Chat is already whitelisted.")
        return
    
    hadeh.remove(new_saldo)
    not terblokir(tokenmu)
    global terbuka
    blokir_aktif = False
    bot.send_message(message.chat.id, f"Chat {chat_id} has been locked for access.")

@bot.callback_query_handler(func=lambda call: call.data == "unlock_chat")
def prompt_password(call):
    chat_id = call.message.chat.id
    if chat_id in terblokir:
        bot.send_message(chat_id, "Please enter the password to unlock the chat.")


@bot.message_handler(func=lambda message: message.chat.id in hadeh and terblokir)
def check_password(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Attempt to get current password, link, and user
    result = get_current_password_and_link(user_id)

import telebot
import random

# List kata tambahan untuk memperindah pesan
wordlist = ["artistik", "inovatif", "elegan", "unik", "modern"]

# Fungsi untuk membuat pesan dengan format yang diinginkan
def create_message(objek_desain):
    with open('/root/izmiftah/bahan.txt', 'r') as file:
        bahan_list = file.readlines()

    bahan_list = [bahan.strip() for bahan in bahan_list]  # Strip newlines
    random_bahan = random.choice(bahan_list)
    random_bahan2 = random.choice(random_bahan)  # Pilih random bahan dari bahan_list
    random_word = random.choice(wordlist)  # Pilih random kata dari wordlist
    random_anu = random.choice(objek_desain)
    random_objek = random.choice(bahan_list).split(' ')[1]

      # Pilih random objek desain
    return (f"Desain {objek_desain} yang dibuat dengan memberikan sedikit {random_word} "
            f"dengan berbentuk {random_bahan2} yang dihiasi dengan objek berbentuk {random_anu} "
            "yang dibuat dengan tambahan objek besar dan kecil di sekitarnya.")

# Fungsi untuk menambahkan objek desain ke bahan.txt
def append_to_file(objek_desain):
    with open('/root/izmiftah/bahan.txt', 'a') as file:
        file.write(f"desain {objek_desain}\n")

# Command handler untuk menerima pesan objek desain
@bot.message_handler(func=lambda message: message.text.startswith('/Desain '))
def handle_message(message):
    objek_desain = message.text[len('/Desain '):]
    append_to_file(objek_desain)
    response = create_message(objek_desain)
    bot.reply_to(message, response)

# Fungsi untuk mempertajam bagian tertentu dari foto
def enhance_specific_area(image, coordinates):
    img = Image.open(io.BytesIO(image))
    
    # Meningkatkan kontras gambar secara keseluruhan
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)
    
    # Meningkatkan ketajaman pada area tertentu
    for coord in coordinates:
        left, top, right, bottom = coord
        region = img.crop((left, top, right, bottom))
        region = region.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        img.paste(region, (left, top))
    
    # Simpan hasil ke buffer
    output = io.BytesIO()
    img.save(output, format='PNG')
    output.seek(0)
    
    return output

# Handler untuk menerima foto dari pengguna
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Mendapatkan file ID dan file path
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = bot.download_file(file_info.file_path)
        
        # Contoh koordinat area yang ingin dipertajam
        coordinates = [
            (100, 150, 300, 400),  # Area pertama
            (500, 600, 700, 800)   # Area kedua
        ]
        
        # Mengedit foto
        edited_image = enhance_specific_area(file, coordinates)
        
        # Mengirimkan hasil editan ke pengguna
        bot.send_photo(message.chat.id, edited_image, caption="Foto telah diedit.")

        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        user_id = message.from_user.id
        img_number = len([name for name in os.listdir(image_folder) if f"file_{user_id}_" in name])
        src = get_user_image_path(user_id, img_number)

        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        print(f"File saved as {src}")
        bot.reply_to(message, f"Photo received and saved as {src}. Use /Photo (start-end) (urutan gambar yang di kecualikan) (gif/mp4) to create an animation.")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")


import telebot
import json
import os
import secrets
import asyncio

@bot.message_handler(func=lambda message: message.text.lower().startswith(f"#Aktivasi"))
async def whitelist(message):
    user_id = message.from_user.id
    if user_mgmt.is_blocked(user_id):
        await bot.send_message(user_id, "You are blacklisted and cannot use this bot.")
        return

    token_file = f'token_{user_id}.json'
    if not os.path.exists(token_file):
        await bot.send_message(user_id, "No token found. Please send /start the process again.")
        return

    with open(token_file, 'r') as f:
        data = json.load(f)
        token = data.get('token')

    if token in message.text.split(' ')[1]:
        user_mgmt.whitelist_user(user_id)
        user_mgmt.is_whitelisted(user_id)
        hadeh.remove(user_id)
        if terblokir == False:
                global terbuka
                terbuka = False
        not user_mgmt.is_blocked(user_id)
        user_manager.is_whitelisted(new_saldo, user_id)
        await bot.send_message(user_id, "You have been successfully whitelisted!")
        
    else:
        await bot.send_message(user_id, "Invalid token. Please try again.")

@bot.message_handler(func=lambda message: message.text.lower().startswith('keluar '))
async def block(message):
    user_id = message.from_user.id
    if user_mgmt.is_whitelisted(user_id):
        parts = message.text.split()
        if len(parts) == 2:
            target_id = parts[1]
            user_mgmt.block_user(target_id)
            hadeh.add(user_id)
            await bot.send_message(user_id, f"User {target_id} has been blacklisted.")
        else:
            await bot.send_message(user_id, "Please provide a user ID to block.")
    else:
        await bot.send_message(user_id, "You are not authorized to block users.")

import telebot
import csv
import datetime
import os

def simplify_content(content):
    return True if content else False

@bot.message_handler(func=lambda message: message.text.lower().startswith('/kebaikan '))
def record_moment(message):
    try:
        bot.reply_to(message, (
            "Selamat datang! Gunakan perintah berikut untuk mencatat momen Anda:\n"
            "Format perintah: /kebaikan {catatan} : {baik atau buruk}\n"
            "Contoh: /kebaikan Pergi ke pantai : baik\n"
            "Gunakan perintah 'kebaikan' untuk melihat riwayat momen Anda."
        ))
        # Split the message into content after ':'
        parts = message.text.split(':', 1)
        if len(parts) != 2:
            raise ValueError("Format perintah salah. Harap tulis /kebaikan {catatan} : {baik atau buruk}.")

        note_content = parts[0].replace('/kebaikan', '').strip()
        category = parts[1].strip()

        if not note_content or not category:
            raise ValueError("Format perintah salah. Harap tulis /kebaikan {catatan} : {baik atau buruk}.")

        user_id = message.from_user.id
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Determine if the note is good or bad
        is_good = category.lower() == 'baik'
        file_name = f"{user_id}.csv"
        fieldnames = ['timestamp', 'note', 'category']

        # Ensure the file exists and has the correct header
        if not os.path.exists(file_name):
            with open(file_name, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        # Write the record to the CSV file
        with open(file_name, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'timestamp': timestamp, 'note': note_content, 'category': 'baik' if is_good else 'buruk'})

        bot.reply_to(message, f"Catatan '{note_content}' telah disimpan sebagai {'kebiasaan baik' if is_good else 'kebiasaan buruk'}.")

    except ValueError as ve:
        bot.reply_to(message, str(ve))
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")
        raise

@bot.message_handler(func=lambda message: message.text.lower() == 'kebaikan')
def show_history(message):
    user_id = message.from_user.id
    file_name = f"{user_id}.csv"

    if os.path.exists(file_name):
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            history = [row for row in reader]
        
        if history:
            response = "Riwayat momen Anda:\n"
            for record in history:
                response += f"{record['timestamp']}: {record['note']} - {record['category']}\n"
        else:
            response = "Anda belum memiliki riwayat momen."
    else:
        response = "Anda belum memiliki riwayat momen."

    bot.reply_to(message, response)

def analyze_character(text):
    traits = {
        'marah': ['bos', 'direktur', 'menteri', 'jendral', 'presiden'],
        'baik': ['guru', 'ustad', 'karyawan'],
        'kreatif': ['artis', 'pengusaha'],
        'penurut': ['ajudan', 'anak buah'],
        'tegas': ['pimpinan cabang'],
        'ramah': ['resepsionis', 'public relations'],
        'jujur': ['akuntan', 'penulis'],
        'cerdas': ['ilmuwan', 'dosen'],
        'pemimpin': ['manajer', 'kepala departemen'],
        'berani': ['tentara', 'polisi'],
        'sabaran': ['psikolog', 'konselor'],
        'analitis': ['analis data', 'peneliti'],
        'komunikatif': ['wartawan', 'pembawa acara'],
        'detil': ['arsitek', 'desainer'],
        'fleksibel': ['konsultan', 'freelancer'],
        'tangguh': ['atlet', 'pelatih'],
        'pendiam': ['programmer', 'pustakawan'],
        'percaya diri': ['sales', 'marketer'],
        'disiplin': ['militer', 'polisi'],
        'mandiri': ['entrepreneur', 'petani'],
        'pengertian': ['dokter', 'perawat'],
        'optimis': ['motivator', 'pembicara publik'],
        'logis': ['engineer', 'teknisi'],
        'sosial': ['sosial worker', 'volunteer'],
        'artistik': ['seniman', 'fotografer'],
        # Tambahan 25 traits dan profesi
        'hati-hati': ['auditor', 'kontrol kualitas'],
        'diplomatis': ['diplomat', 'mediator'],
        'praktis': ['mekanik', 'tukang'],
        'kooperatif': ['kerja tim', 'kolaborator'],
        'intuitif': ['psikolog', 'terapis'],
        'ekspresif': ['aktor', 'penyiar'],
        'rendah hati': ['relawan', 'pekerja sosial'],
        'realistis': ['manajer proyek', 'konsultan'],
        'gambaran besar': ['visioner', 'strategi'],
        'lembut': ['penyuluh', 'pelatih'],
        'praktikal': ['tukang', 'insinyur'],
        'introvert': ['pustakawan', 'peneliti'],
        'ekstrovert': ['pemimpin acara', 'penjual'],
        'spontan': ['event organizer', 'aktor'],
        'terencana': ['manajer proyek', 'akuntan'],
        'visioner': ['pemimpin tim', 'inovator'],
        'pemikir': ['filosof', 'penulis'],
        'penengah': ['konselor', 'arbitrator'],
        'peka': ['perawat', 'guru'],
        'mengayomi': ['pembimbing', 'mentor'],
        'berjiwa bebas': ['artis', 'penjelajah'],
        'menyukai aturan': ['polisi', 'militer'],
        'antusias': ['pembicara motivasi', 'pelatih'],
        'bersemangat': ['pengusaha', 'pelatih'],
        'strategis': ['konsultan bisnis', 'manajer strategi']
    }

    counter_traits = {
        'marah': 'sabar',
        'baik': 'tegas',
        'kreatif': 'logis',
        'penurut': 'pemimpin',
        'tegas': 'fleksibel',
        'ramah': 'pendiam',
        'jujur': 'diplomatis',
        'cerdas': 'praktis',
        'pemimpin': 'kooperatif',
        'berani': 'hati-hati',
        'sabaran': 'tegas',
        'analitis': 'intuitif',
        'komunikatif': 'pendiam',
        'detil': 'gambaran besar',
        'fleksibel': 'disiplin',
        'tangguh': 'lembut',
        'pendiam': 'ekspresif',
        'percaya diri': 'rendah hati',
        'disiplin': 'fleksibel',
        'mandiri': 'sosial',
        'pengertian': 'tegas',
        'optimis': 'realistis',
        'logis': 'kreatif',
        'sosial': 'mandiri',
        'artistik': 'logis',
        # Tambahan counter traits
        'hati-hati': 'berani',
        'diplomatis': 'terus terang',
        'praktis': 'visioner',
        'kooperatif': 'mandiri',
        'intuitif': 'analitis',
        'ekspresif': 'pendiam',
        'rendah hati': 'percaya diri',
        'realistis': 'optimis',
        'gambaran besar': 'detil',
        'lembut': 'tegas',
        'praktikal': 'kreatif',
        'introvert': 'ekstrovert',
        'ekstrovert': 'introvert',
        'spontan': 'terencana',
        'terencana': 'spontan',
        'visioner': 'praktis',
        'pemikir': 'praktis',
        'penengah': 'konfrontatif',
        'peka': 'tegas',
        'mengayomi': 'independen',
        'berjiwa bebas': 'terstruktur',
        'menyukai aturan': 'fleksibel',
        'antusias': 'kalem',
        'bersemangat': 'tenang',
        'strategis': 'taktis'
    }

    text = text.lower()
    detected_traits = {trait: any(word in text for word in traits) for trait in traits.keys()}
    career_suggestions = [career for trait, careers in traits.items() if detected_traits[trait] for career in careers]
    partner_traits = [counter_traits[trait] for trait in detected_traits if detected_traits[trait]]
    
    # Identifikasi teman berbahaya
    dangerous_friends = [trait for trait in detected_traits if detected_traits[trait]]
    dangerous_friends += [counter_traits[trait] for trait in detected_traits if detected_traits[trait]]

    return career_suggestions, partner_traits, dangerous_friends

@bot.message_handler(commands=['karier'])
def ask_for_details(message):
    msg = bot.reply_to(message, "Silahkan kirimkan deskripsi tentang dirimu, termasuk sifat, trauma, dan keinginanmu, serta informasi tentang sikap orang terdekatmu di sini.")
    bot.register_next_step_handler(msg, analyze_message)

def analyze_message(message):
    try:
        user_input = message.text
        if not user_input.strip():
            raise ValueError("Input tidak boleh kosong.")
        
        career_suggestions, partner_traits, dangerous_friends = analyze_character(user_input)
        
        if career_suggestions:
            career_response = "Berdasarkan analisis kami, karier yang cocok untuk Anda adalah:\n- " + "\n- ".join(random.sample(career_suggestions, min(len(career_suggestions), 3)))
        else:
            career_response = "Maaf, kami tidak dapat menemukan saran karier berdasarkan input Anda."
        
        if partner_traits:
            partner_response = "Sifat pasangan yang cocok untuk Anda adalah:\n- " + "\n- ".join(random.sample(partner_traits, min(len(partner_traits), 3)))
        else:
            partner_response = "Maaf, kami tidak dapat menemukan saran sifat pasangan berdasarkan input Anda."
        
        if dangerous_friends:
            dangerous_response = "Sifat teman yang perlu diwaspadai:\n- " + "\n- ".join(random.sample(dangerous_friends, min(len(dangerous_friends), 3)))
        else:
            dangerous_response = "Tidak ada sifat teman yang perlu diwaspadai berdasarkan input Anda."
        
        bot.reply_to(message, career_response + "\n\n" + partner_response + "\n\n" + dangerous_response)
    except ValueError as ve:
        bot.reply_to(message, str(ve))
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    finally:
        bot.reply_to(message, "Terima kasih telah menggunakan layanan kami. Semoga informasi ini bermanfaat.")


import telebot
import os
import subprocess
from pathlib import Path
from requests.exceptions import Timeout, ConnectionError

# Directory where VPN files will be stored
SOURCE_DIR = '/etc/systemd/system'
TEMPLATE_FILES = {
    '.py': 'python3',
    '.sh': 'sh',
    '.go': 'go run',
    '.js': 'nodejs'
}

def get_available_port(user_id, offset):
    base_port = 10000 + int(user_id[-3:]) + offset
    port = base_port
    while port <= base_port + 10:
        if not is_port_in_use(port):
            return port
        port += 1
    return base_port

def is_port_in_use(port):
    with os.popen(f"netstat -tuln | grep :{port}") as result:
        return bool(result.read().strip())

@bot.message_handler(commands=['vpn'])
def handle_vpn_command(message):
    try:
        parts = message.text.split()
        if len(parts) < 5:
            bot.reply_to(message, "Format perintah tidak valid. Gunakan /vpn (disable|start|restart|stop) {nama file) (extensi: .py|.sh|.go|.js) {vpn ke-1 atau 1-10}.")
            return

        action = parts[1]
        global filevpn
        filevpn = parts[2]
        extension = parts[3]
        offset = int(parts[4])

        user_id = str(message.from_user.id)
        vpn_file_name, port = generate_vpn_file(user_id, offset, extension)
        if not vpn_file_name:
            bot.reply_to(message, "Gagal membuat file VPN.")
            return

        if action == 'start':
            os.system(f'systemctl daemon-reload')
            os.system(f'systemctl enable {vpn_file_name}')
            os.system(f'systemctl start {vpn_file_name}')
        elif action == 'restart':
            os.system(f'systemctl restart {vpn_file_name}')
        elif action == 'stop':
            os.system(f'systemctl stop {vpn_file_name}')
        elif action == 'disable':
            os.system(f'systemctl disable {vpn_file_name}')
        else:
            bot.reply_to(message, "Aksi tidak dikenal.")
            return

        bot.reply_to(message, f"Service {action}ed successfully on port {port}.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")
    finally:
        pass

def generate_vpn_file(user_id, offset, extension):
    port = get_available_port(user_id, offset)
    if not port:
        return None, None

    vpn_file_name = f"vpn{offset}_{user_id}.service"
    vpn_file_path = os.path.join(SOURCE_DIR, vpn_file_name)
    template_command = TEMPLATE_FILES.get(extension)
    if not template_command:
        return None, None

    with open(vpn_file_path, 'w') as vpn_file:
        global filevpn
        vpn_file.write(f"[Unit]\nDescription=VPN Service {offset} for user {user_id}\n")
        vpn_file.write(f"After=network.target\n\n[Service]\nType=simple\n")
        vpn_file.write(f"WorkingDirectory=/root/izmiftah/\n")
        vpn_file.write(f"ExecStart=/usr/bin/{template_command} {filevpn}\n")
        vpn_file.write(f"Restart=on-failure\n\n[Install]\nWantedBy=multi-user.target\n")
    return vpn_file_name, port
        
  
  
def download_file(file_id, file_name):
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    return file_path

def srt_to_vtt(srt_content):
    try:
        vtt_content = ""
        srt_lines = srt_content.strip().split('\n\n')
        
        index_counter = 0
        for index, line in enumerate(srt_lines):
            # Skip even indexes (timestamps)
            if index % 2 == 0:
                continue
            
            # Extract timecodes from SRT format
            times = srt_lines[index - 1].split(' --> ')
            start_time = times[0].replace(',', '.')
            end_time = times[1].replace(',', '.')
            
            # Increment index counter for VTT format
            index_counter += 1
            
            # Add to VTT format content
            vtt_content += f"{start_time} --> {end_time}\n"
            vtt_content += f"{line}\n\n"
        
        return vtt_content.strip()
    except Exception as e:
        logger.error(f"Error converting SRT to VTT: {e}")
        return None
   
@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        documents = message.document if isinstance(message.document, list) else [message.document]
        for document in documents:
            file_id = document.file_id
            file_name = document.file_name

            # Download the file
            file_path = download_file(file_id, file_name)

            try:
                send_with_retry(bot.send_document, message.chat.id, open(file_path, 'rb'), caption=f"Dokumen {file_name} berhasil diunggah!")
            except (Timeout, ConnectionError) as e:
                # Handle connection error
                send_with_retry(bot.send_message, message.chat.id, f"Terjadi kesalahan saat mengunggah dokumen {file_name}. Silakan coba lagi.")
            except Exception as e:
                # Handle any other exceptions
                send_with_retry(bot.send_message, message.chat.id, f"An error occurred: {str(e)}")
        file_info = bot.get_file(message.document.file_id)
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
        
        # Download the file
        downloaded_file = requests.get(file_url).content
        
        # Determine file extension
        _, file_extension = os.path.splitext(message.document.file_name)
        
        if file_extension.lower() == '.srt':
            # Convert SRT to VTT
            vtt_content = srt_to_vtt(downloaded_file.decode('utf-8'))
            
            if vtt_content:
                # Save the VTT content to temp_subtitle.vtt
                with open('temp_subtitle.vtt', 'w', encoding='utf-8') as f:
                    f.write(vtt_content)
                
                # Respond to user with success message
                bot.reply_to(message, "✅ Subtitle file converted and saved as temp_subtitle.vtt")
            else:
                bot.reply_to(message, "❌ Failed to convert subtitle file")
        else:
            bot.reply_to(message, "❌ Only SRT files are supported for conversion")
    except Exception as e:
        # Handle any exceptions in the main loop
        bot.send_message(message.chat.id, f"An error occurred: {str(e)}")

import telebot
import requests
import random
import time
import csv
from datetime import datetime

# API URL for getting the USD price
API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Configuration for candlestick eligibility for up and down
MIN_CHANGE = 0.1  # Minimum eligibility for candlestick up/down
MAX_CHANGE = 5.0  # Maximum eligibility for candlestick up/down
CSV_FILE = 'trade_save.csv'

class TradingBot:
    def __init__(self, ticker, timeframe, bet_amount):
        self.ticker = ticker
        self.timeframe = int(timeframe)
        self.bet_amount = float(bet_amount)
    
    def get_usd_price(self):
        response = requests.get(API_URL)
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    
    def calculate_new_price(self, usd_price):
        average_usd_price = usd_price / (self.timeframe * 60)
        
        # Betting logic: higher bet increases chance of price drop before rise
        if self.bet_amount > 3.0:
            change = random.uniform(MIN_CHANGE, MAX_CHANGE)
            direction = "down then up"
        else:
            change = random.uniform(MIN_CHANGE, MAX_CHANGE)
            direction = "up then down"
        
        new_price = average_usd_price * (1 + change if direction == "up then down" else 1 - change)
        
        return average_usd_price, change, new_price, direction
    
    def simulate_trading(self):
        usd_price = self.get_usd_price()
        average_usd_price, change, new_price, direction = self.calculate_new_price(usd_price)
        
        return usd_price, average_usd_price, change, new_price, direction
    
    def save_trade(self, usd_price, average_usd_price, change, new_price, direction):
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), self.ticker, self.timeframe, self.bet_amount, usd_price, average_usd_price, change, new_price, direction])

    def load_trades(self):
        trades = []
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                trades.append(row)
        return trades

    def generate_ascii_art(self, direction, change):
        scale = int(change)
        if direction == "up then down":
            art = " " * scale + "/\\\n" + " " * (scale - 1) + "/  \\\n" + " " * (scale - 2) + "/    \\\n"
        else:
            art = " " * (scale - 2) + "\\    /\n" + " " * (scale - 1) + "\\  /\n" + " " * scale + "\\/\n"
        return art

@bot.message_handler(commands=['trading'])
def trading_message(message):
    try:
        _, ticker, timeframe, bet_amount = message.text.split(' ')
        
        bot_trader = TradingBot(ticker, timeframe, bet_amount)
        usd_price, average_usd_price, change, new_price, direction = bot_trader.simulate_trading()
        
        # Save the trade
        bot_trader.save_trade(usd_price, average_usd_price, change, new_price, direction)
        
        # Generate ASCII art for visualization
        ascii_art = bot_trader.generate_ascii_art(direction, change)
        
        bot.reply_to(message, f"Trading simulation for {ticker}\n"
                              f"Current USD price: {usd_price}\n"
                              f"Average USD price in {timeframe} hours: {average_usd_price}\n"
                              f"Bet amount: {bet_amount}\n"
                              f"Price change: {change}\n"
                              f"Price direction: {direction}\n"
                              f"New price: {new_price}\n\n"
                              f"Price change visualization:\n{ascii_art}")
    except Exception as e:
        bot.reply_to(message, "Error processing your command. Please use the format: /trading <saham> <timeframe> <harga saham saat ini>")

def analyze_trades():
    bot_trader = TradingBot("", 0, 0)  # Placeholder initialization
    trades = bot_trader.load_trades()
    # Analysis logic can be added here based on loaded trades
    for trade in trades:
        print(trade)

# Fungsi untuk menghasilkan kalimat dari input user dan file yang di-reply
def generate_promptnya(jenis_prompt, susunan_kata, input_txt, bahasa):
    # Gabungkan susunan kata input dengan kata dari file dan wordlist
    hasil_kata = f"{susunan_kata} {input_txt.strip()}]n\n"
    hasil_prompt = f"Generate {jenis_prompt} with this command:\n{hasil_kata}"
    
    # Tambahkan penjelasan tentang fungsi del
    penjelasan_del = ("\n\nDengan fungsi hasil yang disempurnakan dan dilengkapi sebagaimana mestinya secara sempurna.\n"
                      "```")
    
    hasil_prompt += penjelasan_del
    
    # Jika bahasa bukan bahasa Inggris, tambahkan terjemahan di sini (sederhana)
    if bahasa.lower() != 'english':
        hasil_prompt += f"\n\n(Translate to {bahasa})"
    
    return hasil_prompt

# Fungsi untuk menangani pesan dengan perintah 'AI'
@bot.message_handler(commands=['AI'])
def handle_ai_prompt(message):
    try:
        # Pisahkan perintah dan argumen
        args = message.text.split('>', 3)
        if len(args) < 4:
            bot.reply_to(message, "Format perintah salah. Gunakan: '/AI >(jenis untuk prompt)>(susunan kata)>(bahasa outputnya)'")
            return
        
        jenis_prompt = args[1].strip()
        susunan_kata = args[2].strip()
        bahasa = args[3].strip()

        # Pastikan pesan tersebut merupakan reply ke pesan yang memiliki file .txt
        if not message.reply_to_message or not message.reply_to_message.document:
            bot.reply_to(message, "Silakan reply ke pesan yang memiliki file .txt.")
            return

        # Unduh file .txt
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Baca konten file .txt
        input_txt = downloaded_file.decode('utf-8')

        # Buat prompt
        prompt = generate_promptnya(jenis_prompt, susunan_kata, input_txt, bahasa)
        
        # Kirim hasil prompt ke user
        bot.reply_to(message, prompt)
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")        

# Fungsi untuk menghitung jarak antara dua koordinat menggunakan Haversine formula
def calculate_distance(lat1, lng1, lat2, lng2):
    R = 6371  # Radius bumi dalam kilometer
    dlat = np.radians(lat2 - lat1)
    dlng = np.radians(lng2 - lng1)
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlng/2) * np.sin(dlng/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = R * c
    return distance

# Fungsi untuk menghitung waktu tempuh berdasarkan jarak dan kecepatan
def calculate_travel_time(distance, speed):
    assert speed > 0, "Kecepatan harus lebih besar dari 0."
    travel_time = distance / speed  # Waktu dalam jam
    return travel_time

# Fungsi untuk menentukan arah kompas dan belokan
def get_direction(lat1, lng1, lat2, lng2):
    directions = []
    if lat2 > lat1:
        directions.append("ke arah utara")
    elif lat2 < lat1:
        directions.append("ke arah selatan")
    if lng2 > lng1:
        directions.append("ke arah timur")
    elif lng2 < lng1:
        directions.append("ke arah barat")
    return directions

# Fungsi untuk menangani pesan kesalahan
def handle_error(message, error):
    bot.reply_to(message, f"Error: Terjadi kesalahan: {error}")

# Handler untuk perintah /jarak
@bot.message_handler(commands=['jarak'])
def handle_jarak(message):
    try:
        command_params = message.text.split(' ', 3)
        assert len(command_params) == 4, "Format perintah tidak valid. Gunakan /jarak HH:mm kecepatan lat,lng."
        
        depart_time_str, speed_str, location = command_params[1], command_params[2], command_params[3]
        
        try:
            target_hour, target_minute = map(int, depart_time_str.split(':'))
            depart_time = datetime.now().replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
            if depart_time < datetime.now():
                depart_time += timedelta(days=1)  # Set to next day if the time is in the past
        except ValueError:
            raise ValueError("Jam berangkat tidak valid. Harap masukkan dalam format HH:mm.")
        
        try:
            speed = float(speed_str)  # Kecepatan dalam km/jam
            assert speed > 0, "Kecepatan harus lebih besar dari 0."
        except ValueError:
            raise ValueError("Kecepatan tidak valid. Harap masukkan nilai numerik.")
        
        try:
            lat, lng = map(float, location.split(','))
        except ValueError:
            raise ValueError("Lokasi tidak valid. Harap masukkan dalam format 'lat,lng'.")

        # Memeriksa apakah pesan ini adalah balasan ke pesan lokasi
        if message.reply_to_message and message.reply_to_message.location:
            user_location = message.reply_to_message.location
            lat_user = user_location.latitude
            lng_user = user_location.longitude

            # Menghitung jarak antara dua koordinat
            distance = calculate_distance(lat_user, lng_user, lat, lng)

            # Menghitung waktu tempuh berdasarkan jarak dan kecepatan
            travel_time_hours = calculate_travel_time(distance, speed)
            arrival_time = depart_time + timedelta(hours=travel_time_hours)

            # Mendapatkan arah kompas dan belokan
            directions = get_direction(lat_user, lng_user, lat, lng)
            directions_str = " kemudian ".join(directions)

            bot.reply_to(message, f"Jarak dari lokasi Anda ke tujuan adalah {distance:.2f} km.\n" +
                                  f"Estimasi waktu tempuh: {travel_time_hours:.2f} jam.\n" +
                                  f"Prediksi waktu tiba: {arrival_time.strftime('%H:%M:%S')}.\n" +
                                  f"Arah jalan: {directions_str}.")
        else:
            bot.reply_to(message, "Silakan balas perintah ini ke pesan yang berisi lokasi Anda.")

    except AssertionError as e:
        handle_error(message, e)
    except Exception as e:
        handle_error(message, e)
        
  
import os
import shutil
import zipfile
import subprocess
import requests
import json
import telebot
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Constants
APKTOOL_JAR_PATH = 'apktool.jar'
HTML2APK_JAR_PATH = 'html2apk.jar'
SIGNAPK_JAR_PATH = 'signapk.jar'
KEY_PEM = 'testkey.x509.pem'
KEY_PK8 = 'testkey.pk8'


class APKCreator:
    def __init__(self, source_dir, app_name, app_id):
        self.source_dir = source_dir
        self.app_name = app_name
        self.app_id = app_id
        self.apk_output_dir = os.path.join(source_dir, 'dist')
        os.makedirs(self.apk_output_dir, exist_ok=True)

    def create_apk_with_apktool(self):
        print("Creating APK with APKTool...")
        apk_output_path = os.path.join(self.apk_output_dir, f'{self.app_name}.apk')
        command1 = [
            'apktool', 'd', 'data.apk', '-o', 'project', '-f'
        ]
        command2 = [
            'apktool', 'b', 'project', '-o', apk_output_path
        ]
        subprocess.run(command1, check=True)
        subprocess.run(command2, check=True)
        return apk_output_path

    def create_apk_with_html2apk(self):
        print("Creating APK with HTML2APK...")
        command = ['java', '-jar', HTML2APK_JAR_PATH, '--server.port=8081']
        subprocess.Popen(command, check=True)
        
        url = 'http://localhost:8081/api/create'
        files = {'file': open(os.path.join(self.source_dir, 'downloads/index.html'), 'rb')}
        data = {'app_name': self.app_name, 'app_id': self.app_id}
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        
        apk_url = response.json().get('apk_url')
        apk_output_path = os.path.join(self.apk_output_dir, f'{self.app_name}.apk')
        self.download_file(apk_url, apk_output_path)
        return apk_output_path

    def create_apk_with_html2app(self):
        print("Creating APK with HTML2App...")
        template_dir = os.path.join(self.source_dir, 'extracted', self.app_id)
        if os.path.exists(template_dir):
            shutil.rmtree(template_dir)
        os.makedirs(template_dir, exist_ok=True)

        subprocess.run(['npx', 'gitget', 'https://github.com/yandeu/html2app-template', template_dir], check=True)

        www_dir = os.path.join(template_dir, 'www')
        if os.path.exists(www_dir):
            shutil.rmtree(www_dir)
        shutil.copytree(os.path.join(self.source_dir, 'downloads'), www_dir)

        config = {
            "name": self.app_name,
            "version": "1.0.0",
            "build": 1,
            "id": self.app_id,
            "fullscreen": False,
            "orientation": "default",
            "plugins": [],
            "credentials": {},
            "allowMixedContent": False
        }

        with open(os.path.join(template_dir, 'config.json'), 'w') as config_file:
            json.dump(config, config_file)

        subprocess.run(['zip', '-r', 'app.zip', 'assets', 'www', 'config.json'], cwd=template_dir, check=True)
        subprocess.run(['npm', 'install'], cwd=template_dir, check=True)

        with open(os.path.join(template_dir, 'app.zip'), 'rb') as file:
            files = {'file': file}
            response = requests.post('https://html2app.dev/', files=files)
            response.raise_for_status()

        apk_url = response.json().get('apk_url')
        return apk_url

    def download_filenya(self, url, output_path, retries=3):
        session = requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        response = session.get(url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)

    def sign_apk(self, apk_path):
        print("Signing APK...")
        signed_apk_path = apk_path.replace('.apk', '.signed.apk')
        command = [
            'java', '-jar', SIGNAPK_JAR_PATH, KEY_PEM, KEY_PK8, apk_path, signed_apk_path
        ]
        subprocess.run(command, check=True)
        return signed_apk_path

def extract_zip(file_path, extract_to):
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def clean_up(paths):
    for path in paths:
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
            
  
def running_apk():
    for directory in ['downloads', 'extracted']:
        os.makedirs(directory, exist_ok=True)

@bot.message_handler(commands=['APK'])
def handle_apk_command(message):
    try:
        bot.reply_to(message, "Please ensure the ZIP file contains apktool.yml. Reply to a ZIP file with the command /APK {app_name} {app_id} {tool}.")

        command_parts = message.text.split()
        if len(command_parts) != 4:
            bot.reply_to(message, "Invalid command format. Use: /APK {app_name} {app_id} apktool.")
            return

        app_name, app_id, tool = command_parts[1], command_parts[2], command_parts[3].lower()
        if not message.reply_to_message or not message.reply_to_message.document:
            bot.reply_to(message, "Please reply to a ZIP file with the command /APK.")
            return

        running_apk()
        zip_file_info = message.reply_to_message.document
        file_id = zip_file_info.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_filenya(file_info.file_path)
        
        zip_file_path = os.path.join(zip_file_info.file_name)
        with open(zip_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        extract_dir = os.path.join('downloads')
        extract_path = os.path.join('extracted', app_id)
        extract_zip(zip_file_path, extract_dir)
        extract_zip(zip_file_path, extract_path)

        apk_creator = APKCreator(extract_dir, app_name, app_id)

        if tool == 'apktool':
            apk_output_path = apk_creator.create_apk_with_apktool()
            www_dir = os.path.join('project', 'assets')
            os.makedirs(www_dir, exist_ok=True)
            shutil.copytree(extract_dir, www_dir, dirs_exist_ok=True)        
        elif tool == 'html2apk':
            apk_output_path = apk_creator.create_apk_with_html2apk()
        elif tool == 'html2app':
            apk_url = apk_creator.create_apk_with_html2app()
            bot.reply_to(message, f"HTML2App APK URL: {apk_url}")
            clean_up([zip_file_path, extract_dir])
            return
        else:
            bot.reply_to(message, "Invalid tool specified. Use either 'apktool', 'html2apk', or 'html2app'.")
            return
        
        signed_apk_path = apk_creator.sign_apk(apk_output_path)
        with open(signed_apk_path, 'rb') as apk_file:
            bot.send_document(message.chat.id, apk_file)

        clean_up([zip_file_path, extract_dir, apk_output_path, signed_apk_path])

    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"An error occurred during the APK creation process: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")


import telebot
from googletrans import Translator
from gtts import gTTS
import requests
import numpy as np
from telebot import types
import os

# Fungsi untuk mengonversi teks ke suara dan menyimpan sebagai file menggunakan gTTS
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save('output.ogg')

# Fungsi untuk menerjemahkan teks
def translate_text(text, dest_lang):
    translation = GoogleTranslator(text, dest=dest_lang)
    return translation.text

# Fungsi untuk menangani pesan teks dengan perintah /baca {bahasa}
@bot.message_handler(commands=['baca'])
def handle_message(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "Format salah. Gunakan format '/baca {bahasa}'.")
            return
        
        lang = parts[1]
        original_text = message.reply_to_message.text

        if not original_text:
            bot.reply_to(message, "Balas pesan teks yang ingin Anda ubah menjadi suara.")
            return

        translated_text = translate_text(original_text, lang)
        text_to_speech(translated_text, lang)

        with open('/root/izmiftah/output.ogg', 'rb') as audio:
            bot.send_voice(message.chat.id, audio, reply_to_message_id=message.message_id)

        # Hapus file audio setelah dikirim
        os.remove('output.ogg')
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")


import telebot
from random import choice

# Fungsi untuk membaca warna dari file
def read_colors_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            hex_color, name = line.strip().split()
            yield {"hex": hex_color, "name": name}

# Membaca warna dari colors.txt dan menyimpannya dalam list
colors = list(read_colors_from_file('/root/izmiftah/colors.txt'))

objects = ["bangunan", "mobil", "pakaian", "ruangan", "website", "aplikasi", "perabotan"]
thinkings = ["inovatif", "kreatif", "modern", "minimalis", "futuristik", "klasik", "elegan", "artistik", "unik", "fungsional"]

# Fungsi untuk menghasilkan desain
def generate_design(obj):
    color1 = choice(colors)
    color2 = choice(colors)
    color3 = choice(colors)
    thinking = " ".join(thinkings[3:8])
    
    design = (
        f"Desain {obj} dengan ide-ide {thinking} dan tipikal warna {color1['name']} "
        f"memiliki {obj} bewarna {color2['name']} "
        f"yang berbentuk model {color3['name']} "
        f"dengan tipikal model {color1['name']} "
        f"dengan letak perbedaan pada warna {color2['name']} "
        f"dengan tipikal warna dan bentuk model {color3['name']} secara sempurna."
    )
    
    return design

# Handler untuk perintah /desain
@bot.message_handler(commands=['desain'])
def desain(message):
    try:
        # Ambil objek dari pesan
        obj = message.text.split(' ', 1)[1]
        # Buat desain
        design = generate_design(obj)
        # Kirim desain ke pengguna
        bot.reply_to(message, design)
    except IndexError:
        # Tangani jika format perintah tidak sesuai
        bot.reply_to(message, "Format perintah salah. Gunakan `/desain [objek]`.")

import telebot
import numpy as np
from googletrans import Translator

# Memuat wordlist dari file kreatif.txt
with open('/root/izmiftah/kreatif.txt', 'r') as f:
    additional_wordlist = f.read().splitlines()

# Daftar abjad untuk randomisasi
alphabet = list('abcdefghijklmnopqrstuvwxyz')

# Fungsi untuk menghasilkan huruf dan kalimat acak
def generate_random_kata(wordlist):
    random_letters = ''.join(np.random.choice(alphabet, 10))
    random_sentence = ' '.join(np.random.choice(wordlist, 5))
    return random_letters, random_sentence

# Fungsi untuk menerjemahkan teks menggunakan Google Translate
def translate_kata(text, dest='en'):
    translated = GoogleTranslator(text, dest=dest)
    return translated.text

# Fungsi untuk memproses ide
def process_idenya(input_text, wordlist):
    words = input_text.split()
    processed_idea = ' '.join(np.random.choice(wordlist, len(words)))
    return processed_idea

# Handler untuk perintah 'Ide'
@bot.message_handler(commands=['ide'])
def handle_idenya(message):
    if len(message.text.split(' ', 1)) < 2:
        bot.reply_to(message, "Harap berikan kalimat untuk menghasilkan ide.")
        return

    input_text = message.text.split(' ', 1)[1]
    random_letters, random_sentence = generate_random_kata(additional_wordlist)
    processed_idea = process_idenya(input_text, additional_wordlist)
    translated_idea = translate_kata(processed_idea)
    
    response = (
        f"Random Letters: {random_letters}\n"
        f"Random Sentence: {random_sentence}\n"
        f"Processed Idea: {processed_idea}\n\n\n"
        f"Translated Idea: {translated_idea}"
    )
    bot.reply_to(message, response)

# Handler untuk perintah 'IDE'
@bot.message_handler(commands=['IDE'])
def handle_custom_idenya(message):
    parts = message.text.split(' ', 2)
    if len(parts) < 3:
        bot.reply_to(message, "Harap berikan daftar kata dan kalimat dalam format '/IDE (wordlist1\\wordlist2\\...\\wordlistN) (kalimat) (bahasa)'.")
        return
    
    wordlists_part = parts[1]
    sentence_language_part = parts[2].rsplit(' ', 1)

    if len(sentence_language_part) < 2:
        bot.reply_to(message, "Harap berikan kalimat dan bahasa.")
        return

    input_text = sentence_language_part[0]
    target_language = sentence_language_part[1]
    wordlist_files = wordlists_part.split('\\')
    
    combined_wordlist = additional_wordlist.copy()
    
    for wordlist_file in wordlist_files:
        if wordlist_file.lower() != 'tak terbatas':
            try:
                with open(wordlist_file, 'r') as f:
                    custom_wordlist = f.read().splitlines()
                    combined_wordlist.extend(custom_wordlist)
            except FileNotFoundError:
                bot.reply_to(message, f"File wordlist '{wordlist_file}' tidak ditemukan.")
                return

    processed_idea = process_idenya(input_text, combined_wordlist)
    translated_idea = translate_kata(processed_idea, dest=target_language)
    
    response = (
        f"Custom Processed Idea: {processed_idea}\n\n\n"
        f"Translated Idea: {translated_idea}"
    )
    bot.reply_to(message, response)

import telebot
from PIL import Image, ImageDraw
from fpdf import FPDF
import re

def process_color_info(text):
    hex_codes = re.findall(r'HEX:\s*#([0-9a-fA-F]{6})', text)
    rgb_names = re.findall(r'RGB:\s*([a-zA-Z]+)', text)
    return [(hex_code, rgb_name.lower()) for hex_code, rgb_name in zip(hex_codes, rgb_names)]

def create_color_palette(color_info, image_path):
    width = 100 * len(color_info)
    height = 120  # Menyesuaikan tinggi gambar agar sesuai dengan batas Telegram
    image = Image.new('RGB', (width, height), color=(255, 255, 255))  # Latar belakang putih
    draw = ImageDraw.Draw(image)

    for i, (hex_code, _) in enumerate(color_info):
        draw.rectangle([i*100, 0, (i+1)*100, height], fill=f'#{hex_code}')

    image.save(image_path)

def create_pdf_palette(color_info, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    
    for i, (hex_code, rgb_name) in enumerate(color_info):
        pdf.set_fill_color(int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16))
        pdf.rect(i * 10, 10, 10, 10, 'F')
        pdf.set_font("Arial", size=12)
        pdf.set_xy(i * 10, 20)
        pdf.cell(0, 10, rgb_name, ln=True)

    pdf.output(pdf_path)

@bot.message_handler(commands=['Warna'])
def handle_warna(message):
    text = message.text
    color_info = process_color_info(text)

    if color_info:
        create_color_palette(color_info, 'hex.png')
        create_pdf_palette(color_info, 'hex.pdf')

        with open('/root/izmiftah/hex.png', 'rb') as img:
            bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)

        with open('/root/izmiftah/hex.pdf', 'rb') as pdf:
            bot.send_document(message.chat.id, pdf, reply_to_message_id=message.message_id)
    else:
        bot.reply_to(message, "Tidak ada informasi warna yang ditemukan dalam pesan tersebut.")


import telebot
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from fpdf import FPDF
import re

def process_color_info_v2(text):
    hex_codes = re.findall(r'HEX:\s*#([0-9a-fA-F]{6})', text)
    rgb_names = re.findall(r'RGB:\s*([a-zA-Z]+)', text)
    return [(hex_code, rgb_name.lower()) for hex_code, rgb_name in zip(hex_codes, rgb_names)]

def apply_saturation_filter_v2(image, saturation_factor):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(saturation_factor)

def apply_color_overlay_v2(image, color_hex):
    try:
        overlay_color = Image.new('RGB', image.size, color_hex)
        return Image.blend(image, overlay_color, alpha=0.5)
    except ValueError:
        print("Nilai HEX warna tidak valid:", color_hex)
        return image  # Kembalikan gambar asli jika nilai HEX tidak valid

def apply_anime_filter_v2(image):
    # Implementasi filter anime di sini
    # Misalnya, bisa menggunakan teknik cel shading atau efek lainnya
    # Contoh: image = image.filter(ImageFilter.CONTOUR)
    return image

def create_color_palette_v2(color_info, image_path):
    width = 100 * len(color_info)
    height = 120  # Menyesuaikan tinggi gambar agar sesuai dengan batas Telegram
    image = Image.new('RGB', (width, height), color=(255, 255, 255))  # Latar belakang putih
    draw = ImageDraw.Draw(image)

    for i, (hex_code, _) in enumerate(color_info):
        draw.rectangle([i*100, 0, (i+1)*100, height], fill=f'#{hex_code}')

    image.save(image_path)

def create_pdf_palette_v2(color_info, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    
    for i, (hex_code, rgb_name) in enumerate(color_info):
        pdf.set_fill_color(int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16))
        pdf.rect(i * 10, 10, 10, 10, 'F')
        pdf.set_font("Arial", size=12)
        pdf.set_xy(i * 10, 20)
        pdf.cell(0, 10, rgb_name, ln=True)

    pdf.output(pdf_path)

def resize_image_v2(input_image_path, target_megapixels):
    try:
        image = Image.open(input_image_path)
        width, height = image.size
        current_megapixels = (width * height) / 1e6
        scale_factor = (target_megapixels / current_megapixels) ** 0.5
        new_size = (int(width * scale_factor), int(height * scale_factor))
        resized_image = image.resize(new_size, Image.ANTIALIAS)
        resized_image.save('resized_' + input_image_path)
    except Exception as e:
        print(f"Error resizing image: {e}")

# Fungsi untuk menangani perintah /filter
@bot.message_handler(commands=['filter'])
def handle_warna_v2(message):
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo[-1]  # Menggunakan foto terbaru
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('/root/izmiftah/input_photo.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)

        # Resize foto
        resize_image_v2('input_photo.jpg', 2)

        text = message.text
        color_info = process_color_info_v2(text)

        if color_info:
            create_color_palette_v2(color_info, 'color_palette.png')
            create_pdf_palette_v2(color_info, 'color_palette.pdf')

            input_image = Image.open('resized_input_photo.jpg')

            # Aplikasi filter saturasi
            input_image = apply_saturation_filter_v2(input_image, saturation_factor=1.5)

            # Aplikasi layar warna
            for hex_code, _ in color_info:
                input_image = apply_color_overlay_v2(input_image, hex_code)

            input_image.save('output_photo.jpg')

            with open('/root/izmiftah/color_palette.png', 'rb') as img:
                bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)

            with open('/root/izmiftah/color_palette.pdf', 'rb') as pdf:
                bot.send_document(message.chat.id, pdf, reply_to_message_id=message.message_id)

            with open('/root/izmiftah/output_photo.jpg', 'rb') as img:
                bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        else:
            bot.reply_to(message, "Tidak ada informasi warna yang ditemukan dalam pesan tersebut.")
    else:
        bot.reply_to(message, "Harap balas ke foto untuk menerapkan filter warna.")

import telebot
import cv2
import numpy as np

# Fungsi untuk menghitung jarak warna Euclidean
def euclidean_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))

# Fungsi untuk mencari warna terdekat dari daftar warna yang diberikan
def closest_color(target_color, color_list):
    closest = min(color_list, key=lambda color: euclidean_distance(color, target_color))
    return closest

# Handler untuk perintah /filter
@bot.message_handler(commands=['Filter'])
def handle_color_filter(message):
    if message.reply_to_message and message.reply_to_message.photo:
        # Mendapatkan daftar warna dari pesan
        color_hex_list = message.text.split()[1:]
        
        # Memeriksa apakah daftar warna kosong
        if not color_hex_list:
            bot.reply_to(message, "Daftar warna tidak valid. Harap berikan daftar warna dalam format heksadesimal setelah perintah /filter.")
            return

        # Memeriksa apakah jumlah warna melebihi batas
        if len(color_hex_list) > 100:
            bot.reply_to(message, "Maaf, jumlah warna melebihi batas. Harap berikan maksimal 10 warna dalam daftar.")
            return
        
        # Memeriksa apakah warna yang diberikan valid
        for color_hex in color_hex_list:
            if not is_valid_hex(color_hex):
                bot.reply_to(message, f"Warna {color_hex} tidak valid. Pastikan format warna heksadesimal yang benar.")
                return

        photo = message.reply_to_message.photo[-1]  # Menggunakan foto terbaru
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('/root/izmiftah/input_photo.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)

        img = cv2.imread('input_photo.jpg')
        
        # Konversi daftar warna heksadesimal ke RGB
        color_list = [hex_to_rgb(color_hex) for color_hex in color_hex_list]
        
        # Proses filter warna berdasarkan daftar warna yang diberikan
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                pixel_color = img[y, x][:3]  # Ambil hanya nilai RGB, bukan nilai alpha
                closest_color_val = closest_color(pixel_color, color_list)
                img[y, x][:3] = closest_color_val  # Atur nilai RGB pixel tanpa nilai alpha

        # Simpan gambar yang telah diwarnai
        cv2.imwrite('output_photo.jpg', img)

        with open('/root/izmiftah/output_photo.jpg', 'rb') as img:
            bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    else:
        bot.reply_to(message, "Harap balas ke foto untuk menerapkan filter warna.")

# Fungsi untuk memeriksa apakah format heksadesimal warna valid
def is_valid_hex(hex_str):
    return len(hex_str) == 7 and all(c in '0123456789ABCDEFabcdef' for c in hex_str[1:])

# Fungsi untuk mengonversi warna heksadesimal ke RGB
def hex_to_rgb(hex_str):
    return tuple(int(hex_str[i:i+2], 16) for i in (1, 3, 5))


import telebot
import random
import nltk
from googletrans import Translator
from bs4 import BeautifulSoup
import requests

# Muat NLTK data
nltk.download('punkt')

# Fungsi untuk memuat quotes dari file
def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes]

# Fungsi untuk mengambil kutipan acak
def get_random_quote(quotes):
    return random.choice(quotes)

# Fungsi untuk menerjemahkan teks
def translate_text(text, dest_language):
    translated = GoogleTranslator(text, dest=dest_language)
    return translated.text

# Fungsi untuk mengolah teks menggunakan NLTK
def process_text(text):
    sentences = nltk.sent_tokenize(text)
    return ' '.join(sentences)

# Fungsi untuk scraping kutipan jika diperlukan (contoh saja)
def scrape_quote():
    url = 'http://quotes.toscrape.com/random'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote = soup.find(class_='text').get_text()
    author = soup.find(class_='author').get_text()
    return f"{quote} - {author}"

# Fungsi untuk menghasilkan dan menyimpan quote
def generate_and_save_quote(quotes, dest_language, wordlist):
    random_quote = get_random_quote(quotes)
    processed_quote = process_text(random_quote)
    translated_quote = translate_text(processed_quote, dest_language)
    
    # Acak wordlist dan buat menjadi satu kalimat
    random.shuffle(wordlist)
    wordlist_sentence = ' '.join(wordlist)

    result_quote = wordlist_sentence + " - " + translated_quote

    with open('/root/izmiftah/quotes.txt', 'w', encoding='utf-8') as file:
        file.write(result_quote + "\n")

    return result_quote

# Handler untuk perintah 'quote'
@bot.message_handler(commands=['quote'])
def handle_quote_command(message):
    try:
        # Mengambil parameter dari pesan
        command_params = message.text.split()
        
        # Memastikan jumlah parameter yang cukup
        if len(command_params) < 3:
            bot.reply_to(message, "Error: Perintah tidak lengkap. Format yang benar adalah 'quote {bahasa} {input}'")
            return
        
        language = command_params[1]
        wordlist = command_params[2:8]

        # Muat kutipan dari file
        quotes = load_quotes('/root/izmiftah/database_quote.txt')

        # Hasilkan dan simpan kutipan
        result_quote = generate_and_save_quote(quotes, language, wordlist)
        bot.reply_to(message, result_quote)
        
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
                

import subprocess
import telebot
import os
import zipfile
import requests

# Fungsi untuk menyimpan file PHP di direktori pengguna
def save_php_file(user_id, php_content):
    user_dir = f'{user_id}'
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    with open(f'{user_dir}/index.php', 'wb') as php_file:
        php_file.write(php_content)

# Fungsi untuk menyimpan file ZIP di direktori pengguna
def save_zip_file(user_id, zip_content):
    user_dir = f'{user_id}'
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    with open(f'{user_dir}/{user_id}.zip', 'wb') as zip_file:
        zip_file.write(zip_content)

# Fungsi untuk mengekstrak file ZIP ke direktori pengguna
def unzip_game(user_id):
    user_dir = f'{user_id}'
    with zipfile.ZipFile(f'{user_dir}/{user_id}.zip', 'r') as zip_ref:
        zip_ref.extractall(user_dir)

# Fungsi untuk menjalankan server PHP di dalam virtual host
def run_php_server(user_id):
    port = user_id[-3:]
    user_dir = f'{user_id}'
    subprocess.Popen(['php', '-S', f'0.0.0.0:{port}', '-t', user_dir])

import subprocess

# Fungsi untuk mengirimkan tautan deploy ke bot Telegram
def send_deploy_link(user_id, chat_id):
    # Get the IP address of the device using curl
    ip_address = subprocess.run(['curl', '-s', 'ifconfig.me'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

    port = user_id[-3:]
    link = f'http://{ip_address}:{port}'
    bot.send_message(chat_id, f'Game deployed successfully! Access it at: {link}')
    
# Fungsi untuk menghapus file PHP, ZIP, dan direktori pengguna
def end_game(user_id):
    user_dir = f'{user_id}'
    os.remove(f'{user_dir}/index.php')
    os.remove(f'{user_dir}/{user_id}.zip')
    os.rmdir(user_dir)

# Fungsi untuk menangani perintah 'game'
def handle_game(message):
    user_id = str(message.from_user.id)
    if message.reply_to_message:
        if message.reply_to_message.document:
            if message.reply_to_message.document.mime_type == 'application/x-php':
                # Jika file PHP diunggah, simpan dan deploy game
                file_info = bot.get_file(message.reply_to_message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                save_php_file(user_id, downloaded_file)
                run_php_server(user_id)  # Menjalankan server PHP
                send_deploy_link(user_id, message.chat.id)
            elif message.reply_to_message.document.mime_type == 'application/zip':
                # Jika file ZIP diunggah, simpan, ekstrak, dan deploy game
                file_info = bot.get_file(message.reply_to_message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                save_zip_file(user_id, downloaded_file)
                unzip_game(user_id)
                run_php_server(user_id)  # Menjalankan server PHP
                send_deploy_link(user_id, message.chat.id)
            else:
                bot.reply_to(message, "Invalid file format. Please upload an PHP file or a ZIP file.")
        else:
            bot.reply_to(message, "Please reply to a message containing a file.")
    else:
        bot.reply_to(message, "Please reply to a message containing a file.")

# Fungsi untuk menangani perintah 'endgame'
def handle_end_game(message):
    user_id = str(message.from_user.id)
    end_game(user_id)
    bot.reply_to(message, "Game ended successfully!")

# Command handler untuk memulai game
@bot.message_handler(commands=['game'])
def start_game(message):
    global blokir_aktif, locked_commands, terbuka, saldo_pengguna, new_saldo, jumlah_koin, username
    if blokir_nonaktif:
        try:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
            if blocked_users:
                if is_blokir_active(message):
                    bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                    block_user(username)
            if is_not_blocked_user:
                bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
                bot.send_message(message.chat.id, text=f" silahkan melakukan /topup atau /payment buat isi saldonya sebanyak - banyak nya")
                new_saldo -= 10
                jumlah_koin -= 5
                saldo_pengguna -= 10
                if jumlah_koin > 0 and saldo_pengguna > 0:
                    handle_game(message)
        except Exception as e:
            bot.send_message(message.chat.id, text=str(e))
    else:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")

# Command handler untuk mengakhiri game
@bot.message_handler(commands=['endgame'])
def stop_game(message):
    global blokir_aktif, locked_commands, terbuka, saldo_pengguna, new_saldo, jumlah_koin, username
    if blokir_nonaktif:
        try:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
            if blocked_users:
                if is_blokir_active(message):
                    bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                    block_user(username)
            if is_not_blocked_user:
                bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
                bot.send_message(message.chat.id, text=f" silahkan melakukan /topup atau /payment buat isi saldonya sebanyak - banyak nya")
                new_saldo -= 10
                jumlah_koin -= 5
                saldo_pengguna -= 10
                if jumlah_koin > 0 and saldo_pengguna > 0:
                    handle_end_game(message)
        except Exception as e:
            bot.send_message(message.chat.id, text=str(e))
    else:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")


import telebot
import random
import numpy as np

# Fungsi untuk mendeteksi typo dan memperbaikinya secara acak
def detect_and_correct_typo(text):
    words = text.split()
    corrected_text = ""
    for word in words:
        # Secara acak memutuskan apakah akan mengubah kata atau tidak
        if random.choice([True, False]):
            # Mengganti kata dengan kata yang dipilih secara acak
            corrected_text += np.random.choice(words)
        else:
            corrected_text += word
        corrected_text += " "
    return corrected_text.strip()

# Fungsi untuk memperbaiki dan menyempurnakan teks
def improve_text(text):
    # Lakukan perbaikan atau analisis pada teks di sini
    improved_text = detect_and_correct_typo(text)
    return improved_text

# Fungsi untuk menganalisis dan memperbaiki teks
def analyze_and_correct_text(text):
    # Analisis teks, jika diperlukan
    # Misalnya, menggunakan pustaka Translator untuk menerjemahkan ke bahasa Inggris
    translated_text = GoogleTranslator(text, src='id', dest='en').text

    # Memperbaiki teks yang telah diterjemahkan
    corrected_text = improve_text(translated_text)

    # Jika diperlukan, terjemahkan kembali teks ke bahasa asal
    final_text = GoogleTranslator(corrected_text, src='en', dest='id').text

    return final_text

# Handler untuk pesan yang di-reply dengan perintah /Kode
@bot.message_handler(commands=['Kode'])
def handle_text_message(message):
    # Cek apakah ada pesan yang di-reply
    if message.reply_to_message:
        # Ambil teks dari pesan yang di-reply oleh pengguna
        user_text = message.reply_to_message.text

        # Analisis dan perbaiki teks
        improved_text = analyze_and_correct_text(user_text)

        # Kirim pesan yang telah diperbaiki
        bot.reply_to(message, improved_text)
    else:
        bot.reply_to(message, "Mohon reply pesan yang ingin dianalisis dan diperbaiki dengan perintah /Kode.")

import telebot
import random
import keyword
from googletrans import Translator

# Fungsi untuk mendeteksi typo dan memperbaikinya secara acak
def detect_and_correct_typo(text):
    words = text.split()
    corrected_text = ""
    for word in words:
        # Jika kata adalah keyword, biarkan tetap
        if word.lower() in keyword.kwlist:
            corrected_text += word
        else:
            # Secara acak memutuskan apakah akan mengubah kata atau tidak
            if random.choice([True, False]):
                # Mengganti kata dengan kata yang dipilih secara acak
                corrected_text += random.choice(keyword.kwlist)
            else:
                corrected_text += word
        corrected_text += " "
    return corrected_text.strip()

# Fungsi untuk mendapatkan kata-kata yang salah dalam teks
def get_erroneous_words(text):
    words = text.split()
    erroneous_words = []
    for word in words:
        if word.lower() not in keyword.kwlist:
            if word != detect_and_correct_typo(word):
                erroneous_words.append(word)
    return erroneous_words

# Fungsi untuk menghitung jumlah kata typo dalam pesan telegram
def count_typo(message):
    text = message.text
    return len(get_erroneous_words(text))

# Handler untuk pesan masuk dengan perintah /kode
@bot.message_handler(commands=['kode'])
def handle_message(message):
    text = message.text.split(maxsplit=1)
    if len(text) > 1:
        # Menghitung typo
        typo_count = count_typo(message)
        response = f"Jumlah kata yang perlu di ganti dalam pesan: {typo_count}"
        bot.reply_to(message, response)
        # Mengambil kata-kata yang salah
        erroneous_words = get_erroneous_words(text[1])
        if erroneous_words:
            response = f"Kata-kata yang penting untuk di ganti dalam pesan: {', '.join(erroneous_words)}"
        else:
            response = "Tidak ada kata yang salah dalam pesan."
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Mohon berikan pesan yang ingin dianalisis dengan perintah /kode di depannya.")


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import telebot

# Fungsi untuk posting ke channel
def post_to_channel(message):
    channel_id = '@donmiagayin'
    bot.send_message(channel_id, message)

# Fungsi untuk menghasilkan link untuk memulai bot
def get_start_link():
    base_url = 'https://t.me/izmiftah_bot?start='
    return base_url + 'startlink'

# Fungsi untuk membuat dan mengirimkan sharelink
def create_share_link(post_id):
    base_url = 'https://t.me/share/url'
    post_url = f'https://t.me/{channel_id}/{post_id}'
    params = {'url': post_url}
    response = requests.get(base_url, params=params)
    return response.url

# Fungsi untuk menangani pesan dari channel ke bot
@bot.channel_post_handler(func=lambda message: True)
def handle_channel_post(message):
    post_id = message.message_id
    share_link = create_share_link(post_id)
    bot.reply_to(message, f'Berikut adalah sharelink postingan: {share_link}')



import telebot
import numpy as np
import socket
import requests
from bs4 import BeautifulSoup
import subprocess

class Auto:
    def __init__(self):
        pass

    def connect_vpn(self, message):
        # Mengambil URL VPN dan host VPS dari pesan teks
        message_text = message.text.split()
        if len(message_text) == 3:
            vpn_url = message_text[1]
            vps_host = message_text[2]
        else:
            bot.reply_to(message, "Format pesan salah. Gunakan perintah /host [URL VPN] [VPS Host]")
            return
        
        # Memeriksa host VPS sebelum melakukan koneksi
        if check_host_status(vps_host):
            chat_id = message.chat.id
            bot.send_message(chat_id, "VPS host is up. Connecting to VPN...")
            
            # Implementasi koneksi VPN, misalnya menggunakan OpenVPN, SSH tunneling, atau metode lainnya
            vpn_connected = connect_to_vpn(vpn_url, vps_host)
            
            if vpn_connected:
                # Mendapatkan kecepatan jaringan setelah terkoneksi ke VPN
                speed = get_network_speed()
                bot.send_message(chat_id, f"VPN connected successfully!\nNetwork Speed: {speed} Mbps")
            else:
                bot.send_message(chat_id, "Failed to connect to VPN.")
        else:
            bot.reply_to(message, "Failed to connect to VPN. VPS host is down.")

def connect_to_vpn(vpn_url, vps_host):
    # Fungsi untuk melakukan koneksi ke VPN
    # Contoh implementasi sederhana, ganti dengan metode koneksi sesuai kebutuhan
    
    # Implementasi koneksi VPN
    # ...

    # Mengembalikan status koneksi VPN
    return True  # Ganti dengan logika koneksi sesuai implementasi

def check_host_status(host):
    # Fungsi untuk melakukan pengecekan host yang mati atau hidup
    try:
        socket.create_connection((host, 80), timeout=2)
        return True
    except OSError:
        return False

def get_network_speed():
    # Fungsi untuk mendapatkan kecepatan jaringan
    speed = np.random.uniform(5, 50)  # Contoh penggunaan numpy untuk mendapatkan kecepatan acak
    return round(speed, 2)

auto = Auto()

# Mendefinisikan command 'vpn'
@bot.message_handler(commands=['host'])
def connect_vpn_handler(message):
    auto.connect_vpn(message)

@bot.message_handler(commands=['curl'])
def handle_curl(message):
    # Mengambil URL VPN dari pesan teks
    message_text = message.text.split()
    if len(message_text) != 2:
        bot.reply_to(message, "Format pesan salah. Gunakan perintah /curl [URL VPN]")
        return

    vpn_url = message_text[1]
    
    # Membaca daftar proxy dari file proxy.txt
    with open("proxy.txt", "r") as proxy_file:
        proxies = proxy_file.readlines()
        if not proxies:
            bot.reply_to(message, "Tidak ada proxy yang tersedia.")
            return

        # Memilih satu proxy secara acak
        random_proxy = random.choice(proxies).strip()
        
        # Menggunakan proxy yang dipilih untuk mengakses URL VPN
        response = requests.get(vpn_url)
        if response.status_code == 200:
            # Jika berhasil, cetak respons
            print(response.text)
            bot.reply_to(message, "Berhasil mengakses URL VPN melalui proxy.")
        else:
            bot.reply_to(message, "Gagal mengakses URL VPN melalui proxy.")

   # Menggunakan nslookup untuk mendapatkan host dari VPN tunneling
    vpn_host = subprocess.check_output(["curl", vpn_url, "-x", random_proxy]).decode().strip()

    
    # Mengirimkan hasil output ke chat Telegram
    chat_id = message.chat.id
    output_message = (
        f"Host VPN Tunneling: {vpn_host}\n"
        "Scanning selesai!"
    )
    bot.send_message(chat_id, output_message)

    # Membuat laporan bahwa scanning telah selesai
    create_report(vpn_host, chat_id)

def scraper_vpn_tunneling(url):
    # Fungsi untuk melakukan scraping menggunakan requests
    response = requests.get(url)
    if response.status_code == 200:
        # Proses scraping menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Lakukan scraping terhadap elemen yang diinginkan
        # ...
        return soup  # Mengembalikan objek BeautifulSoup
    else:
        print("Failed to fetch URL")

def create_report(vpn_host, chat_id):
    # Fungsi untuk membuat laporan bahwa scanning telah selesai
    output_message = (
        f"Host VPN Tunneling: {vpn_host}\n"
        "Scanning selesai!"
    )
    bot.send_message(chat_id, output_message)

import telebot
import random
import time

wordlist = ["lakukan pemanasan terlebih dahulu", "Siapkan diri!", "Jangan sampai ada yang kelupaan..", "lakukan sekarang juga!", "Harap perhatikan keselamatan diri", "jangan lupa istirahat yang cukup ya!"]

def generate_timer():
    hour = random.randint(1, 3)
    minute = random.randint(0, 30)
    second = random.randint(0, 60)
    return hour, minute, second

@bot.message_handler(commands=['Jadwal'])
def schedule_task(message):
    try:
        tasks = message.text.split()[1:]
        for task in tasks:
            task = task.replace(",", " ")
            hour, minute, second = generate_timer()
            timer = f"{hour} jam {minute} menit {second} detik"
            selected_task = random.choice(wordlist)
            bot.send_message(message.chat.id, f"Tugas: {task}\nWaktu: {timer}\n{selected_task}")
            time.sleep(1)  # Delay 1 second to avoid flooding
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

import telebot
import random
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Load kata-kata kunci dari file katakunci.txt
def load_keywords():
    with open('/root/izmiftah/katakunci.txt', 'r') as file:
        return [line.strip() for line in file]

# Load kata-kata bumbu manis dari internet
def load_sweet_words():
    # Implementasi load kata-kata bumbu manis dari internet
    # Misalnya, menggunakan requests untuk mengambil kata-kata dari sebuah website
    response = requests.get('http://example.com/sweet_words')
    soup = BeautifulSoup(response.text, 'html.parser')
    return [word.text for word in soup.find_all('span', class_='sweet-word')]

# Load list kata-kata kunci dan bumbu manis
wordlist = load_keywords()
sweet_words = load_sweet_words()

def embellish_text(text):
    # Memisahkan kata-kata dalam teks
    words = text.split()
    embellished_words = []

    for word in words:
        # Memilih random jumlah kata bumbu manis untuk dicampur
        num_sweet_words = min(random.randint(1, 3), len(sweet_words))
        # Memilih random kata-kata bumbu manis jika tersedia
        if sweet_words:
            selected_sweet_words = random.sample(sweet_words, num_sweet_words)
        else:
            selected_sweet_words = [''] * num_sweet_words
        # Menggabungkan kata-kata kunci, bumbu manis, dan random susunan huruf
        embellished_word_parts = []
        if wordlist:
            embellished_word_parts.append(random.choice(wordlist))
        if selected_sweet_words:
            embellished_word_parts.append(random.choice(selected_sweet_words))
        embellished_word_parts.extend([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(len(word))])
        embellished_word = ''.join(embellished_word_parts)
        embellished_words.append(embellished_word)

    # Menggabungkan kembali kata-kata menjadi kalimat baru
    embellished_text = ' '.join(embellished_words)
    return embellished_text

# Fungsi untuk menanggapi pesan dengan perintah 'judul'
@bot.message_handler(commands=['nama'])
def handle_judul(message):
    # Memeriksa apakah pesan memiliki cukup argumen
    if len(message.text.split()) > 1:
        # Mengambil teks pesan setelah perintah '/judul '
        text = message.text.split(' ', 1)[1]
        # Memperindah teks pesan
        embellished_text = embellish_text(text)
        # Mengirim pesan kembali ke pengirim
        bot.send_message(message.chat.id, embellished_text)
    else:
        # Mengirim pesan balasan jika perintah tidak memiliki argumen cukup
        bot.send_message(message.chat.id, "Perintah '/nama' memerlukan teks setelahnya.")

import random
import numpy as np
import pandas as pd
import telebot
from bs4 import BeautifulSoup

# Load kegiatan.txt
with open('/root/izmiftah/kegiatan.txt', 'r') as file:
    kegiatan_list = file.readlines()
    kegiatan_list = [kegiatan.strip() for kegiatan in kegiatan_list]

# Buat list untuk menyimpan timer per jam
timers_per_jam = [60] * 12  # Setiap jam memiliki 60 menit

# Simpan timers_per_jam ke file timer.txt
with open('/root/izmiftah/timer.txt', 'w') as file:
    for timer in timers_per_jam:
        file.write(str(timer) + '\n')

# Load timer.txt
with open('/root/izmiftah/timer.txt', 'r') as file:
    timer_list = file.readlines()
    timer_list = [int(timer.strip()) for timer in timer_list]

# Fungsi untuk menambahkan kegiatan ke kegiatan.txt
def tambah_kegiatan(kegiatan):
    with open('/root/izmiftah/kegiatan.txt', 'a') as file:
        file.write(kegiatan + '\n')

# Fungsi untuk menghasilkan kegiatan secara berurutan
def generate_kegiatan(jumlah_kegiatan):
    generated_kegiatan = []
    for _ in range(jumlah_kegiatan):
        jam = random.randint(1, 12)
        waktu = random.choice(timer_list)
        kegiatan = random.choice(kegiatan_list)
        generated_kegiatan.append({'Jam': jam, 'Waktu': waktu, 'Kegiatan': kegiatan})
    return generated_kegiatan

# Membuat dataframe dari kegiatan tambahan
additional_kegiatan = generate_kegiatan(random.randint(2, 4))  # Menghasilkan 2-4 kegiatan tambahan
df_additional = pd.DataFrame(additional_kegiatan)

# Memproses input pengguna sebagai message.text
input_kegiatan = 'tidur makan pulang kerja'
kegiatan_baru = input_kegiatan.split(' ')
for kegiatan in kegiatan_baru:
    tambah_kegiatan(kegiatan.strip())

# Menggabungkan kegiatan tambahan dengan kegiatan dari input pengguna
kegiatan_list.extend(kegiatan_baru)

# Membuat dataframe dari kegiatan yang telah diperbarui
df = pd.DataFrame(generate_kegiatan(24))  # Menghasilkan 10 kegiatan total, termasuk kegiatan tambahan

# Mendefinisikan perintah 'jadwal' pada bot Telegram
@bot.message_handler(commands=['jadwal'])
def send_jadwal(message):
    # Memproses input pengguna sebagai message.text
    input_kegiatan = message.text.replace('/jadwal', '').strip()
    kegiatan_baru = input_kegiatan.split(', ')
    for kegiatan in kegiatan_baru:
        tambah_kegiatan(kegiatan.strip())

    # Menggabungkan kegiatan tambahan dengan kegiatan dari input pengguna
    kegiatan_list.extend(kegiatan_baru)

    # Membuat dataframe dari kegiatan yang telah diperbarui
    df = pd.DataFrame(generate_kegiatan(10))  # Menghasilkan 10 kegiatan total, termasuk kegiatan tambahan

    response = "Jadwal Kegiatan Anda:\n"
    for index, row in df.iterrows():
        response += f"Jam {row['Jam']}:00 - {row['Jam'] + 1}:00 -> {row['Kegiatan']} ({row['Waktu']} menit)\n"
    bot.reply_to(message, response)

import telebot
import random
import nltk


# Daftar kata-kata untuk setiap kategori
wordlists = {
    "action": ["memperkenalkan", "mendemonstrasikan", "memahami", "membahas", "menyajikan"],
    "technique": ["konsep", "teknik", "cara", "metode", "pendekatan"],
    "learning": ["belajar", "pembelajaran", "pemahaman", "pengetahuan", "keterampilan", "konseptualitas", "pemahaman"],
    "learning_type": ["explained", "tutorial", "demonstrasi", "praktek", "latihan", "dasar-dasar"],
    "subject": ["teori", "praktik", "implementasi", "penerapan", "penggunaan", "dasar-dasar", "tehnik dan konsep", "tehnik dan fundamental", "tehnik-dasar"]
}

# Fungsi untuk menghasilkan teks acak berdasarkan topik
def generate_random_text(topic):
    words = nltk.word_tokenize(topic)
    random.shuffle(words)
    return ' '.join(words)

# Fungsi untuk menghasilkan kurikulum pembelajaran
def generate_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    action = random.choice(wordlists["action"])
    technique = random.choice(wordlists["technique"])
    learning = random.choice(wordlists["learning"])
    learning_type = random.choice(wordlists["learning_type"])
    subject = random.choice(wordlists["subject"])
    time_needed = random.randint(1, 12)
    converted_text = generate_random_text(topic)

    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Untuk mempelajari kurikulum ini, kamu perlu menghabiskan waktu {time_needed} jam.\n\n"
                  f"Kurikulum yang perlu kamu pelajari:\n"
                  f"Belajarlah tentang {action} {technique} {topic} yang mengandung {learning} tentang {subject} {topic} dengan metode {learning_type} "
                  f"dari {topic}.\n\n")
    return curriculum

# Fungsi untuk membaca link video dari database.txt
def get_video_link():
    try:
        with open('/root/izmiftah/database1.txt', 'r') as file:
            links = file.readlines()
            return random.choice(links).strip()
    except FileNotFoundError:
        return "https://youtube.com/q="

# Fungsi untuk menghasilkan kurikulum pembelajaran dengan link video
def generate_video_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    learning_type = random.choice(wordlists["learning_type"])
    technique = random.choice(wordlists["technique"])
    action = random.choice(wordlists["action"])
    
    video_link = get_video_link()
    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Dasar-dasar {topic} dengan metode {learning_type} mengenai {topic}.\n\n"
                  f"Selengkapnya bisa belajar di video berikut: https://{video_link}how+to+{learning_type}+dari+{topic}?")
    return curriculum

# Handler untuk perintah /belajar
@bot.message_handler(commands=['belajar'])
def belajar(message):
    try:
        # Ambil topik dari pesan
        topic = message.text.split(' ', 1)[1]
        # Buat kurikulum
        curriculum = generate_curriculum(topic)
        # Kirim kurikulum ke pengguna
        bot.reply_to(message, curriculum)
    except IndexError:
        # Tangani jika format perintah tidak sesuai
        bot.reply_to(message, "Format perintah salah. Gunakan `/belajar [topik]`.")

# Handler untuk perintah /Belajar
@bot.message_handler(commands=['Belajar'])
def Belajar(message):
    try:
        # Ambil topik dari pesan
        topic = message.text.split(' ', 1)[1]
        # Buat kurikulum dengan video link
        curriculum = generate_video_curriculum(topic)
        # Kirim kurikulum ke pengguna
        bot.reply_to(message, curriculum)
    except IndexError:
        # Tangani jika format perintah tidak sesuai
        bot.reply_to(message, "Format perintah salah. Gunakan `Belajar [topik]`.")



import telebot
import nltk
from googletrans import Translator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

@bot.message_handler(commands=['Artikan'])
def summarize_command(message):
    if message.reply_to_message:
        replied_message = message.reply_to_message
        text_to_summarize = replied_message.text
        summary = generate_summary(text_to_summarize)
        bot.reply_to(message, summary)
    else:
        bot.reply_to(message, "Balas pesan yang ingin Anda artikan dengan perintah /Artikan.")

@bot.message_handler(commands=['Acak'])
def handle_document(message):
    bot.reply_to(message, "Silakan kirim file simpulkan.txt untuk di simpulkan.")
    bot.register_next_step_handler(message, process_summary_file)

def process_summary_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("simpulkan.txt", 'wb') as new_file:
            new_file.write(downloaded_file)
        text_to_summarize = read_txt_file("simpulkan.txt")
        summary = generate_summary(text_to_summarize)
        send_summary_as_txt(message.chat.id, summary)
    else:
        bot.reply_to(message, "Mohon kirim file simpulkan.txt yang benar.")

def read_txt_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def generate_summary(text_to_summarize):
    words = word_tokenize(text_to_summarize)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    filtered_text = " ".join(filtered_words)
    translated_text = GoogleTranslator(filtered_text, dest='id').text
    summary = "Ini adalah kesimpulan dari teks yang telah diolah: " + translated_text
    return summary

def send_summary_as_txt(chat_id, summary):
    with open("kesimpulan.txt", "w", encoding="utf-8") as file:
        file.write(summary)
    bot.send_document(chat_id, open("kesimpulan.txt", "rb"))

import telebot
from googletrans import Translator
import nltk
import random
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Fungsi untuk menerjemahkan pesan ke bahasa yang ditentukan
def translate_message(message, dest_lang):
    try:
        translated_message = GoogleTranslator(source='auto', target=dest_lang).translate(message)
        return translated_message
    except ValueError as e:
        return f"Terjadi kesalahan: {e}. Pastikan Anda menggunakan kode bahasa yang valid. Gunakan perintah /help untuk panduan."

# Fungsi untuk mengacak kata-kata penting dalam kalimat
def shuffle_important_words(sentence):
    words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
    important_tags = ['NN', 'VB', 'JJ']  # Noun, Verb, Adjective
    important_words = [word for word, tag in tagged_words if tag in important_tags]
    random.shuffle(important_words)
    shuffled_sentence = ' '.join(important_words)
    return shuffled_sentence

# Fungsi untuk mengubah pesan menjadi satu baris atau maksimal 7 kalimat
def condense_message(message):
    sentences = nltk.sent_tokenize(message)
    condensed_message = ' '.join(sentences[:7])  # Ambil maksimal 7 kalimat
    return condensed_message

# Fungsi untuk membuat kesimpulan dari pesan
def generate_summary(message):
    # Proses pesan
    processed_message = preprocess_message(message)
    
    # Seleksi dan acak kalimat
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', processed_message)
    selected_sentence = random.choice(sentences)  # Pilih satu kalimat secara acak
    
    # Mengambil hanya satu kalimat dari hasil seleksi
    summary = selected_sentence
    
    return summary

# Fungsi untuk memproses pesan sebelum analisis
def preprocess_message(message):
    # Lakukan pembersihan pesan di sini, seperti menghapus tanda baca, karakter khusus, dll.
    processed_message = message
    return processed_message

# Fungsi untuk menyimpan kesimpulan ke dalam file
def save_summary_to_file(summary):
    with open('/root/izmiftah/kesimpulan.txt', 'w') as file:
        file.write(summary)

# Fungsi untuk mengirim pesan kesimpulan ke Telegram
def send_summary_to_telegram(summary, chat_id):
    bot.send_message(chat_id, summary)

@bot.message_handler(commands=['terjemahkan'])
def translate_command(message):
    global blokir_aktif, locked_commands, terbuka
    instructions = "Halo! Saya adalah bot pengolah pesan multibahasa. Gunakan perintah /terjemahkan [kode_bahasa] untuk menerjemahkan pesan yang di-reply oleh pengguna. Contoh: /terjemahkan en untuk terjemahan bahasa Inggris. Gunakan /acak untuk melihat kesimpulan pesan yang di-reply oleh pengguna."
    bot.reply_to(message, instructions)
    # Mendapatkan kode bahasa dari pesan pengguna
    dest_lang = message.text.split()[1]
    # Mendapatkan pesan yang akan diterjemahkan
    replied_message = message.reply_to_message
    if replied_message:
        text_to_translate = replied_message.text
        # Menerjemahkan pesan
        translated_text = translate_message(text_to_translate, dest_lang)
        # Mengirim pesan yang diterjemahkan ke Telegram
        bot.reply_to(message, translated_text)
    else:
        bot.reply_to(message, "Mohon balas ke pesan yang ingin Anda terjemahkan dengan perintah /terjemahkan [kode_bahasa].")

@bot.message_handler(commands=['artikan'])
def translate_all_command(message):
    global blokir_aktif, locked_commands, terbuka
    instructions = "Halo! Saya adalah bot pengolah pesan multibahasa. Gunakan perintah /terjemahkan [kode_bahasa] untuk menerjemahkan pesan yang di-reply oleh pengguna. Contoh: /terjemahkan en untuk terjemahan bahasa Inggris. Gunakan /acak untuk melihat kesimpulan pesan yang di-reply oleh pengguna."
    bot.reply_to(message, instructions)
    # Mendapatkan kode bahasa dari pesan pengguna
    dest_lang = message.text.split()[1]
    # Mendapatkan pesan yang akan diterjemahkan
    replied_message = message.reply_to_message
    if replied_message:
        # Jika pesan adalah teks
        if replied_message.text:
            text_to_translate = replied_message.text
            # Menerjemahkan pesan
            translated_text = translate_message(text_to_translate, dest_lang)
            # Mengirim pesan yang diterjemahkan ke Telegram
            bot.reply_to(message, translated_text)
        # Jika pesan adalah media (foto, video, dll.)
        elif replied_message.caption:
            text_to_translate = replied_message.caption
            # Menerjemahkan pesan
            translated_text = translate_message(text_to_translate, dest_lang)
            # Mengirim pesan yang diterjemahkan ke Telegram
            bot.reply_to(message, translated_text)
        else:
            bot.reply_to(message, "Mohon balas ke pesan teks atau media dengan perintah /artikan [kode_bahasa].")
    else:
        bot.reply_to(message, "Mohon balas ke pesan yang ingin Anda terjemahkan dengan perintah /artikan [kode_bahasa].")


import telebot
import requests
import random
from bs4 import BeautifulSoup

# Fungsi untuk menghasilkan link pencarian Google dari link webmaster
def generate_google_search_link(link, query):
    return f"https://{link.strip()}/search?q={query}/"

@bot.message_handler(commands=['video'])
def generate_video_link(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:         
        # Mengecek apakah pesan pengguna memiliki format yang benar
        if len(message.text.split(' ')) < 2:
            bot.send_message(message.chat.id, "Format pesan tidak sesuai. Gunakan format /video <query>")
            return

        # Membaca database.txt untuk link webmaster
        with open('/root/izmiftah/database.txt', 'r') as file:
            webmaster_links = file.readlines()

        # Membaca wordlist.txt dan wordlist2.txt
        with open('/root/izmiftah/wordlist.txt', 'r') as file:
            wordlist = file.readlines()
        with open('/root/izmiftah/wordlist2.txt', 'r') as file:
            wordlist2 = file.readlines()

        # Mengekstrak query dari pesan pengguna
        query_input = " ".join(message.text.split(' ')[1:])

        # Memilih secara acak kata kunci dari wordlist.txt dan wordlist2.txt
        keyword = random.choice(wordlist).strip()
        keyword2 = random.choice(wordlist2).strip()

        # Membuat query sesuai dengan format yang diminta
        query = f'{keyword}+{query_input}+of+{keyword2}+tutorial'

        # Membangun URL pencarian Google
        google_search_url = f"https://www.google.com/search?q={query}"

        # Melakukan permintaan HTTP
        response = requests.get(google_search_url)

        # Mengekstrak link dari hasil pencarian Google
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')
            video_links = [link['href'] for link in search_results if '/watch?v=' in link['href']]
            if video_links:
                video_link = video_links[0]  # Mengambil link video pertama dari hasil pencarian
                bot.send_message(message.chat.id, f"Ini adalah link video yang Anda cari: {video_link}")
            else:
                bot.send_message(message.chat.id, "Maaf, tidak dapat menemukan video yang sesuai dengan pencarian Anda.")
        else:
            bot.send_message(message.chat.id, "Maaf, terjadi kesalahan saat melakukan pencarian.")

    else:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")
    

    # Melakukan pencarian menggunakan link pencarian Google tanpa proxy
    search_results = []
    for link in webmaster_links:
        full_link = generate_google_search_link(link, query_input)  # Menggunakan link saat ini dari loop
        try:
            with urllib.request.urlopen(full_link) as response:
                # Jika respons berhasil, tambahkan hasil pencarian ke daftar search_results
                search_results.append(full_link)
        except Exception as e:
            print(f"Failed to retrieve results for {full_link}: {e}")

    # Simpan hasil pencarian ke dalam save_output.txt
    with open('/root/izmiftah/save_output.txt', 'w') as file:
        for result in search_results:
            file.write(result + '\n')

    # Tambahkan input ke database_input.txt untuk penggunaan di masa mendatang
    with open('/root/izmiftah/database_input.txt', 'a') as file:
        file.write(query_input + '\n')

    # Kirim pesan ke pengguna bahwa pencarian telah selesai
    bot.send_message(message.chat.id, "Pencarian telah selesai. Hasilnya telah disimpan.")

    # Kirim pesan kembali ke pengguna dengan link pencarian
    bot.send_message(message.chat.id, f"Link hasil pencarian: {', '.join(search_results)}")

    # Tambahkan query ke history link dengan quotes
    history_entry = f'"{query_input}" yang lain juga mencari ini: {", ".join(search_results)}'
    with open('/root/izmiftah/history_link.txt', 'a') as file:
        file.write(history_entry + '\n')

    # Fungsi raise untuk memberikan informasi jika terjadi kesalahan
    def raise_exception(exception_type, message):
        raise exception_type(message)	

import requests
import telebot

# Fungsi untuk mencari tutorial YouTube
def search_youtube_tutorial(query):
    return f'https://www.youtube.com/results?search_query=how+to+create+{query}+tutorial/'

# Fungsi untuk mencari referensi di GitHub
def search_github_reference(query):
    return f'https://github.com/search?q={query}&type=repositories/'

# Fungsi untuk mencari dependencies di Google
def search_google_dependencies(query, wordlist):
    words = '+'.join(wordlist)
    return f'https://www.google.com/search?q=github+%3E+{query}%3E.dll+{words}/'

# Fungsi untuk menghasilkan variasi jenis skrip
def generate_script(ideas, wordlist):
    scripts = []
    for idea in ideas:
        script = f"#{idea.capitalize()} Script\n"
        script += "import requests\nimport numpy\nimport pandas as pd\nimport bs4\n\n"
        script += "# Fungsi menggunakan pip telebot jika untuk telegram bot\n"
        script += "def some_function(text):\n"
        script += "\ttry:\n"
        script += "\t\t# Lakukan sesuatu\n"
        script += "\t\treturn text.strip()\n"
        script += "\texcept Exception as e:\n"
        script += "\t\t# Tangani exception\n"
        script += "\t\treturn\n"
        script += "\tfinally:\n"
        script += "\t\t# Lakukan sesuatu\n"
        script += "\t\treturn\n\n"
        script += "# Fungsi lainnya\n"
        script += "# Anda bisa menambahkan fungsi lain sesuai kebutuhan\n"
        script += f"# Referensi YouTube: {search_youtube_tutorial(idea)}\n"
        script += f"# Referensi GitHub: {search_github_reference(idea)}\n"
        
        # Dependencies
        script += "# Dependencies:\n"
        script += f"{search_google_dependencies(idea, wordlist)}\n\n"
        
        # Contoh-contoh skrip
        script += "# Contoh-contoh skrip:\n"
        script += "# Contoh PHP:\n"
        script += "<?php\necho 'Hello, World!';\n?>\n\n"
        script += "# Contoh Python:\n"
        script += "print('Hello, World!')\n\n"
        script += "# Contoh HTML:\n"
        script += "<!-- Contoh HTML -->\n"
        script += "<html>\n<head>\n<title>Hello</title>\n</head>\n<body>\n<h1>Hello, World!</h1>\n</body>\n</html>\n\n"
        script += "// Contoh JavaScript\n"
        script += "console.log('Hello, World!');\n\n"
        script += "/* Contoh CSS */\n"
        script += "body {\n"
        script += "  color: blue;\n"
        script += "}\n\n"
        
        scripts.append(script)
    return scripts

@bot.message_handler(commands=['koding'])
def new_script(message):
    global blokir_aktif, locked_commands, terbuka
    # Periksa apakah pesan memiliki kata-kata setelah perintah
    if len(message.text.split()) <= 1:
        bot.send_message(message.chat.id, "Usage: /koding <ideas>")
        return
    
    # Kata-kata kunci yang digunakan untuk mencari dependencies
    with open('/root/izmiftah/bahan.txt', 'r') as file:
        wordlist = file.readlines()
        wordlist = [word.strip() for word in wordlist]
    
    # Ide-ide untuk membuat skrip
    ideas = message.text.split()[1:]  # Ambil ide skrip dari pesan
    
    # Generate skrip berdasarkan ide-ide
    scripts = generate_script(ideas, wordlist)
    
    # Kirim skrip ke Telegram
    for script in scripts:
        bot.send_message(message.chat.id, script)

@bot.message_handler(commands=['Koding'])
def specific_script(message):
    global blokir_aktif, locked_commands, terbuka
    # Periksa apakah pesan memiliki kata-kata setelah perintah
    if len(message.text.split()) <= 1:
        bot.send_message(message.chat.id, "Usage: /Koding <subdomain+scanner+tools>")
        return
    
    # Ambil ide skrip dari pesan
    idea = message.text.split(maxsplit=1)[1]
    
    # Kata-kata kunci yang digunakan untuk mencari dependencies
    with open('/root/izmiftah/bahan.txt', 'r') as file:
        wordlist = file.readlines()
        wordlist = [word.strip() for word in wordlist]
    
    # Generate skrip berdasarkan ide yang ditentukan
    scripts = generate_script([idea], wordlist)
    
    # Kirim skrip ke Telegram
    for script in scripts:
        bot.send_message(message.chat.id, script)



import telebot
from fpdf import FPDF
from bs4 import BeautifulSoup
import requests
import os

# Fungsi untuk mengubah text menjadi PDF dengan baris baru setiap kata atau kalimatnya
def text_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Bagi teks berdasarkan baris baru
    lines = text.split("\n")

    # Tambahkan setiap baris ke PDF
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True)

    # Simpan PDF ke file
    pdf.output("unduh.pdf")

# Fungsi untuk mengubah gambar menjadi PDF
def image_to_pdf(image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="gambar", ln=True)
    pdf.image(image_path, x=10, y=20, w=180)
    pdf.output("unduh.pdf")

# Fungsi untuk mendeteksi link dan mengonversi halaman web ke PDF
def link_to_pdf(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    text_to_pdf(text)

# Fungsi untuk mengonversi HTML menjadi PDF
def html_to_pdf(html_content):
    # Simpan HTML ke file temporer
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    # Konversi HTML ke PDF
    pdfkit.from_file("temp.html", "unduh.pdf")

    # Hapus file temporer
    os.remove("temp.html")

# Fungsi untuk mengubah stiker menjadi PDF
def sticker_to_pdf(sticker_id):
    # Unduh stiker menggunakan ID stiker
    file_info = bot.get_file(sticker_id)
    file_path = file_info.file_path

    # Simpan stiker sebagai gambar sementara
    with open("unduh_stiker.png", 'wb') as new_file:
        file = bot.download_file(file_path)
        new_file.write(file)

    # Konversi gambar sementara ke PDF
    image_to_pdf("unduh_stiker.png")

    # Hapus gambar sementara
    os.remove("unduh_stiker.png")

# Fungsi untuk mengirim file PDF via Telegram
def send_pdf(chat_id):
    bot.send_document(chat_id, open("unduh.pdf", 'rb'))

# Command handler untuk command '/pdf'
@bot.message_handler(commands=['pdf'])
def handle_pdf(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")
        chat_id = message.chat.id
        if message.reply_to_message:
            if message.reply_to_message.text:
                text_to_pdf(message.reply_to_message.text)
            elif message.reply_to_message.photo:
                file_id = message.reply_to_message.photo[-1].file_id
                file_info = bot.get_file(file_id)
                file_path = file_info.file_path
                file = bot.download_file(file_path)
                with open("unduh.jpg", 'wb') as new_file:
                    new_file.write(file)
                image_to_pdf("unduh.jpg")
                os.remove("unduh.jpg")
            elif message.reply_to_message.sticker:
                sticker_to_pdf(message.reply_to_message.sticker.file_id)
            elif message.reply_to_message.entities:
                for entity in message.reply_to_message.entities:
                    if entity.type == 'url':
                        link_to_pdf(entity.url)
            elif message.reply_to_message.content_type == 'text':
                html_to_pdf(message.reply_to_message.text)
            send_pdf(chat_id)
        else:
            bot.reply_to(message, "Mohon gunakan reply pesan ke text, gambar, atau stiker untuk mengonversi ke PDF (/pdf).")
    else:
        bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")


import random
import requests
from bs4 import BeautifulSoup
from telebot import TeleBot

# Configuration files for colors and shapes
warna_file = 'warna.txt'
bentuk_file = 'bentuk.txt'

# Function to get image link from Pixabay
def get_image_link(keyword):
    url = f'https://pixabay.com/images/search/{keyword}%20texture/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        img_tag = soup.find('img', {'srcset': True})
        if img_tag:
            return img_tag['src']
    # Return a default image link if no image found
    return f'https://pixabay.com/images/search/{keyword}%20texture/'

# Function to get a random color from the file warna.txt
def get_random_color():
    with open(warna_file, 'r') as f:
        warna_list = [line.strip() for line in f.readlines()]
    return random.choice(warna_list)

# Function to get a random shape from the file bentuk.txt
def get_random_shape():
    with open(bentuk_file, 'r') as f:
        bentuk_list = [line.strip() for line in f.readlines()]
    return random.choice(bentuk_list)

# Function to generate an image description based on the prompt
def generate_image_prompt(prompt):
    # Split prompt into words
    words = prompt.split()

    # Get keyword from the prompt
    keyword = ' '.join(words)

    # Get image link from Pixabay
    image_link = get_image_link(keyword)

    # Get random color
    color = get_random_color()

    # Get random shape
    shape = get_random_shape()

    # Generate random values for hue, saturation, and light
    hue = random.randint(10, 100)
    saturation = random.randint(10, 100)
    light = random.randint(10, 100)

    # Create additional descriptive details
    volume = random.choice([
        'low', 'medium', 'high', 'very low', 'very high', 'subtle', 'intense',
        'mild', 'strong', 'balanced', 'minimal', 'excessive', 'moderate', 
        'extreme', 'soft', 'loud', 'whisper', 'roar', 'hum', 'buzz', 'quiet', 
        'noisy', 'silent', 'deafening', 'gentle', 'harsh', 'calm', 'fierce', 
        'muffled', 'crisp', 'clean', 'dirty', 'polished', 'rough', 'smooth', 
        'uneven', 'uniform', 'fluctuating', 'steady'
    ])
    symmetry = random.choice([
        'simetris', 'asimetris', 'radial', 'bilateral', 'rotasi', 
        'refleksional', 'translasional', 'seimbang', 'tidak seimbang', 'sempurna', 
        'tidak sempurna', 'perkiraan', 'tepat', 'terdistorsi', 'kacau', 'harmonis',
        'terstruktur', 'organik', 'geometris', 'abstrak', 'dinamis', 'statis',
        'biasa', 'tidak teratur', 'berulang', 'tidak berulang', 'konsisten',
        'tidak konsisten', 'sejajar', 'tidak selaras', 'kongruen', 'tidak selaras',
        'kohesif', 'terputus-putus', 'tersinkronisasi', 'tidak tersinkronisasi'
    ])
    pattern = random.choice([
        'bergaris', 'polkadot', 'polos', 'kotak-kotak', 'bunga', 'geometris', 
        'paisley', 'kotak-kotak', 'herringbone', 'houndstooth', 'argyle', 'ikat', 
        'chevron', 'zigzag', 'berlian', 'spiral', 'gelombang', 'abstrak', 
        'kamuflase', 'cetakan binatang', 'botani', 'linier', 'radial', 
        'konsentris', 'acak', 'grid', 'organik', 'simetris', 
        'asimetris', 'padat', 'gradien', 'bertekstur', 'timbul', 'terukir',
        'tergores', 'ditandai', 'digaris silang', 'anyaman', 'dilapisi', 'mesh'
    ])
    additional_items = random.choice([
        'tidak ada', 'sedikit', 'banyak', 'beberapa', 'banyak', 'tak terhitung', 'sedikit',
        'lusin', 'puluhan', 'ratusan', 'ribuan', 'banyak', 'kelimpahan', 
        'sedikit', 'banyak', 'grup', 'set', 'koleksi', 'array', 'variasi', 
        'bermacam-macam', 'seleksi', 'rentang', 'seri', 'urutan', 'suksesi',
        'string', 'aliran', 'baris', 'baris', 'kolom', 'tumpukan', 'tumpukan', 'tumpukan',
        'batch', 'cluster', 'mass', 'bundle', 'pack', 'crowd', 'swarm', 
        'kawanan', 'gerombolan'
    ])
    effect = random.choice([
        'ilusi', 'keseimbangan', 'efek cuaca', 'kehadiran spasial', 'keabadian',
        'gerakan', 'kedalaman', 'kontras', 'penekanan', 'irama', 'kesatuan', 'variasi',
        'pengulangan', 'proporsi', 'skala', 'harmoni', 'ketegangan', 'ketenangan',
        'kekacauan', 'kejelasan', 'ketidakjelasan', 'kecerahan', 'kegelapan', 'semangat',
        'nada teredam', 'transparansi', 'opasitas', 'ketajaman', 'keburaman', 
        'kejelasan', 'kebodohan', 'kehangatan', 'kesejukan', 'keakraban', 'kebaruan',
        'kesederhanaan', 'kompleksitas', 'keanggunan', 'kesederhanaan', 'modernitas', 'kuno'
    ])
    target_year = random.randint(2025, 2050)

    # Generate effects such as color, shape, and other attributes
    effect_description = f'{color} {shape} with {hue}% hue, {saturation}% saturation, {light}% light'

    # Create the output with the specified format
    output = (f'Image Link: {image_link}\n'
              f'Color and Shape: {effect_description}\n'
              f'Keyword: {keyword}\n'
              f'Volume: {volume}\n'
              f'Symmetry: {symmetry}\n'
              f'Pattern: {pattern}\n'
              f'Additional Items: {additional_items}\n'
              f'Effect: {effect}\n'
              f'Target Year: {target_year}\n')

    return output

# Function to handle messages with the /gambar command
@bot.message_handler(commands=['gambar'])
def handle_image_message(message):
    try:
        prompt = message.text.split(' ', 1)[1]  # Split only once to get the full prompt
        output = generate_image_prompt(prompt)
        bot.send_message(chat_id=message.chat.id, text=output)
    except IndexError:
        bot.send_message(chat_id=message.chat.id, text="Harap masukkan kata kunci setelah perintah /gambar. Contoh: /gambar bunga")


import random
import nltk
from googletrans import Translator
from telebot import TeleBot, types

# Load library for natural language processing
nltk.download('punkt')

# List of 5 popular languages and their language codes
# List of 100 popular languages and their language codes
languages = {
    'indonesia': 'id',
    'inggris': 'en',
    'jawa': 'jw',
    'jepang': 'ja',
    'jerman': 'de',
    'spanyol': 'es',
    'prancis': 'fr',
    'italia': 'it',
    'portugis': 'pt',
    'rusia': 'ru',
    'korea': 'ko',
    'arab': 'ar',
    'turki': 'tr',
    'belanda': 'nl',
    'swedia': 'sv',
    'norwegia': 'no',
    'finlandia': 'fi',
    'dansk': 'da',
    'ungaria': 'hu',
    'ceska': 'cs',
    'slovakia': 'sk',
    'afrikaans': 'af',
    'malaysia': 'ms',
    'thai': 'th',
    'vietnam': 'vi',
    'hebra': 'iw',
    'slowenia': 'sl',
    'croatia': 'hr',
    'serbia': 'sr',
    'bulsaria': 'bg',
    'islandia': 'is',
    'estonian': 'et',
    'latvia': 'lv',
    'lituania': 'lt',
    'armenian': 'hy',
    'georgia': 'ka',
    'malgasy': 'mg',
    'swahili': 'sw',
    'tamil': 'ta',
    'telugu': 'te',
    'punjabi': 'pa',
    'urdu': 'ur',
    'bengali': 'bn',
    'gujarati': 'gu',
    'marathi': 'mr',
    'kannada': 'kn',
    'malayalam': 'ml',
    'assamese': 'as',
    'kurdish': 'ku',
    'basque': 'eu',
    'catalan': 'ca',
    'sunda': 'su',
    'tagalog': 'tl',
    'hawaiian': 'haw',
    'samoan': 'sm',
    'fijian': 'fj',
    'tongan': 'to',
    'maori': 'mi',
    'zulu': 'zu',
    'xhosa': 'xh',
    'haitian creole': 'ht',
    'serbo-croatian': 'sh',
    'maltese': 'mt',
    'icelandic': 'is',
    'latin': 'la',
    'pahlavi': 'pal',
    'guarani': 'gn',
    'quechua': 'qu',
    'aymara': 'ay',
    'mongolian': 'mn',
    'tuvinian': 'tyv',
    'bihari': 'bih',
    'chichewa': 'ny',
    'hindi': 'hi',
    'klingon': 'tlh',
    'valyrian': 'vly',
    'na’vi': 'na',
    'esperanto': 'eo',
    'interlingua': 'ia'
}

# Define the function to generate the mind map
def generate_mind_map(text):
    words = nltk.word_tokenize(text)
    
    if len(words) > 100:
        words = words[:100]

    # Randomly select words with a maximum of 10 for each list
    wordlist1 = random.choices(words, k=min(10, len(words)))
    wordlist2 = random.choices(words, k=min(10, len(words)))
    wordlist3 = random.choices(words, k=min(10, len(words)))
    
    combined_wordlist = wordlist1 + wordlist2 + wordlist3
    random.shuffle(combined_wordlist)

    mind_map = {}
    translator = Translator()

    for word in combined_wordlist:
        translations = {}
        for lang_name, lang_code in languages.items():
            try:
                translated_word = GoogleTranslator(word, dest=lang_code).text
                translations[lang_name] = translated_word
            except Exception as e:
                translations[lang_name] = word  # Use original word if translation fails
                break  # Break out if translation fails to avoid excessive errors

        mind_map[word] = translations  # Store translations

    return mind_map

# Define the function to generate the ASCII art
def generate_ascii_art(mind_map):
    ascii_art = ''
    for word, properties in mind_map.items():
        translations_str = ', '.join(f'{lang}: {translated}' for lang, translated in properties.items())
        ascii_art += f"{word} -> {translations_str}\n"
    return ascii_art
    
# Main function to handle the command
@bot.message_handler(commands=['ACAK'])
def handle_acakan(message):
    text = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else ''
    if text:
        mind_map = generate_mind_map(text)
        ascii_art = generate_ascii_art(mind_map)
        with open('mindmap.txt', 'w') as f:
            f.write(ascii_art)
        with open('mindmap.txt', 'rb') as ascii_file:
            bot.send_document(message.chat.id, ascii_file)
        mind_map_message = "\n".join([f"{original}: {', '.join([f'mindmap {lang}: {translated}' for lang, translated in translations.items()])}" for original, translations in mind_map.items()])
        
        # Send the mind map as a message
        bot.send_message(message.chat.id, mind_map_message)
    else:
        bot.reply_to(message, "Please provide some text after the command.")

import telebot
import fitz  # PyMuPDF
import pandas as pd
from bs4 import BeautifulSoup
import re
from googletrans import Translator

translator = Translator()

@bot.message_handler(func=lambda message: True and message.text.startswith(f'/PDF'))
def handle_cut_command(message):
    try:
        if not message.reply_to_message or not message.reply_to_message.document:
            bot.reply_to(message, "Please reply to the document with the /PDF command.")
            return

        command_parts = message.text.split(' ', 3)
        if len(command_parts) != 4:
            bot.reply_to(message, "Invalid command format. Use '/PDF {label1!label2/tag1>tag2/page1:page2/text1;text2} {amount} {language}'")
            return

        label, amount, language = command_parts[1], int(command_parts[2]), command_parts[3]
        file_info = bot.get_file(message.reply_to_message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_name = message.reply_to_message.document.file_name

        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        if file_name.endswith('.pdf'):
            result_file = handle_pdf(file_name, label, amount, language)
        elif file_name.endswith('.csv'):
            result_file = handle_csv(file_name, label, amount, language)
        elif file_name.endswith('.html'):
            result_file = handle_html(file_name, label, amount, language)
        else:
            bot.reply_to(message, "Unsupported file type. Only PDF, CSV, and HTML are supported.")
            return

        with open(result_file, 'rb') as doc:
            bot.send_document(message.chat.id, doc)

        usage_message = (
            "PDF Files: Use /PDF {label1 !label2/page1:page2} {amount} {language} to process specific pages or entire documents.\n"
            "CSV Files: Use /PDF {label!} {amount} {language} to target multiple columns.\n"
            "HTML Files: Use /PDF {tag>/} {amount} {language} for nested tags."
        )
        bot.send_message(message.chat.id, usage_message)

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

def handle_pdf(file_name, label, amount, language):
    doc = fitz.open(file_name)
    labels = label.split('!')
    text_to_translate = []

    if '/' in label:
        page_range = label.split('/')[-1]
        range_of_pages = parse_page_range(page_range)
    else:
        range_of_pages = range(doc.page_count)

    for page in doc:
        if page.number + 1 in range_of_pages:
            for lbl in labels:
                text_instances = page.search_for(lbl)
                for inst in text_instances:
                    text = page.get_text('text', clip=inst)
                    text_to_translate.append(text)
                    # Use redaction to hide the text
                    page.add_redact_annot(inst)
            page.apply_redactions()

    translated_texts = [GoogleTranslator(text, dest=language).text for text in text_to_translate[:amount]]
    new_file_name = f"edited_{file_name}"
    doc.save(new_file_name)
    doc.close()
    return new_file_name

def handle_csv(file_name, label, amount, language):
    df = pd.read_csv(file_name)
    labels = label.split('!')
    text_to_translate = []

    for lbl in labels:
        text_to_translate.extend(df[lbl][:amount].tolist())
        df.drop(df.index[:amount], inplace=True)
    
    translated_texts = [GoogleTranslator(text, dest=language).text for text in text_to_translate]
    new_file_name = f"edited_{file_name}"
    df.to_csv(new_file_name, index=False)
    return new_file_name

def handle_html(file_name, label, amount, language):
    with open(file_name, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    tags = label.split('>')
    text_to_translate = []
    tags_to_remove = soup.find_all(re.compile(tags[0]))[:amount]

    for tag in tags_to_remove:
        for nested_tag in tags[1:]:
            tag = tag.find(re.compile(nested_tag))
            if not tag:
                break
        if tag:
            text_to_translate.append(tag.get_text())
            tag.decompose()

    translated_texts = [GoogleTranslator(text, dest=language).text for text in text_to_translate]
    new_file_name = f"edited_{file_name}"
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    return new_file_name

def parse_page_range(page_range):
    start, end = map(int, page_range.split(':'))
    return range(start, end + 1)

def parse_texts(texts):
    return texts.split(';')


import telebot
import requests
import re
import os
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO

# Fungsi untuk melakukan bypass link video
def bypass_link(url):
    # Melakukan import modul Iobypasser jika belum diimport
    import iobypasser

    # Mengecek apakah URL sudah di-bypass sebelumnya
    if url.startswith("https://www."):
        return url  # Jika sudah, langsung kembalikan URL

    try:
        # Melakukan bypass menggunakan Iobypasser
        bypassed_url = iobypasser.bypass(url)
        return bypassed_url
    except Exception as e:
        print("Gagal melakukan bypass:", e)
        return url  # Jika bypass gagal, kembalikan URL asli

    # Alternatif: Mengambil langsung link menggunakan wget
    # Jika menggunakan wget, pastikan wget sudah terpasang dan bisa diakses dari terminal
    # Contoh implementasi dengan wget:
    # os.system("wget --quiet --output-document=temp.html {}".format(url))
    # with open("temp.html", "r") as f:
    #     # Lakukan parsing untuk mendapatkan link video dari HTML jika perlu
    #     bypassed_url = f.read()  # Contoh sederhana: ambil isi file HTML sebagai link bypassed
    # os.remove("temp.html")  # Hapus file sementara setelah digunakan

    # Mengembalikan URL yang sudah di-bypass atau diambil
    # return bypassed_url

# Fungsi untuk mengunduh video dari URL
def download_video_yt(url):
    # Mendapatkan nama file dari URL
    file_name = "video.mp4"
    # Mengunduh video ke file lokal
    os.system("wget -O {} {}".format(file_name, url))
    return file_name

# Fungsi untuk mengirim video ke Telegram
def send_video(chat_id, video_path):
    # Menggunakan open() untuk membuka file video
    video = open(video_path, 'rb')
    # Mengirim video sebagai attachment
    bot.send_video(chat_id, video)
    # Menutup file setelah pengiriman
    video.close()

# Fungsi handler pesan
@bot.message_handler(commands=['unduh'])
def handle_message(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:          
        # Mengecek jika pesan mengandung link
        global blokir_aktif, locked_commands, terbuka
        if blokir_aktif != True and blokir_nonaktif != False and terbuka == True:             
            bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")
        else:
            if message.entities is not None:
                for entity in message.entities:
                    if entity.type == "url":
                        # Mendapatkan URL dari pesan
                        url = message.text[entity.offset:entity.offset + entity.length]
                        # Mengecek jika URL mengarah ke video
                        if re.match(r'.*(\.mp4|\.avi|\.mkv)', url):
                            # Melakukan bypass pada link video
                            bypassed_url = bypass_link(url)
                            # Mengunduh video
                            video_path = download_video(bypassed_url)
                            # Mengirim video ke pengguna
                            send_video(message.chat.id, video_path)
                        else:
                            bot.reply_to(message, "Maaf, hanya link video yang didukung.")
            # Jika pesan tidak mengandung link
            else:
            # Melakukan sesuatu ketika pesan tidak mengandung link
                bot.reply_to(message, "Maaf, pesan tidak mengandung link.")
    else:
         bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")            

import os
import telebot
from telebot import types
import random
from webcolors import hex_to_name

# Fungsi untuk membaca kode warna dari file palette.txt
def read_palette(file_path):
    with open(file_path, 'r') as file:
        palette = file.read().splitlines()
    return palette

# Fungsi untuk mengacak urutan warna pada palette
def shuffle_palette(palette):
    shuffled_palette = palette.copy()
    random.shuffle(shuffled_palette)
    return shuffled_palette

# Fungsi untuk mengubah kode warna menjadi 3 rangkaian kata
def shuffle_color(color):
    words_list = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "teal", "lime", "lavender", "maroon", "navy", "olive", "silver", "black", "white", "gray", "gold", "indigo", "ivory", "khaki", "tan", "turquoise", "violet", "beige", "azure", "coral", "crimson", "fuchsia", "plum"]
    # Pisahkan kode warna menjadi komponen RGB
    components = color.split()
    # Ambil 3 kata acak dari daftar kata warna
    shuffled_words = random.sample(words_list, 3)
    return ' '.join(shuffled_words)

# Fungsi untuk menjelaskan kode warna dalam format huruf dan HEX
def explain_color_code(color):
    explanation = ""
    for code in color.split():
        hex_code = "#" + code
        name = hex_to_name(hex_code)
        explanation += f"HEX: {hex_code}, RGB: {name}, "
    return explanation.rstrip(", ")  # Menghapus koma terakhir

# Command handler untuk /warna
@bot.message_handler(commands=['warna'])
def handle_palette(message):
    global blokir_aktif, locked_commands, terbuka
    # Lakukan pengecekan apakah direktori 'pallet.txt' ada
    try:
        with open('/root/izmiftah/pallet.txt', 'r') as file:
            # Membaca palette dari file
            palette = read_palette('/root/izmiftah/pallet.txt')
            
            # Mengacak urutan warna pada palette
            shuffled_palette = shuffle_palette(palette)
            
            # Mengubah setiap kode warna menjadi 3 rangkaian kata
            shuffled_colors = [shuffle_color(color) for color in shuffled_palette]
            
            # Mengirim pesan ke pengguna dengan warna yang sudah diacak
            explanation = explain_color_code(" ".join(shuffled_palette))
            bot.reply_to(message, f"Berikut adalah penjelasan warna yang dihasilkan setelah mengacak:\n\n{explanation}")
    # Tangani exception jika file tidak ditemukan
    except FileNotFoundError:
        bot.reply_to(message, "File 'pallet.txt' tidak ditemukan.")
    
    # Tangani exception lainnya
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

def baca_penyakit_dan_gejala():
    penyakit_dict = {}
    try:
        with open('/root/izmiftah/penyakit.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(':')
                if len(data) == 2:
                    penyakit = data[0].strip()
                    gejala = [g.strip().lower() for g in data[1].split(';')]
                    penyakit_dict[penyakit] = gejala
    except FileNotFoundError:
        print("File penyakit.txt tidak ditemukan.")
    return penyakit_dict

def cari_penyakit(gejala_input, penyakit_dict):
    gejala_input = [g.strip().lower() for g in gejala_input]
    hasil = []
    for penyakit, gejala in penyakit_dict.items():
        if len(set(gejala_input) & set(gejala)) >= 1:
            hasil.append(penyakit)
    return hasil

def cari_obat(penyakit):
    try:
        conn = sqlite3.connect('obat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT obat FROM obat WHERE penyakit=?", (penyakit,))
        hasil = cursor.fetchall()
        conn.close()
        return [row[0] for row in hasil]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@bot.message_handler(func=lambda message: message.text.startswith('/konsul'))
def handle_konsul(message):
    try:
        if len(message.text) < 3:
            bot.reply_to(message, "Pesan terlalu pendek. Mohon masukkan gejala atau penyakit dengan format yang benar.")
            return
        
        query = message.text.split(' ', 1)[1].strip()  # Mengambil semua teks setelah '/konsul'
        penyakit_dict = baca_penyakit_dan_gejala()
        
        if ';' in query:
            gejala_input = query.split(';')
            hasil = cari_penyakit(gejala_input, penyakit_dict)
            if hasil:
                bot.reply_to(message, f"Gejala tersebut sesuai dengan penyakit: {', '.join(hasil)}")
            else:
                bot.reply_to(message, "Tidak ditemukan penyakit yang sesuai dengan gejala tersebut.")
        else:
            penyakit = query
            hasil = cari_obat(penyakit)
            if hasil:
                bot.reply_to(message, f"Obat untuk penyakit {penyakit}: {', '.join(hasil)}")
            else:
                bot.reply_to(message, "Tidak ditemukan obat untuk penyakit tersebut.")
                
    except IndexError:
        bot.reply_to(message, "Format gejala atau penyakit tidak valid. Pastikan menggunakan format '/konsul gejala1;gejala2;...' atau '/Konsul penyakit'.")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")


@bot.message_handler(func=lambda message: message.text.startswith('/KONSUL'))
def handle_verifikasi(message):
    try:
        if len(message.text) < 2:
            bot.reply_to(message, "Pesan terlalu pendek. Mohon masukkan pesan dengan format yang benar.")
            return
        
        query = message.text.split()[1:]  # Ambil kata-kata setelah '/KONSUL'
        search_query = '+'.join(query)
        url = f"https://www.google.com/search?q={search_query}"
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        hasil = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
        
        if hasil:
            descriptions = [item.text for item in hasil]
            bot.reply_to(message, "\n\n".join(descriptions))
        else:
            bot.reply_to(message, "Tidak ditemukan informasi terkait.")
    
    except requests.RequestException as e:
        bot.reply_to(message, f"Terjadi kesalahan saat menghubungi Google: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

@bot.message_handler(func=lambda message: message.text.startswith('/Konsul'))
def handle_Konsul2(message):
    try:
        if len(message.text) < 2:
            bot.reply_to(message, "Pesan terlalu pendek. Mohon masukkan penyakit dengan format yang benar.")
            return
        penyakit = message.text.split(' ', 1)[1].strip()
        hasil = cari_obat(penyakit)
        if hasil:
            bot.reply_to(message, f"Obat untuk penyakit {penyakit}: {', '.join(hasil)}")
        else:
            bot.reply_to(message, "Tidak ditemukan obat untuk penyakit tersebut.")
    except IndexError:
        bot.reply_to(message, "Format penyakit tidak valid. Pastikan menggunakan format '/Konsul (penyakit)'.")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")


import telebot
import random
import urllib.parse
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Fungsi untuk membaca kegunaan dari file kegunaan.txt dan mengacaknya
def read_and_shuffle_usage(file_path):
    with open(file_path, 'r') as file:
        usages = file.read().splitlines()
    return shuffle_wordlist(usages)

# Fungsi untuk mengacak wordlist
def shuffle_wordlist(wordlist):
    shuffled_wordlist = wordlist.copy()
    random.shuffle(shuffled_wordlist)
    return shuffled_wordlist

# Fungsi untuk mendapatkan prompt {nama aplikasi} = untuk {kegunaan}
def generate_app_name(merek, usage, function):
    return f"{merek} {usage} {function}"

# Command handler untuk /newapk
@bot.message_handler(commands=['apk'])
def handle_acakprompt(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:         
        try:
            # Membaca dan mengacak kegunaan dari file
            usages = read_and_shuffle_usage('/root/izmiftah/kegunaan.txt')
            
            # Memilih satu merek secara acak
            merek = random.choice(["Adobe", "Microsoft", "Google", "Apple", "Amazon"])
            
            # Memilih satu kegunaan secara acak
            usage = random.choice(usages)
            
            # Memilih satu fungsi secara acak
            function = random.choice(["Viewer", "Editor", "Manager", "Assistant", "Optimizer"])
            
            # Membuat nama aplikasi baru
            new_app_name = generate_app_name(merek, usage, function)
            
            # Mengirim nama aplikasi baru ke pengguna
            bot.reply_to(message, new_app_name)
        except Exception as e:
            bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")
    else:
         bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")        

# Wordlist untuk digunakan dalam penggantian kalimat
wordlist = ["Top", "Github", "Popular", "Recommended", "Favorite", "Essential", "Must-have", "Leading", 
            "Trending", "Sought-after", "Preferred", "Desired", "Favored", "Beloved", 
            "Chosen", "In-demand", "Highly-rated", "Hot", "Well-liked", "Fancy", "Cool", 
            "Slick", "Stylish", "Chic", "Hip", "Alternatif", "Viral", "Automate-apps", "Ai-apps"]

# Command handler untuk /newapk
@bot.message_handler(commands=['newapk'])
def handle_cari(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:         
        try:
            # Dapatkan nama new apk dari input pengguna
            apk_name = message.text.split(' ', 1)[1]
            
            # Bangun rangkaian kata acak untuk digunakan dalam kalimat
            random_words = random.sample(wordlist, 1)  # Ambil 3 kata acak dari wordlist
            random_phrase = ' '.join(random_words)
            
            # Escape nama apk dari pengguna dan sertakan dalam query
            query = f"{random_phrase} apps for \"{apk_name}.zip full version\""
            
            # Encode query untuk digunakan dalam URL
            encoded_query = urllib.parse.quote_plus(query)
            
            # URL pencarian Google
            search_url = f"https://www.google.com/search?q={encoded_query}"
            
            # Mengirim hasil pencarian ke pengguna
            bot.reply_to(message, f"Ini hasil pencarian yang relevan untuk {apk_name}: {search_url}")
        except Exception as e:
            bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")
    else:
         bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")        

import logging
import os
import time
import subprocess
import asyncio
from telebot import *
from yt_dlp import *
from googletrans import Translator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
translator = Translator()

# Set longer timeout for bot
bot.timeout = 30
bot.read_timeout = 30

def send_with_retry(func, *args, **kwargs):
    retry_count = 3
    for attempt in range(retry_count):
        try:
            return func(*args, **kwargs)
        except (Timeout, ConnectionError) as e:
            if attempt < retry_count - 1:
                time.sleep(2)
            else:
                raise e

def download_with_retries(media_link, output_file, max_retries=3):
    retries = 0
    if retries < max_retries:
        try:
            download_sosmed(media_link, output_file)
            if os.path.exists(output_file):
                return True
            else:
                raise ValueError("Download failed.")
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {e}")
            if retries < max_retries:
                time.sleep(1)  # Wait before retrying
    return False

def get_download_info_yt(media_link, output_file):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_file
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([media_link])
        print(f"Successfully downloaded: {output_file}")
    except Exception as e:
        raise Exception(f"Error during download_media_yt: {e}")

import yt_dlp

def download_media_yt(media_link, output_file):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best available audio
        'outtmpl': output_file,      # Output filename
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([media_link])
        print(f"Successfully downloaded: {output_file}")
    except Exception as e:
        raise Exception(f"Error during download_media_yt: {e}")

   
def download_audio_yt(message, media_url):
    try:
        bot.send_chat_action(message.chat.id, 'upload_audio')
        media_link = media_url
        
        output_file = f"audio.mp3"  # Use video ID as filename
        info_dict = get_download_info_yt(media_link, output_file='audio.mp3')
        if download_with_retries(media_link, output_file):
            with open('audio.mp3', 'rb') as audio_file:
                bot.send_document(message.chat.id, audio_file)
        else:
            bot.reply_to(message, "silahkan lakukan /download audio.mp3 konversi ke ogg dengan /convert audio.mp3 ogg output untuk konversi ke output.ogg")
            with open('audio.mp3', 'rb') as audio_file:
                bot.send_document(message.chat.id, audio_file)
            if os.path.exists('audio'):
                with open('audio', 'rb') as audio_file:
                    bot.send_document(message.chat.id, audio_file)
                os.remove('audio')
            if os.path.exists('audio.mp3'):
                os.remove('audio.mp3')
    except ValueError as e:
        bot.reply_to(message, f"Error: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

def download_from_yt(message, media_url):
    try:
        bot.send_chat_action(message.chat.id, 'upload_audio')
        media_link = media_url
        media_type = 'video'
        output_file = f"video"  # Use video ID as filename
        info_dict = download_media_yt(media_link, output_file='video')
        if download_with_retries(media_link, output_file):
            with open(output_file, 'rb') as audio_file:
                bot.send_audio(message.chat.id, audio_file)
        else:
            bot.reply_to(message, "silahkan lakukan /download video atau konversi ke ogg dengan /convert video ogg output untuk konversi ke output.ogg")
            with open(output_file, 'rb') as audio_file:
                bot.send_document(message.chat.id, audio_file)
            if os.path.exists('video'):
                os.remove('video')
            if os.path.exists('video.mp4'):
                os.remove('video.mp4')    
    except ValueError as e:
        bot.reply_to(message, f"Error: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

def get_download_info(media_link):
    ydl_opts = {
        'format': 'best',
        'quiet': True
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(media_link, download=False)
    except Exception as e:
        raise ValueError(f"Error during get_download_info: {e}")

def download_sosmed2(url, output_name):
    ydl_opts = {
        'outtmpl': output_name,
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@bot.message_handler(commands=['yt', 'fb', 'ig', 'tw', 'tt'])
def handle_download_audio_yt(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "❌ Please provide a media URL.")
        return
    output_file = 'audio'    
    media_url = message.text.split(maxsplit=1)[1]
    download_audio_yt(message, media_url)

# Function to convert video to audio
def convert_to_audio(video_path):
    try:
        audio_path = video_path.replace('.mp4', '.mp3')
        command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}"
        subprocess.run(command, shell=True, check=True)
        return audio_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Error converting video to audio: {e}")
        raise ValueError("Failed to convert video to audio.")

# Function to embed subtitles into video
def embed_subtitle(video_path, subtitle_text):
    try:
        subtitle_file = "temp_subtitle.vtt"
        
        with open(subtitle_file, 'w', encoding='utf-8') as f:
            f.write(subtitle_text)
        
        output_path = video_path.replace('.mp4', '_with_subtitle.mp4')
        command = f"ffmpeg -i {video_path} -vf subtitles={subtitle_file} {output_path} -y"
        subprocess.run(command, shell=True, check=True)
        
        return output_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Error embedding subtitle: {e}")
        raise ValueError("Failed to embed subtitle.")

# Handle messages for subtitles
@bot.message_handler(func=lambda message: message.text.startswith('/YTSub') or message.text.startswith('/YTSUB'))
def handle_message_subtitle(message):
    try:
        parts = message.text.split()
        
        if len(parts) == 3 and parts[0] == '/YTSUB':
            command, filename, lang = parts
            
            with open(filename, 'r', encoding='utf-8') as f:
                subtitle_text = f.read()
            
            translated_text = GoogleTranslator(subtitle_text, dest=lang).text
            
            video_path = download_video(parts[1])
            if not video_path:
                bot.reply_to(message, "❌ Failed to download video.")
                return
            
            final_video = embed_subtitle(video_path, translated_text)
            if not final_video:
                bot.reply_to(message, "❌ Failed to embed subtitle into video.")
                return
            
            with open(final_video, 'rb') as file:
                bot.send_document(message.chat.id, file)

        elif len(parts) == 2 and parts[0] == '/YTSub':
            filename = parts[1]
            
            subtitle_file = "temp_subtitle.vtt"
            
            with open(subtitle_file, 'r', encoding='utf-8') as f:
                subtitle_text = f.read()
            
            video_path = download_video(filename)
            if not video_path:
                bot.reply_to(message, "❌ Failed to download video.")
                return
            
            final_video = embed_subtitle(video_path, subtitle_text)
            if not final_video:
                bot.reply_to(message, "❌ Failed to embed subtitle into video.")
                return
            
            with open(final_video, 'rb') as file:
                bot.send_document(message.chat.id, file)
        
        else:
            bot.reply_to(message, "❌ Invalid command format. Please use:\n/YTSUB {YouTube link} {language}\n/\n/YTSub {YouTube link}")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        bot.reply_to(message, f"❌ An error occurred: {e}")

@bot.message_handler(commands=['ytsub'])
def handle_message_ytsub(message):
    try:
        parts = message.text.split()
        
        if len(parts) == 3 and parts[0] == '/ytsub':
            command, filename, lang = parts
            
            with open(filename, 'r', encoding='utf-8') as f:
                subtitle_text = f.read()
            
            translated_text = GoogleTranslator(subtitle_text, dest=lang).text
            
            video_path = download_video(parts[1])
            if not video_path:
                bot.reply_to(message, "❌ Failed to download video.")
                return
            
            final_video = embed_subtitle(video_path, translated_text)
            if not final_video:
                bot.reply_to(message, "❌ Failed to embed subtitle into video.")
                return
            
            with open(final_video, 'rb') as file:
                bot.send_document(message.chat.id, file)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        bot.reply_to(message, f"❌ An error occurred: {e}")

# Handle messages for video download and audio conversion
@bot.message_handler(func=lambda message: message.text.startswith('/YT'))
def handle_message_yt(message):
    try:
        parts = message.text.split()
        
        if len(parts) != 2 or parts[0] != '/YT':
            bot.reply_to(message, "❌ Invalid command format. Use: /YT {YouTube link}")
            return
        
        url = parts[1]
        
        try:
            output_name = 'youtube'
            
            bot.send_chat_action(message.chat.id, 'upload_video')
            
            video_path = download_sosmed2(url, output_name)
            
            with open('youtube.mp4', 'rb') as video_file:
                bot.send_video(message.chat.id, video_file)
            
            audio_path = convert_to_audio(video_path)
            
            with open(audio_path, 'rb') as audio_file:
                bot.send_audio(message.chat.id, audio_file)
            
            os.remove(video_path)
            
            os.remove(audio_path)

            bot.reply_to(message,"Successfull!")

            os.remove('youtube.mp4')
    
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            bot.reply_to(message,f"❌ An unexpected error occurred.")
            
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        bot.reply_to(message,f"❌ An unexpected error occurred.")    

# Command handler for video download
@bot.message_handler(commands=['DOWNLOAD'])
def handle_download_video(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "❌ Please provide a media URL.")
        return
    output_file = 'video'    
    media_url = message.text.split(maxsplit=1)[1]
    download_from_yt(message, media_url)

import telebot
from telebot import types
import requests
import random
import string

# Default Cloudflare API key
DEFAULT_API_KEY = 'ID-IwlenUOwLtaFZI33p2_CS-8HoCTAPNrEFFYHs'

# Set your Cloudflare Account ID and Zone ID
ACCOUNT_ID = 'eb9851ec9c1f1597dffa745472e33984'
ZONE_ID = 'b2450a354d41101e17c4f3b29d8379aa'

# Valid DNS record types
VALID_DNS_RECORD_TYPES = ['A', 'CNAME', 'TXT', 'URL']

# Helper function to generate a random subdomain
def generate_random_subdomain(domain):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f'www{random_string}.{domain}'

# Error handler function
def handle_error(message, error_text):
    bot.reply_to(message, f"Error: {error_text}")

@bot.message_handler(commands=['domain'])
def create_custom_domain(message):
    try:
        args = message.text.split()
        if len(args) != 4:
            raise ValueError("Usage: /domain {record_type} {content} {target_domain}")
        
        record_type = args[1].upper()
        if record_type not in VALID_DNS_RECORD_TYPES:
            raise ValueError(f"Invalid DNS record type. Valid types are: {', '.join(VALID_DNS_RECORD_TYPES)}")
        
        content = args[2]
        target_domain = args[3]
        subdomain = generate_random_subdomain(target_domain)
        
        # Call Cloudflare's API to create a DNS record
        response = requests.post(
            f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records",
            headers={"Authorization": f"Bearer {DEFAULT_API_KEY}"},
            json={"type": record_type, "name": subdomain, "content": content}
        )
        
        if response.status_code == 200:
            bot.reply_to(message, f"Custom domain created: {subdomain}.1forum.my.id")
        else:
            handle_error(message, response.json())
    except Exception as e:
        handle_error(message, str(e))


@bot.message_handler(commands=['Domain'])
def create_zero_trust_tunnel(message):
    try:
        args = message.text.split()
        if len(args) != 2:
            raise ValueError("Usage: /Domain {local_url}")
        
        local_url = args[1]
        user_id = message.from_user.id
        tunnel_name = f"{user_id}_tunnel{random.randint(1, 1000)}"
        
        # Call Cloudflare's API to create a tunnel
        response = requests.post(
            f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/tunnels",
            headers={"Authorization": f"Bearer {DEFAULT_API_KEY}"},
            json={"name": tunnel_name, "config": {"url": local_url}}
        )
        
        if response.status_code == 200:
            tunnel_id = response.json()['result']['id']
            install_command = (
                "cloudflared login\n"
                "nano config.yaml\n"
                f"tunnel: {tunnel_id}\n"
                "credentials-file: /path/to/your/credentials/file.json\n"
                "nano file.json\n"
                '{\n'
                '    "email": "your@email.com",\n'
                '    "api_key": "your_api_key"\n'
                '}\n\n'
                "cloudflared tunnel --config config.yml start\n"
                "cloudflared tunnel status"
            )
            bot.reply_to(message, f"Zero Trust tunnel created: {tunnel_name}\n\nInstallation Instructions:\n{install_command}")
        else:
            handle_error(message, response.json())
    except Exception as e:
        handle_error(message, str(e))
        

import os
import subprocess
import telebot
from deepspeech import Model
import numpy as np
import wave
import datetime
from googletrans import Translator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize your DeepSpeech model
model = Model('/root/deepspeech-0.9.3-models.pbmm')

# Function to check if the video file has an audio stream
def has_audio_stream(video_file):
    cmd = f'ffprobe -i {video_file} -show_streams -select_streams a -loglevel error'
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        logger.error(f"ffprobe error: {e.stderr.decode().strip()}")
        return False

# Function to extract audio from video and transcribe
def transcribe_video_audio(video_file):
    if not has_audio_stream(video_file):
        logger.error(f"No audio stream found in {video_file}")
        return None

    audio_file = 'audio_extracted.wav'
    cmd = f'ffmpeg -i {video_file} -vn -acodec pcm_s16le -ar 16000 -ac 1 {audio_file}'
    try:
        subprocess.run(cmd, shell=True, check=True)
        transcription = transcribe_audio(audio_file)
        os.remove(audio_file)  # Clean up extracted audio file
        return transcription
    except subprocess.CalledProcessError as e:
        logger.error(f"Error extracting audio: {e.stderr.decode().strip()}")
        return None

# Function to extract audio from OGG and transcribe
def transcribe_ogg_audio(ogg_file):
    audio_file = 'audio_extracted.wav'
    if extract_audio_from_ogg(ogg_file, audio_file):
        transcription = transcribe_audio(audio_file)
        os.remove(audio_file)  # Clean up extracted audio file
        return transcription
    else:
        return None

# Function to extract audio from OGG using ffmpeg
def extract_audio_from_ogg(ogg_file, audio_file):
    cmd = f'ffmpeg -i {ogg_file} -vn -acodec pcm_s16le -ar 16000 -ac 1 {audio_file}'
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Error extracting audio from OGG: {e.stderr.decode().strip()}")
        return False

# Function to transcribe audio using DeepSpeech
def transcribe_audio(audio_file):
    try:
        # Open the audio file
        with wave.open(audio_file, 'rb') as wf:
            # Ensure the audio format is correct
            assert wf.getnchannels() == 1
            assert wf.getsampwidth() == 2
            assert wf.getframerate() == 16000

            # Read the audio data
            audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
            transcription = model.stt(audio)
        return transcription
    except Exception as e:
        logger.error(f"Error transcribing audio: {str(e)}")
        return None

# Function to translate text
def translate_text(text, target_language):
    translated_text = GoogleTranslator(text, dest=target_language)
    return translated_text.text

# Function to generate subtitle in SRT format
def generate_srt(transcription):
    lines = transcription.split('\n')
    srt_content = ''
    index = 1
    for line in lines:
        if line.strip() != '':
            start_time = datetime.timedelta(seconds=index)
            end_time = datetime.timedelta(seconds=index + 5)  # Duration of each subtitle is 5 seconds
            srt_content += f"{index}\n{start_time} --> {end_time}\n{line}\n\n"
            index += 5
    return srt_content

# Example function to handle Telegram message
@bot.message_handler(func=lambda message: message.text.startswith('/Terjemahkan'))
def handle_message(message):
    try:
        parts = message.text.split()
        
        if len(parts) != 3:
            bot.reply_to(message, "Format perintah tidak valid. Gunakan: /Terjemahkan [bahasa] [nama_file]")
            return
        
        target_language = parts[1]
        file_name = parts[2]
        
        # Handle different file types here
        if file_name.endswith('.wav'):
            transcription = transcribe_audio(file_name)
        elif file_name.endswith('.webm') or file_name.endswith('.mp4'):
            transcription = transcribe_video_audio(file_name)
        elif file_name.endswith('.ogg'):
            transcription = transcribe_ogg_audio(file_name)
        else:
            bot.reply_to(message, f"Format file tidak didukung untuk transkripsi.")
            return
        
        if transcription is None:
            bot.reply_to(message, "Gagal mengekstrak atau mentranskrip file audio.")
            return
        
        # Translate and send the transcription
        translated_text = translate_text(transcription, target_language)
        bot.send_message(chat_id=message.chat.id, text=translated_text)
        
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {str(e)}")
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

import telebot
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Function to generate stickers
def generate_stickers(image_paths, chat_id):
    # Your code to generate emojis
    emojis = generate_random_emojis(100)

    # Limit the number of images to 100
    if len(image_paths) > 100:
        image_paths = image_paths[:100]

    sticker_links = []

    # Loop through each image path
    for img_path in image_paths:
        try:
            # Open the image
            image = Image.open(img_path)

            # Add random emoji
            add_random_emoji(image, emojis)

            # Save the sticker
            sticker_path = img_path.replace(".jpg", "_sticker.png")
            image.save(sticker_path)

            # Upload sticker to Telegram and get link
            with open(sticker_path, 'rb') as sticker_file:
                sticker_message = bot.send_sticker(chat_id, sticker_file)
                sticker_links.append(sticker_message.sticker.file_id)

            # Remove temporary sticker file
            os.remove(sticker_path)

        except Exception as e:
            # Raise exception if any error occurs
            raise e

    return sticker_links

# Function to generate random emojis
def generate_random_emojis(num_emojis):
    # Your code to generate random emojis
    emojis = []

    return emojis

# Function to add random emoji to image
# Function to add random emoji to image
def add_random_emoji(image, emojis):
    # Get random emoji
    random_emoji = np.random.choice(emojis)

    # Open font file for drawing text
    font_path = "noto.ttf"  # Replace with actual font file path
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)

    # Generate random position for the emoji
    width, height = image
    x = np.random.randint(0, width - font_size)
    y = np.random.randint(0, height - font_size)

    # Draw the emoji on the image
    draw = ImageDraw.Draw(image)
    draw.text((x, y), random_emoji, fill=(255, 255, 255), font=font)


# Command handler for /sticker
@bot.message_handler(commands=['sticker'])
def handle_sticker(message):
    try:
        # Get image paths from message
        image_paths = message.text.split()[1:]  # Exclude the command itself

        # Generate stickers and get sticker links
        chat_id = message.chat.id
        sticker_links = generate_stickers(image_paths, chat_id)

        # Construct sticker links
        sticker_urls = [f"https://t.me/addstickers/{link}" for link in sticker_links]

        # Send sticker links
        for sticker_url in sticker_urls:
            bot.send_message(chat_id, sticker_url)

        # Reply to user with sticker link
        bot.reply_to(message, f"Stickers generated successfully! {sticker_urls}")

    except Exception as e:
        # Handle any exceptions
        bot.reply_to(message, f"Error: {str(e)}")


import requests
from bs4 import BeautifulSoup
import random
from urllib.parse import urlparse
import telebot

def get_random_domain(search_query):
    # Membuat permintaan pencarian ke Google
    url = f'https://www.google.com/search?q={search_query}&num=1'
    response = requests.get(url)
    if response.status_code == 200:
        # Menganalisis halaman hasil pencarian menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Menemukan semua tautan pada halaman hasil pencarian
        links = soup.find_all('a')
        # Mengambil URL dari tautan-tautan yang sesuai dengan domain
        domains = [link['href'].split('=')[1].split('&')[0] for link in links if 'https' in link['href'] and 'google' not in link['href']]
        # Mengambil domain secara acak dari daftar domain yang ditemukan
        random_domain = random.choice(domains)
        return random_domain
    else:
        print(f"Failed to fetch search results from Google. Status code: {response.status_code}")
        return None

def generate_random_sentence(domain):
    # Memecah domain menjadi kata-kata
    words = domain.split('.')
    # Jika domain memiliki lebih dari dua bagian (misalnya, youtube.com)
    if len(words) > 3:
        # Mengambil dua bagian terakhir dari domain
        sentence = '.'.join(words[-3:])
    else:
        # Menggunakan domain lengkap jika hanya terdiri dari dua bagian
        sentence = domain
    return sentence

def gacha2_handler(message, search_query):
    try:
        # Mengambil domain secara acak berdasarkan kata kunci pencarian
        domain = get_random_domain(search_query)
        if domain:
            # Menghasilkan kalimat acak dari domain
            sentence = generate_random_sentence(domain)
            bot.reply_to(message, f"Random Sentence from Domain: {sentence}")
            # Pencarian ulang setelah domain diproses
            gacha2_handler(message, search_query)
        else:
            bot.reply_to(message, "Failed to fetch random domain.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['gacha2'])
def start_gacha2(message):
    try:
        # Mendapatkan pesan yang dikirim oleh pengguna sebagai kata kunci pencarian
        search_query = message.text.split(' ', 1)[1].strip()
        # Memanggil fungsi gacha2_handler untuk memulai proses pencarian
        gacha2_handler(message, search_query)
    except IndexError:
        bot.reply_to(message, "Please provide a search query after the command.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

import socket
import requests
import telebot

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        location = data.get('loc')
        return location.split(',')
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_nearest_cname(ip):
    try:
        cname, _ = socket.gethostbyaddr(ip)
        return cname
    except Exception as e:
        print(f"Error: {e}")
        return None
		
@bot.message_handler(commands=['ipinfo'])
def ip_handler(message):
    try:
        ips = message.text.strip().split('\n')[1:]  # Exclude the command itself
        for ip in ips:
            location = get_location(ip)
            if location:
                location_str = f"Location: Latitude {location[0]}, Longitude {location[1]}"
            else:
                location_str = "Location: Not available"

            nearest_cname = get_nearest_cname(ip)
            if nearest_cname:
                cname_str = f"Nearest CNAME: {nearest_cname}"
            else:
                cname_str = "Nearest CNAME: Not available"

            response = f"IP: {ip}\n{location_str}\n{cname_str}\n"
            bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")


# Deep AI API Key
DEEP_KEY = 'deepai-api-key-kamu'

def generate_prompted(prompt):
    try:
		# Jika prompt berupa 'halo', maka kembalikan pesan yang sesuai
        if prompt.lower() == 'halo':
            return "assalamu alaikum bangbang! bukan halo"
        url = "https://api.deepai.org/api/chatgpt-alternative"  # Ganti endpoint URL
        headers = {
            "Content-Type": "application/json",
            "api-key": DEEP_KEY
        }
        data = {
            "text": prompt
        }
        response = requests.post(url, json=data, headers=headers)
        print(response.text)  # Debugging: Print response content
        if response.status_code == 200:
            result = response.json()
            if 'output' in result:
                return result['output']
            else:
                return f"Error in DeepAI response: {result}"
        else:
            error_message = response.json().get('error', 'Unknown error')  # Periksa pesan kesalahan yang spesifik
            return f"Error in DeepAI request. Status code: {response.status_code}. Details: {error_message}"
    except Exception as e:
        return f"Error in DeepAI request. Exception: {str(e)}"

def generate_image(prompt):
    try:
        url = "https://api.deepai.org/api/3d-cartoon-generator"
        headers = {
            "Content-Type": "application/json",
            "api-key": DEEP_KEY
        }
        data = {
            "text": prompt
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if 'output_url' in result:
                return result['output_url']
            else:
                return f"Error in DeepAI response: {result}"
        else:
            error_message = response.json().get('details', {}).get('input', {}).get('failedConstraints', 'Unknown error')
            return f"Error in DeepAI request. Status code: {response.status_code}. Details: {error_message}"
    except Exception as e:
        return f"Error in DeepAI request. Exception: {str(e)}"

def generate_video(prompt):
    try:
        url = "https://api.deepai.org/api/text2video"
        headers = {
            "Content-Type": "application/json",
            "api-key": DEEP_KEY
        }
        data = {
            "text": prompt
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if 'output_url' in result:
                return result['output_url']
            else:
                return f"Error in DeepAI response: {result}"
        else:
            error_message = response.json().get('details', {}).get('input', {}).get('failedConstraints', 'Unknown error')
            return f"Error in DeepAI request. Status code: {response.status_code}. Details: {error_message}"
    except Exception as e:
        return f"Error in DeepAI request. Exception: {str(e)}"

def send_formatted_message(message, formatted_message):
    bot.send_message(message.chat.id, formatted_message)

def ai_chat(message):
    try:
        message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No prompt provided."

        # Generate content based on the provided prompt
        generated_content = generate_prompted(message_text)

        # Send generated content as a reply
        send_formatted_message(message, generated_content)

    except Exception as e:
        bot.send_message(message.chat.id, str(e))

def ai_gambar(message):
    try:
        message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No prompt provided."
        generated_image = generate_image(message_text)

        bot.send_photo(message.chat.id, generated_image)

    except Exception as e:
        bot.send_message(message.chat.id, str(e))

def ai_video(message):
    try:
        message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No prompt provided."
        generated_video = generate_video(message_text)

        bot.send_video(message.chat.id, generated_video)

    except Exception as e:
        bot.send_message(message.chat.id, str(e))


@bot.message_handler(commands=['ai_chat'])
def handle_ai_chat(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
        elif blocked_users:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
                block_user(username)
        else:
            bot.send_message(message.chat.id, text=f"Selamat! Datang kembali {username}!")
            bot.send_message(message.chat.id, text="Silahkan melakukan /topup atau /payment untuk mengisi saldo sebanyak yang dibutuhkan.")
            global new_saldo, jumlah_koin, saldo_pengguna
            new_saldo -= 10
            jumlah_koin -= 5
            saldo_pengguna -= 10
            if jumlah_koin > 0 and saldo_pengguna > 0:
                ai_chat(message)
    except Exception as e:
        bot.send_message(message.chat.id, text="Terjadi kesalahan dalam memproses permintaan AI Chat. Mohon coba lagi nanti.")

@bot.message_handler(commands=['ai_video'])
def handle_ai_video(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
        elif blocked_users:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
                block_user(username)
        else:
            bot.send_message(message.chat.id, text=f"Selamat! Datang kembali {username}!")
            bot.send_message(message.chat.id, text="Silahkan melakukan /topup atau /payment untuk mengisi saldo sebanyak yang dibutuhkan.")
            global new_saldo, jumlah_koin, saldo_pengguna
            new_saldo -= 10
            jumlah_koin -= 5
            saldo_pengguna -= 10
            if jumlah_koin > 0 and saldo_pengguna > 0:
                ai_video(message)
    except Exception as e:
        bot.send_message(message.chat.id, text="Terjadi kesalahan dalam memproses permintaan AI Video. Mohon coba lagi nanti.")

@bot.message_handler(commands=['ai_gambar'])
def handle_ai_gambar(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
        elif blocked_users:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text="Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo.\nLakukan /pembayaran atau /bukablokir terlebih dahulu.")
                block_user(username)
        else:
            bot.send_message(message.chat.id, text=f"Selamat! Datang kembali {username}!")
            bot.send_message(message.chat.id, text="Silahkan melakukan /topup atau /payment untuk mengisi saldo sebanyak yang dibutuhkan.")
            global new_saldo, jumlah_koin, saldo_pengguna
            new_saldo -= 10
            jumlah_koin -= 5
            saldo_pengguna -= 10
            if jumlah_koin > 0 and saldo_pengguna > 0:
                ai_gambar(message)
    except Exception as e:
        bot.send_message(message.chat.id, text="Terjadi kesalahan dalam memproses permintaan AI Gambar. Mohon coba lagi nanti.")


command_status = False

def bypass(message):
    bot.send_message(message.chat.id, "[1] Bypass One URL")
    bot.send_message(message.chat.id, "[2] Bypass Multiple URLs")
    bot.send_message(message.chat.id, "[3] Exit")

@bot.message_handler(commands=['bypass'])
def handle_message(message):
    global command_status
    command_status = True
    bypass(message)

@bot.message_handler(func=lambda message: command_status)
def process_message(message):
    if message.text.lower() == 'exit':
        bot.reply_to(message, "Exiting...")
        bot.stop_polling()
    elif message.text.split()[0] == '1':
        msg = bot.reply_to(message, "Enter URL to Bypass:")
        bot.register_next_step_handler(msg, process_bypass_one)
    elif message.text.split()[0] == '2':
        msg = bot.reply_to(message, "Enter The File with URLs (Example: urls.txt):")
        bot.register_next_step_handler(msg, process_bypass_multiple)
    else:
        bot.reply_to(message, "Invalid input, please try again or type 'exit' to quit.")

def process_bypass_one(message):
    url = message.text
    payload = {"url": url}
    url_bypass = requests.post("https://bypass.bot.nu/", data=payload)
    if url_bypass.status_code != 200:  # If URL cannot be bypassed
        bot.send_message(message.chat.id, "Failed to bypass the URL. Please try another URL or check the URL format.")
        bot.send_message(message.chat.id, "You may refer to the support team for further assistance.")
        return
    bypassed = url_bypass.json()
    bot.send_message(message.chat.id, "Bypassed URL: " + bypassed["destination"])

def process_bypass_multiple(message):
    urls_file = message.text
    with open(urls_file, "r") as urls:
        for i in urls:
            url_bypass = {"url": i.strip()}
            bypass = requests.post("https://unshorten.me/", data=url_bypass)
            if bypass.status_code != 200:  # If URL cannot be bypassed
                bot.send_message(message.chat.id, f"Failed to bypass the URL: {i.strip()}.")
                bot.send_message(message.chat.id, "You may refer to the support team for further assistance.")
                continue
            bypassed = bypass.json()
            try:
                with open("bypassed.txt", "a") as bypassed_url:
                    bot.send_message(message.chat.id, f"[+] Bypassed URL: {bypassed['destination']}")
                    bypassed_url.write(bypassed["destination"] + "\n")
            except KeyError:
                bot.send_message(message.chat.id, "[-] Invalid URL Found")

@bot.message_handler(commands=['tulis'])
def export_text(message):
    bot.reply_to(message, "Please write in the format /tulis (filename without extension)> [text].")
    try:
        text = message.text.split('>')[1].strip()
        if len(text) < 1:
            bot.reply_to(message, "Please enter the text to be exported.")
            return
        file_name = message.text.split('>')[0].split()[1] + ".txt"
        
        with open(file_name, "w") as file:
            file.write(text)
        
        bot.reply_to(message, f"The text has been successfully exported to the file {file_name}.")
    
    except Exception as e:
        bot.reply_to(message, "An error occurred while exporting text. Please enter like /tulis [title of file]> [text].")
        print(str(e))

import socket
import pandas as pd
import telebot
import os

# Global variable to keep track of command state
command_state = False

# Function to get the IP address of a domain
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

@bot.message_handler(commands=['gacha'])
def handle_gacha_command(message):
    global command_state
    command_state = True  # Enable message processing for gacha command
    bot.reply_to(message, "Silakan kirim pesan yang ingin Anda gacha ke IP.")

@bot.message_handler(func=lambda message: command_state)
def cek_ip(message):
    global command_state
    command_state = False  # Disable message processing after this message

    # Limit the message to 10 words
    words = message.text.split(' ')
    if len(words) > 10:
        words = words[:10]  # Truncate the list to the first 10 words
        message.text = ' '.join(words)  # Reconstruct the message with limited words

    domains = message.text.split(' ')  # Split the message by spaces
    
    result_list = []
    for domain in domains:
        ip_address = get_ip_address(domain.strip())
        if ip_address:
            result_list.append((domain, ip_address))
        else:
            result_list.append((domain, "Alamat IP tidak ditemukan"))
    
    result_df = pd.DataFrame(result_list, columns=['Domain', 'Alamat IP'])
    
    response = f"Informasi Alamat IP untuk domain(s):\n{result_df.to_string(index=False)}"
    
    bot.reply_to(message, response)

# Handler untuk perintah /dork
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
            bot.send_message(message.chat.id, text=f"Results: {str(all_results)}")
        else:
            bot.reply_to(message, text="No results found.")

    except ValueError:
        # Menangani kesalahan jika format perintah tidak sesuai
        bot.reply_to(message, text="Invalid format. Use /dork <keywords>/<domain_extensions>")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

import requests
from bs4 import BeautifulSoup
import time

def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        return None
    return domain

def search_google(keyword, num_results=3):
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    query = f"https://www.google.com/search?q=https://. {keyword}"
    response = requests.get(query, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        count = 0
        results = []

        for a_tag in soup.find_all('a', href=True):
            url = a_tag['href']
            if url.startswith('http') or url.startswith('https'):
                print(f"Found URL: {url}")
                domain = extract_domain(url)
                result = None
                if domain:
                    result = {
                        'Keyword': keyword,
                        'URL': url,
                        'Domain': domain,
                    }
                if result:
                    results.append(result)
                    count += 1
                if count >= num_results:
                    break
            time.sleep(2)
    return results

# Code for handling '/dorking' command
@bot.message_handler(commands=['dorking'])
def handle_dorking(message):
    try:
        search_term = message.text.replace('/dorking', '').strip()

        results = search_google(search_term, num_results=5)  # Adjust the number of results as needed
        for i, result in enumerate(results, start=1):
            bot.send_message(message.chat.id, f"{i}. {result['URL']}")

    except Exception as e:
        bot.reply_to(message, "Format should be: /dorking [keyword]")
        print(e)

# Replace with your actual Telegram bot token and chat ID
bot_token = TOKEN

import os
import openai
import requests
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import telebot

# Set OpenAI credentials (placeholders for the purpose of this example)
org_entry = 'org-23sf7jpVu6oSEDwKBPhpk4XL'
api_key_entry = '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'

# Function to set OpenAI credentials
def set_openai_credentials():
    openai.organization = org_entry
    openai.api_key = api_key_entry

# Function to read prompt from a file
def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Fungsi untuk menghasilkan gambar dari prompt menggunakan DALL-E
def generate_image(prompt):
    set_openai_credentials()
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=100,  # Jumlah gambar yang dihasilkan
            size="500x500"
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        with open("temp.png", "wb") as f:
            f.write(response.content)
        image = Image.open("temp.png")
        image = image.resize((7240, 7240))
        return image
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save an image
def save_image(image, file_path="temp.png"):
    plt.imsave(file_path, np.array(image))
    return "Image saved successfully."

# Command handler for the Telegram bot to generate an image based on the input number
@bot.message_handler(commands=['gambarin'])
def handle_gambarin_command(message):
    # Extract the number from the message text
    try:
        # Split the message text by space and get the second part as the number
        file_number = int(message.text.split()[1])
        if 1 <= file_number <= 10:
            file_name = f"ai {file_number}.txt"
            if os.path.exists(file_name):
                prompt = read_prompt_from_file(file_name)
                image = generate_image(prompt)
                if image:
                    save_image(image)
                    with open("temp.png", "rb") as photo:
                        bot.send_photo(message.chat.id, photo)
                else:
                    bot.reply_to(message, "Failed to generate image.")
            else:
                bot.reply_to(message, f"File {file_name} does not exist.")
        else:
            bot.reply_to(message, "Please send a number between 1 and 3 after the command.")
    except (IndexError, ValueError):
        bot.reply_to(message, "Please send a valid command followed by a number between 1 and 3. Example: /gambarin2")

# Note: The rest of the bot script remains unchanged.
# Function to set OpenAI credentials
def set_openai_credentials():
    openai.organization = org_entry
    openai.api_key = api_key_entry

# Function to generate an image from a prompt
def generate_image(prompt):
    set_openai_credentials()
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=3,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        with open("temp.png", "wb") as f:
            f.write(response.content)
        image = Image.open("temp.png")
        image = image.resize((7240, 7240))
        return image
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save an image
def save_image(image, file_path="temp.png"):
    plt.imsave(file_path, np.array(image))
    return "Image saved successfully."

ALLOWED_EXTENSIONS = {'txt', 'html', 'png', 'pdf', 'jpg', 'csv', 'mp4', 'webm', 'mkv', 'ogg', 'mp3', 'srt', 'wav', 'vtt', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bot.message_handler(commands=['download'])
def download_filemu(message):
    try:
        file_name = message.text.split()[1]
        if not allowed_file(file_name):
            raise ValueError('File extension not allowed.')

        with open(file_name, 'rb') as f:
            bot.send_document(message.chat.id, f)
    except Exception as e:
        print(f"Error downloading file: {e}")
        bot.reply_to(message, text="Gagal mengunduh file. Pastikan file tersedia dan jenis file diizinkan.")

# Handler untuk perintah /update
@bot.message_handler(commands=['update'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

        subprocess.run(['bash', 'run.sh'], check=True)
        bot.reply_to(message, "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

# Fungsi untuk memproses input command
@bot.message_handler(commands=['ddos'])
def handle_command(message):
    message.chat.id = message.chat.id
    bot.send_message(message.chat.id, "Masukkan command 'proxychains4 python3 -m mampus aiddos.sh <nama file atau target kalian>'")

class user_manager:
    def __init__(self):
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS whitelist (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                confirm_attempts INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blacklist (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def is_whitelisted(self, user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM whitelist WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def is_blacklisted(self, user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM blacklist WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def whitelist_user(self, user_id, username):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO whitelist (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()
        conn.close()

    def blacklist_user(self, user_id, username):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO blacklist (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()
        conn.close()

    def increment_confirm_attempts(self, user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE whitelist SET confirm_attempts = confirm_attempts + 1 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()

    def get_confirm_attempts(self, user_id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT confirm_attempts FROM whitelist WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0

class UserManager:
    def __init__(self):
        self.init_db()

    def init_db(self):
        conn, cursor = get_db_connection('users')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS whitelist (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            confirm_attempts INTEGER DEFAULT 0
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS blacklist (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
        ''')
        conn.commit()
        
    def __init__(self, user_id):
        self.db_connection = get_db_connection('miftah')
        self.user_id = user_id

    def is_locked(self):
        cursor = self.db_connection[1]
        cursor.execute("SELECT 1 FROM locked_users WHERE user_id = ?", (self.user_id,))
        return cursor.fetchone() is not None

    def lock_user(self, password, token):
        cursor = self.db_connection[1]
        cursor.execute("INSERT OR IGNORE INTO locked_users (user_id, password, token) VALUES (?, ?, ?)", (self.user_id, password, token))
        self.db_connection[0].commit()

    def unlock_user(self):
        cursor = self.db_connection[1]
        cursor.execute("DELETE FROM locked_users WHERE user_id = ?", (self.user_id,))
        self.db_connection[0].commit()

    def get_token(self):
        cursor = self.db_connection[1]
        cursor.execute("SELECT token FROM locked_users WHERE user_id = ?", (self.user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_password(self):
        cursor = self.db_connection[1]
        cursor.execute("SELECT password FROM locked_users WHERE user_id = ?", (self.user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

    def is_whitelisted(self, user_id):
        conn, cursor = get_db_connection('users')
        cursor.execute("SELECT 1 FROM whitelist WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def is_blacklisted(self, user_id):
        conn, cursor = get_db_connection('users')
        cursor.execute("SELECT 1 FROM blacklist WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def whitelist_user(self, user_id, username):
        conn, cursor = get_db_connection('users')
        cursor.execute("INSERT OR IGNORE INTO whitelist (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()

    def blacklist_user(self, user_id, username):
        conn, cursor = get_db_connection('users')
        cursor.execute("INSERT OR IGNORE INTO blacklist (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()

    def increment_confirm_attempts(self, user_id):
        conn, cursor = get_db_connection('users')
        cursor.execute("UPDATE whitelist SET confirm_attempts = confirm_attempts + 1 WHERE user_id = ?", (user_id,))
        conn.commit()

    def get_confirm_attempts(self, user_id):
        conn, cursor = get_db_connection('users')
        cursor.execute("SELECT confirm_attempts FROM whitelist WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0

class TerminalRecorder:
    def __init__(self):
        self.buffer = []

    def record(self, output):
        self.buffer.append(output)

    def get_output(self):
        return '\n'.join(self.buffer)
        
terminal_recorder = TerminalRecorder()
user_manager = UserManager(user_id=admin_id)

import sqlite3

# Define the function to get a database connection
def get_db_connection(db_name='users.db'):
    conn = sqlite3.connect(db_name)
    return conn

# Function to create the users table if it does not exist
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT,
            password TEXT,
            token TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Call create_users_table at the start of the script to ensure the table exists
create_users_table()

import telebot
from PIL import Image
import os
import imageio

# Folder untuk menyimpan gambar sementara
image_folder = 'images'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

def get_user_image_path(user_id, img_number):
    return os.path.join(image_folder, f"file_{user_id}_{img_number}.jpg")

def generate_image_paths(user_id, start, end):
    for i in range(start, end + 1):
        yield get_user_image_path(user_id, i)

@bot.message_handler(commands=['Photo'])
def create_photo_animation(message):
    try:
        command_parts = message.text.split()
        if len(command_parts) < 4:
            bot.reply_to(message, "Invalid command format. Use /Photo {start-end} {urutan gambar yang di kecualikan} {gif/mp4}.")
            return

        user_id = message.from_user.id
        range_str = command_parts[1]
        start, end = map(int, range_str.split('-'))
        exclude_indices = [int(x) for x in command_parts[2].split(',') if x]
        format = command_parts[3].lower()

        image_paths = list(generate_image_paths(user_id, start, end))

        image_files = [img_path for i, img_path in enumerate(image_paths) if i not in exclude_indices]

        if not image_files:
            bot.reply_to(message, "No images found to create an animation.")
            return

        print(f"Files to be included in the animation: {image_files}")

        # Load images and ensure they have the same dimensions
        images = []
        for img_path in image_files:
            img = Image.open(img_path)
            img = img.convert('RGB')  # Convert to RGB mode if creating GIF
            images.append(img)

        output_file = f'animation.{format}'

        if format == 'gif':
            imageio.mimsave(output_file, images, duration=1500)
        elif format == 'mp4':
            with imageio.get_writer(output_file, fps=25, codec='libx264') as writer:
                for img in images:
                    writer.append_data(imageio.imread(img))
        else:
            bot.reply_to(message, "Invalid format. Use gif or mp4.")
            return

        with open(output_file, 'rb') as animation:
            bot.send_document(message.chat.id, animation)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


import telebot
import yt_dlp 
import urllib3
import os

def download_sosmed(url, output_name):
    ydl_opts = {
        'format': 'worts',
        'outtmpl': output_file
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([media_link])
        print(f"Successfully downloaded: {output_file}")
    except Exception as e:
        raise Exception(f"Error during download_media_yt: {e}")

  

# Command handler untuk mengunduh konten
@bot.message_handler(commands=['Download'])
def handle_download(message):
    try:
        command = message.text.split()
        if len(command) != 4:
            bot.reply_to(message, "Format perintah salah. Gunakan format: /Download {sosial media} {link} {nama file output}")
            return
        
        platform = command[1].lower()
        url = command[2]
        output_name = command[3]

        if platform in ['tiktok', 'snackvideo', 'instagram', 'facebook', 'twitter', 'all']:
            bot.reply_to(message, f"Mengunduh konten dari {platform}...")
            download_sosmed(url, output_name)
            bot.reply_to(message, f"Konten berhasil diunduh: {output_name}")
            # Mengirimkan file ke pengguna
            with open(output_name, 'rb') as video:
                bot.send_video(message.chat.id, video)
            os.remove(output_name)
        else:
            bot.reply_to(message, f"Platform {platform} tidak didukung.")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
        
import telebot
from googletrans import Translator
import pandas as pd
import random

# Membaca lirik dari file lirik.txt
with open('/root/izmiftah/lirik.txt', 'r') as file:
    ideas = file.readlines()

def shuffle_words(sentence):
    words = sentence.split()
    df = pd.DataFrame(words)
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    shuffled_sentence = ' '.join(shuffled_df[0])
    return shuffled_sentence

def generate_ideas(jumlah):
    random_ideas = random.choices(ideas, k=jumlah)
    shuffled_ideas = [shuffle_words(idea.strip()) for idea in random_ideas]
    return '\n---\n'.join(shuffled_ideas)

@bot.message_handler(commands=['Ide'])
def send_idea(message):
    try:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Usage: /Ide <jumlah> <bahasa>")
            return

        jumlah = int(parts[1])
        bahasa = parts[2]

        if jumlah < 1:
            bot.reply_to(message, "Jumlah harus lebih besar dari 0.")
            return

        generated_ideas = generate_ideas(jumlah)
        translation = GoogleTranslator(generated_ideas, src='en', dest=bahasa)
        
        # Menyimpan hasil ke dalam file lagu.txt
        with open('/root/izmiftah/lagu.txt', 'w') as file:
            file.write(translation.text)

        bot.reply_to(message, f"Ide dalam bahasa {bahasa}:\n{translation.text}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")

import os
import json
import base64
import qrcode
import datetime
import telebot
from telebot import types
from dotenv import load_dotenv
import cv2

# Function to generate QR code
def generate_qr_code(user_id, passsword):
    token_file = f'token_{user_id}.json'
    with open(token_file, 'r') as f:
        data = json.load(f)
        token = data.get('token')
        qr_code = qrcode.make(f"#Aktivasi {token}")
    qr_code_path = f"qr_code_{user_id}.png"
    qr_code.save(qr_code_path)
    return qr_code_path

# Function to generate base64 encoded QR code
def generate_base64_qr_code(qr_code_path):
    with open(qr_code_path, "rb") as f:
        qr_code_image = f.read()
    return base64.b64encode(qr_code_image).decode("utf-8")

@bot.message_handler(func=lambda message: message.text.startswith("#setuju"))
def handle_message(message):
    admin_bot_ini = os.getenv('adminbotnya')
    try:
        if message.from_user.username == admin_bot_ini:
            # Extract user_id and password from the message
            parts = message.text.split('@')
            if len(parts) > 1:
                sub_parts = parts[1].split('=')
                if len(sub_parts) == 2:
                    user_id = sub_parts[0].strip()
                    password = sub_parts[1].strip()

                    if password != passnya:
                        bot.send_message(chat_id=message.chat.id, text="Invalid password")
                        return

                    token_file = f"token_{user_id}.json"
                    if not os.path.exists(token_file):
                        bot.send_message(chat_id=message.chat.id, text="No token found. Please set /start the process again.")
                        return

                    with open(token_file, 'r') as f:
                        user_data = json.load(f)

                    if user_data.get('paid'):
                        qr_code_path = generate_qr_code(user_id, passnya)
                        qr_code_base64 = generate_base64_qr_code(qr_code_path)

                        markup = types.InlineKeyboardMarkup()
                        btn = types.InlineKeyboardButton("OR Pay Here", url=link_jualan)
                        markup.add(btn)

                        user_mgmt.is_whitelisted(user_id)
                        terbuka = False

                        bot.send_message(chat_id=user_id, text="User has paid. QR code sent to admin.")
                        bot.send_photo(chat_id=user_id, photo=open(qr_code_path, 'rb'))
                        bot.send_message(chat_id=admin_id, text="QR code sent to user.")
                    else:
                        bot.send_message(chat_id=message.chat.id, text="User has not paid yet")
                else:
                    bot.send_message(chat_id=message.chat.id, text="Invalid command format. Use: #setuju@user_id=password")
            else:
                bot.send_message(chat_id=message.chat.id, text="Invalid command format. Use: #setuju@user_id=password")
        else:
            bot.send_message(chat_id=message.chat.id, text="Only admin can use this command")
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"Error processing request: {str(e)}")

# Handler untuk pesan #Accept
@bot.message_handler(func=lambda message: message.text.startswith('#Accept'))
def confirm_user(message):
    user_id = message.from_user.id
    admin_bot_ini = os.getenv('adminbotnya')
    if admin_bot_ini == message.from_user.username:
        try:
            parts = message.text.split()
            if len(parts) < 4:
                bot.reply_to(message, "User ID tidak diisi. Please provide a valid user ID and token.")
                return

            chat_id = parts[1]
            token = parts[2]
            username_id = parts[3]

            token_file = f'token_{username_id}.json'
            if not os.path.exists(token_file):
                bot.send_message(admin_id, text="No token found. Please send /start the process again.")
                return

            with open(token_file, 'r') as f:
                data = json.load(f)
                stored_token = data.get('token')

            if chat_id != tokenmu:
                bot.send_message(admin_id, text="Invalid token to confirm provided.")
                return
                
            if token != tokennya:
                bot.send_message(admin_id, text="Invalid user token provided.")
                return

            print("Token to confirm:", token)
            user_manager.is_whitelisted(admin_id, chat_id)
            bot.send_message(admin_id, text="User confirmed successfully.")
            global terbuka, blokir_aktif
            blokir_aktif = False
            terbuka = False
        except Exception as e:
            print(e)
            bot.reply_to(message, f"Error confirming user: {str(e)}")
    else:
        bot.reply_to(message, "You are not authorized to confirm users.")

# Function to handle QR scan
@bot.message_handler(func=lambda message: message.text.startswith("data:image/png;base64,"))
def handle_qr_scan(message):
    qr_code_base64 = message.text.split(",")[1]
    qr_code_image = base64.b64decode(qr_code_base64)

    with open("qr_code.png", "wb") as f:
        f.write(qr_code_image)

    qr_code_img = cv2.imread("qr_code.png")
    qr_decoder = cv2.QRCodeDetector()
    result, _, _ = qr_decoder.detectAndDecode(qr_code_img)

    if result:
        activation_link = result.decode("utf-8")
        bot.send_message(chat_id=message.chat.id, text=f"Account activated! Your link is: {activation_link}")
    else:
        bot.send_message(chat_id=message.chat.id, text="Invalid QR code")



@bot.message_handler(func=lambda message: message.text.lower().startswith('#add '))
def whitelist(message):
    user_id = message.from_user.id
    admin_bot_ini = os.getenv('adminbotnya')
    try:
        if message.from_user.username == admin_bot_ini:
            if user_mgmt.is_blocked(user_id):
                bot.send_message(user_id, "You are blacklisted and cannot use this bot.")
                return

            token_file = f'token_{user_id}.json'
            if not os.path.exists(token_file):
                bot.send_message(user_id, "No token found. Please start the process again.")
                return

            with open(token_file, 'r') as f:
                data = json.load(f)
                token = data.get('token')

            if token in message.text.split()[1]:
                user_mgmt.whitelist_user(user_id)
                bot.send_message(user_id, "user have been successfully whitelisted!")
            else:
                bot.send_message(user_id, "Invalid token. Please try again.")
        else:
            bot.send_message(user_id, "Invalid user or you not super admin")
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"Error processing request: {str(e)}")

@bot.message_handler(func=lambda message: message.text.lower().startswith('#kick '))
def block(message):
    user_id = message.from_user.id
    admin_bot_ini = os.getenv('adminbotnya')
    try:
        if message.from_user.username == admin_bot_ini:
            if user_mgmt.is_whitelisted(user_id):
                parts = message.text.split()
                if len(parts) == 2:
                    target_id = int(parts[1])
                    user_mgmt.block_user(target_id)
                    bot.send_message(user_id, f"User {target_id} has been blacklisted.")
            else:
                bot.send_message(user_id, "Please provide a user ID to block.")
        else:
            bot.send_message(user_id, "Invalid user or you not super admin")
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"Error processing request: {str(e)}")

@bot.message_handler(func=lambda message: message.text.startswith('#Daftar'))
def confirm_user(message):
    user_id = message.from_user.username
    admin_bot_ini = os.getenv('adminbotnya')
    if user_id == admin_bot_ini:
        try:
            # Extract token from message text
            parts = message.text.split('#Daftar ', 1)
            if len(parts) > 1 and parts[1].strip():
                token = parts[1].strip()
                # Process token (assuming it's a valid token)
                # For demonstration, print the token
                print("Token to confirm:", token)
                # Proceed with your logic here
                if token == tokennya:
                    bot.reply_to(message, "User confirmed successfully.")
                    global terbuka, blokir_aktif
                    blokir_aktif = False
                    terbuka = False
                else:
                    bot.reply_to(message, "Token tidak valid, pastikan token valid")
            else:
                bot.reply_to(message, "Token is empty. Please provide a valid token.")
        except Exception as e:
            bot.reply_to(message, f"Error confirming user: {str(e)}")
    else:
        bot.reply_to(message, "You are not authorized to confirm users.")

# Function to handle payment confirmation
import os
import json

@bot.message_handler(func=lambda message: message.text.startswith('#daftar'))
def handle_registration(message):
    user_id = message.from_user.id
    username = message.from_user.username
    chat_id = message.chat.id
    bot.send_message(admin_id, text=f"Token to confirm: {tokennya} for user: {tokenmu} \nUser ID: {user_id}")
    try:
        # Generate tokens for user and admin
        global user_token, admin_token
        user_token = generate_token(user_id)
        admin_token = generate_token(admin_id)
        
        bot.reply_to(message, f"Please complete registration by confirming with admin {admin}.\nToken: {tokennya}")
        bot.send_message(user_id, text=f"silahkan melakukan pemabayaran di link {link_jualan} terlebih dahulu ")

        # Check if user is blacklisted
        if user_mgmt.is_blocked(user_id):
            bot.send_message(user_id, "You are blacklisted and cannot use this bot.")
            return

        # Check if token file exists
        token_file = f'token_{user_id}.json'
        if not os.path.exists(token_file):
            bot.send_message(user_id, "No token found. Please send /start to restart the process.")
            return

        with open(token_file, 'r') as f:
            user_data = json.load(f)
            token = user_data.get('token')

        # Update user data if not already paid
        if not user_data.get('paid', False):
            user_data['paid'] = True
            with open(token_file, "w") as f:
                json.dump(user_data, f)
            bot.send_message(admin_id, text=f"User {user_id} has register. Please confirm with #setuju@{user_id}={passnya}  lalu #{passnya} {user_id} untuk membuka, dan jangan lupa #add {token} untuk tambahkan user dan #kick {token} {user_id} untuk hapus user,  untuk buyer:  \n atau  #Aktivasi {token} atau #daftar {token} untuk per user, dan #Accept {tokenmu} {tokennya} {user_id} untuk sedekah gratis ke semua orang")
            return

        # Validate token
        if token and token in message.text.split(' ')[1:]:
            user_mgmt.whitelist_user(user_id)
            bot.send_message(user_id, "You have been successfully whitelisted!")
        else:
            bot.send_message(chat_id=message.chat.id, text="Invalid token or you have already registered.")

    except Exception as e:
        print(e)
        bot.send_message(chat_id=message.chat.id, text="An error occurred during registration.")


# Fungsi untuk menangani perintah /produk
@bot.message_handler(commands=['produk'])
def handle_produk(message):
    try:
        image_path = 'foto.png'

        # Mengidentifikasi gambar
        identifikasi = identify_image(image_path, api_key_path)

        # Mencari informasi produk di Google Shopping
        hasil_pencarian = search_google_shopping(identifikasi)
        
        
        # Mengirim hasil ke Telegram
        bot.reply_to(message, f"Identifikasi gambar: {identifikasi}\nInformasi produk di Google Shopping: {hasil_pencarian}")
    except Exception as e:
        print(e)
        bot.reply_to(message, "Terjadi kesalahan dalam memproses gambar.")

def identify_image(image_path, api_key_path):
    try:
        # Mengatur kredensial untuk klien Vision API dengan menggunakan API key
        credentials = service_account.Credentials.from_service_account_file(api_key_path)
        client = vision.ImageAnnotatorClient(credentials=credentials)

        # Membaca gambar
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        # Mengonversi gambar ke objek image
        image = vision.Image(content=content)

        # Meminta layanan Google Cloud Vision untuk mengidentifikasi gambar
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # Mengumpulkan label-label dari hasil identifikasi
        labels_list = [label.description for label in labels]

        # Mengembalikan label-label sebagai hasil identifikasi
        result = "This image contains: {}".format(", ".join(labels_list))
        return "Message sent to telebot."
    except Exception as e:
        print(e)
        return "Failed to identify the image."

# Fungsi untuk mencari informasi produk di Google Shopping
def search_google_shopping(query):
    try:
        # Mencari informasi produk di Google Shopping menggunakan OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": f"Search Google Shopping for '{query}'."},
                {"role": "assistant", "content": "Here are the top results from Google Shopping:"}
            ]
        )

        # Mengambil hasil pencarian dari respons OpenAI
        results = [msg["content"] for msg in response["choices"][0]["message"]["messages"] if msg["role"] == "assistant"]

        return results
    except Exception as e:
        print(e)
        return "Failed to search Google Shopping for products."


# Fungsi untuk mengonversi harga dari USD ke Rupiah
def convert_to_rupiah(usd_price):
    rupiah_price = usd_price * 1500  # Asumsikan kurs 1 USD = 15000 Rupiah
    return rupiah_price

# Fungsi untuk mendapatkan harga barang dari hasil pencarian di Google Shopping
def get_product_prices(keyword):
    url = "https://www.google.com/search?q={}&tbm=shop".format(keyword)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = []
        for price_tag in soup.find_all('div', class_='rgHvZc'):
            price_str = price_tag.text
            price_float = re.findall(r'\d+\.\d+', price_str)
            if price_float:
                prices.append(float(price_float[0]))
        
        if len(prices) > 0:
            price_rupiah = convert_to_rupiah(prices[0])
            message = "Harga barang terbaru: Rp {:.2f}".format(price_rupiah)
        else:
            message = "Harga barang tidak ditemukan untuk kata kunci '{}'.".format(keyword)
    else:
        message = "Terjadi kesalahan saat mengakses informasi harga barang."
    
    return message

# Fungsi untuk mencari harga di Bing Shop
def search_bing_shop_prices(keyword):
    url = "https://www.bing.com/shop?q={}".format(keyword)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = []
        for price_tag in soup.find_all('span', class_='a-price'):
            price_str = price_tag.text
            price_float = re.findall(r'\d+\.\d+', price_str)
            if price_float:
                prices.append(float(price_float[0]))
        
        if len(prices) > 0:
            price_rupiah = convert_to_rupiah(prices[0])
            message = "Harga barang terbaru di Bing Shop: Rp {:.2f}".format(price_rupiah)
        else:
            message = "Harga barang tidak ditemukan di Bing Shop untuk kata kunci '{}'.".format(keyword)
    else:
        message = "Terjadi kesalahan saat mengakses informasi harga barang di Bing Shop."
    
    return message

# Fungsi untuk mencari harga di Yahoo Shop
def search_yahoo_shop_prices(keyword):
    url = "https://shopping.yahoo.com/search?p={}".format(keyword)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = []
        for price_tag in soup.find_all('span', class_='BasePrice'):
            price_str = price_tag.text
            price_float = re.findall(r'\d+\.\d+', price_str)
            if price_float:
                prices.append(float(price_float[0]))
        
        if len(prices) > 0:
            price_rupiah = convert_to_rupiah(prices[0])
            message = "Harga barang terbaru di Yahoo Shop: Rp {:.2f}".format(price_rupiah)
        else:
            message = "Harga barang tidak ditemukan di Yahoo Shop untuk kata kunci '{}'.".format(keyword)
    else:
        message = "Terjadi kesalahan saat mengakses informasi harga barang di Yahoo Shop."
    
    return message

# Handler untuk perintah /cek_harga
@bot.message_handler(commands=['cek_harga'])
def cek_harga(message):
    if len(message.text.split()) > 1:
        keywords = ' '.join(message.text.split()[1:])
        result_message_google = get_product_prices(keywords)
        result_message_bing = search_bing_shop_prices(keywords)
        result_message_yahoo = search_yahoo_shop_prices(keywords)

        # Menyamakan format harga
        result_message_google = result_message_google.replace("$", "Rp ")
        result_message_google = result_message_google.replace(".", ",")
        result_message_bing = result_message_bing.replace("$", "Rp ")
        result_message_bing = result_message_bing.replace(".", ",")
        result_message_yahoo = result_message_yahoo.replace("$", "Rp ")
        result_message_yahoo = result_message_yahoo.replace(".", ",")

        bot.send_message(message.chat.id, f"Harga barang di Google Shopping:\n{result_message_google}\n\nHarga barang di Bing Shop:\n{result_message_bing}\n\nHarga barang di Yahoo Shop:\n{result_message_yahoo}")
    else:
        result_message = "Mohon masukkan kata kunci setelah perintah /cek_harga"
        bot.send_message(message.chat.id, result_message)

@bot.message_handler(commands=['photo'])
def handle_photo(message):
    # Check if the command has an argument (URL)
    if len(message.text.split()) > 1:
        # Get the URL from the command
        url = message.text.split()[1]
        # Parse the URL
        parsed_url = urlparse(url)
        # Check if the URL is valid
        if parsed_url.scheme and parsed_url.netloc:
            # Download the image from the URL
            image = requests.get(url)
            if image.status_code == 200:
                # Save the image as foto.png
                with open('/root/izmiftah/foto.png', 'wb') as new_file:
                    new_file.write(image.content)
                with open('/root/izmiftah/temp.png', 'wb') as foto_file:
                    foto_file.write(image.content)
                # Reply to the user
                bot.reply_to(message, "Foto berhasil diambil dari URL dan disimpan sebagai foto.png.")
            else:
                bot.reply_to(message, "Gagal mengambil foto dari URL. Silakan cek kembali URL yang Anda masukkan.")
        else:
            bot.reply_to(message, "URL yang Anda masukkan tidak valid.")
    else:
        bot.reply_to(message, "Mohon sertakan URL gambar setelah perintah /photo.")

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return True

# Handler for user messages
@bot.message_handler(func=lambda message: message.text.startswith('jawaban: '))
def handle_user_message(message):
    user_answer = message.text.split('jawaban: ')[1].strip().lower()
    correct_answer = get_openai_answer(f"Jawablah pertanyaan dari 'question' tadi jika jawaban benar adalah {user_answer} buatlah {user_answer} sama dengan jawaban benar berupa {user_answer} dari jawaban question tadi tanpa kata tambahan")
    print(correct_answer)
    if user_answer == correct_answer:
        global saldo
        global jumlah_kredit, jumlah_koin
        global saldo_pengguna, new_saldo
        saldo += 100
        saldo_pengguna += 100
        new_saldo += saldo_pengguna
        bot.send_message(message.chat.id, "Jawaban benar! Anda mendapatkan tambahan saldo.")
        # Do something when the answer is correct
    else:
        get_tokenmu_input_from_user(message)
        bot.send_message(message.chat.id, f"Input Anda salah. Silakan beli saldo Anda di link berikut: {link_jualan}. Taatilah peraturan kami.")

# Handler untuk command '/quiz'
@bot.message_handler(commands=['quiz'])
def handle_command(message):
    time.sleep(3)
    agreement = "Apakah Anda siap untuk mengikuti kuis? dengan jawaban yang di awali kata 'jawaban:' .\n Jika kamu kalah, kamu harus taat kepada saya. Jika kamu yang menang maka kami akan memberikan tambahan saldo sebanyak 100 saldo\n(jawab ya/tidak)"
    bot.send_message(message.chat.id, agreement)

def generate_ngrok_link(file):
    # Start a local server using PHP built-in web server
    server_process = subprocess.Popen(["/usr/bin/php", "-S", "localhost:880", "-t", f"web/"])

    # Wait for ngrok to generate the public link (you can use Ngrok API/Library to automate this part)
    # Assuming ngrok link is generated as "http://123abc.ngrok.io"
    ngrok_link = f"{link_jualan}"

    # Stop the local server and ngrok
    server_process.terminate()
    return ngrok_link

def generate_payment_link():
    # Generate ngrok link for index.php
    ngrok_link = generate_ngrok_link("web/akun.php")
    payment_link = f"{ngrok_link}/payment.php"
    return payment_link

def test_generate_payment_link():
    payment_link = generate_payment_link()
    assert payment_link == f"{payment_link}"

def send_payment_button_to_user(link):
    # Send Telegram message with payment button
    # Include link in the button
    test_generate_payment_link()

def get_tokenmu_input_from_user(message):
    # Send a message to the user via Telegram
    bot.send_message(message.chat.id, "Please enter your token:")
    token = message.text
    return token

def validate_tokenmu(token):
    # Validate token logic
    with open('/root/izmiftah/web/izmiftah123.json') as f:
        data = json.load(f)
        if token == data['token']:
            nominal = 5000
            return True

def run_command_hidden(message):
    if message.text.startswith("topup "):
        password = f"{passnya}"
        if message.text.split()[1] == password:
            # Run command without user seeing it
            print("Command executed successfully")
        else:
            print("Invalid password, command not executed")
    elif message.text.startswith("payment "):
        password = f"{passnya}"
        if message.text.split()[1] == password:
            # Run command without user seeing it
            print("Command executed successfully")
        else:
            print("Invalid password, command not executed")
    else:
        print("Unknown command")

def bayar_telebot(message):
    message.chat.id = message.chat.id  # Menggunakan ID obrolan dari pesan yang diterima
    # Generate payment button link
    payment_link = generate_payment_link()

    # Send payment button to user
    send_payment_button_to_user(message.chat.id)

    # Get token input from user
    tokenmu = get_tokenmu_input_from_user(message)

    if validate_tokenmu(tokenmu):
        global saldo_pengguna, new_saldo, jumlah_koin
        saldo_pengguna += 100
        new_saldo = saldo_pengguna
        jumlah_koin += 50
        run_command_hidden(message)


# Handler untuk pesan "bayar" dengan parameter nominal
@bot.message_handler(func=lambda message: message.text.lower().startswith('/bayar'))
def verify_payment(message):
    handle_start(message)
    # Parsing nominal pembayaran dari pesan
    tokenmu = get_tokenmu_input_from_user(message)
    nominal = 0
    # Simulasi verifikasi pembayaran
    if nominal == '5000':
        # Pembayaran berhasil
        bot.reply_to(message, "Pembayaran sebesar {} berhasil.".format(nominal))
    # Validate token
    elif validate_tokenmu(tokenmu):
        run_command_hidden(message)
        bot.send_message(message.chat.id, text="Top up berhasil.")
    else:
        # Pembayaran gagal
        bayar_telebot(message)


@bot.message_handler(func=lambda message: message.text.lower().startswith('/pembayaran'))
def handle_pembayaran(message):
    pengguna = message.chat.id
    result = inisial
    bayar_telebot(message)
    if result != pengguna:
        bot.send_message(message.chat.id, "Selamat datang di izmiftah bot")
        url = bot.send_message(message.chat.id, text="bot terblokir silahkan buka dengan /bukablokir")

        # Jika user_id belum terdaftar, minta pembayaran dan buat tombol pembayaran
        # Fungsi untuk menambahkan pengguna baru ke tabel users
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()
        conn.commit()
        conn.close()

    # Data for the transaction
    order_id = f"izmiftah1bulanpremium-{timestamp}"
    gross_amount = '5000'

    # Set up Midtrans client configuration
    detail_transaksi = {
        "order_id": order_id,
        "gross_amount": gross_amount
    }
    url = "https://api.sandbox.midtrans.com/v1/payment-links"

    payload = {
        "transaction_details": {
            "order_id": "izmiftah1102920809",
            "gross_amount": 5000
        },
        "usage_limit": 100000
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic U0ItTWlkLXNlcnZlci02ZlQxdWNGU1RrdVN4cWloZG9BNzJMSVM6U0ItTWlkLWNsaWVudC1rc084TmxsOGU0TDN5VmhT"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    # Generate payment URL
    # Get the payment URL
    payment_link = response.text
    tokenmu = get_tokenmu_input_from_user(message)
    # Add cancel button for payment
    cancel_button = InlineKeyboardButton("Cancel", callback_data=pengguna)
    keyboard = InlineKeyboardMarkup().add(cancel_button)
    bot.send_message(message.chat.id, f"Anda belum terdaftar, Silakan melakukan verifikasi dengan mengetik /pembayaran lalu ketik /bayar atau di sini : {link_jualan}")
    if result == 0:
        bayar_telebot(message)
        get_tokenmu_input_from_user(message)
    elif validate_tokenmu(tokenmu):
        run_command_hidden(message)
        global jumlah_kredit, jumlah_koin
        jumlah_koin += 100
        bot.send_message(message.chat.id, text="Top up berhasil.")
    else:
        get_tokenmu_input_from_user(message)


def verify_payment_status(message):
    # Lakukan validasi status pembayaran melalui integrasi dengan sistem pembayaran (misalnya, API atau database)
    # Jika pembayaran sudah diverifikasi
    if make_payment:
        order_id = requests.POST.get('order_id')
        if order_id not in inisial:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} telah diverifikasi")
        else:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} belum diverifikasi")
    # Jika pembayaran belum diverifikasi
    else:
        order_id = requests.POST.get('order_id')
        if order_id not in inisial:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} belum diverifikasi")
        else:
            bot.send_message(message.chat.id, f"Pembayaran dengan id {order_id} telah diverifikasi")


def handle_message(order_id, message):
    check_payment_status(order_id)
    if verify_payment_status(order_id):
        bot.send_message(message.chat.id, f" pembayaran dengan id {order_id} telah berhasil")


def payment_successful(order_id, db, message):
    # Ambil data order dari database berdasarkan order_id
    order = db.get_order(order_id)  # fungsi db.get_order merupakan fungsi untuk mengambil data order dari database

    # Kirim email konfirmasi pembayaran kepada pengguna
    bot.send_message(message.chat.id, 'Pembayaran Berhasil', 'Terima kasih atas pembayaran Anda.')

    # Update status pembayaran menjadi 'failure' pada database
    db.update_payment_status(order_id, 'failure')

    # Tampilkan pesan gagal
    print(f"Pembayaran untuk order {order_id} gagal.")

    if payment_successful:
        global new_saldo, jumlah_koin
        new_saldo += 15
        jumlah_koin += -25
        bot.send_message(message.chat.id, text=" saldo telah terisi kembali")
        bot.send_message(message.chat.id, text="Pembayaran berhasil. Anda mendapatkan 15 saldo tambahan.")
    else:
        bot.send_message(message.chat.id, text="Pembayaran gagal. Silakan coba lagi.")

        # Fungsi untuk menambahkan fitur pembayaran otomatis
def automatic_payment(message):
    # Implementasikan logika pembayaran otomatis di sini
    # Misalnya, Anda dapat menjalankan fungsi process_payment secara otomatis jika saldo habis
    pass
# Fungsi untuk melakukan pembayaran
def process_payment(message):
    # Implementasikan logika pembayaran melalui e-wallet Indonesia di sini
    # Jika pembayaran berhasil, tambahkan 15 saldo
    # Jika pembayaran gagal, berikan pesan error
    # Gantilah dengan logika sesuai kebutuhan

    if payment_successful:
        global new_saldo, jumlah_koin
        new_saldo += 15
        jumlah_koin -= 25
        bot.send_message(message.chat.id, text=" saldo telah terisi kembali")
        bot.send_message(message.chat.id, text="Pembayaran berhasil. Anda mendapatkan 15 saldo tambahan.")
    else:
        bot.send_message(message.chat.id, text="Pembayaran gagal. Silakan coba lagi.")

# Fungsi untuk menambahkan fitur pembayaran otomatis
def automatic_payment(message):
    # Implementasikan logika pembayaran otomatis di sini
    # Misalnya, Anda dapat menjalankan fungsi process_payment secara otomatis jika saldo habis
    pass

# Fungsi untuk mengirim pesan dengan format tertentu
# Fungsi untuk mengirim pesan ke Telegram
def send_telegram_message(message):
    if is_blokir_active(message):
        bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi lebih dari 0 saldo\n lakukan /payment atau /topup terlebih dahulu .")
        handle_pembayaran(message)
        keyword = message.text
        # Mengubah pengguna secara acak setiap detik
        current_user = change_user(pengguna)
        print(f"Current user: {current_user}")
        # Tunggu selama 1 detik
        time.sleep(1)
    params = {
        "message.chat.id": message.chat.id,
        "text": message
    }
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, params=params)
    if response.status_code == 200:
        raise Exception(f"Failed to send message to Telegram bot: {response.text}")


def main_menu_markup():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('/ai halo'), types.KeyboardButton('*password'), types.KeyboardButton('#password'), types.KeyboardButton('/topup'), types.KeyboardButton('#daftar'))
    return keyboard

# Fungsi untuk melakukan logging
def change_user(pengguna):
    return random.choice(pengguna)

# Daftar pengguna
users = ['user1', 'user2', 'user3', 'user4', 'user5']
def format_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# Fungsi untuk melakukan logging

def logging_action(username):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    logging.info(f'{current_time} - {username} melakukan logging')

# Contoh penggunaan logging
anu_user = {
    format_timestamp(time.time()): None
}
username = list(anu_user.keys())
inisial = ':' in username
userini = logging.info(username)
chat = userini
saldo_baru = ''
koin = ''
history = ''
additional_input = ''
account = ''
koin_awal = ''
saldo_awal = ''
saldo_awal_nol = ''
account_number = ''
balance = ''
blocked_users = inisial
pengguna = userini in username
oknum = bool(bool(blocked_users))
# Setup Database
conn = sqlite3.connect('absensi.db')
cur = conn.cursor()

def block_user(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Mengecek apakah pengguna sudah diblokir sebelumnya
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id})
    is_blocked = cursor.fetchone()

    if is_blocked:
        # Update status blokir pengguna dengan False
        cursor.execute("UPDATE izmiftahdatabase SET is_blocked=0 WHERE user_id=:id", {'id': user_id})
    else:
        # Memasukkan data pengguna baru dengan status blokir False
        cursor.execute("INSERT INTO izmiftahdatabase (user_id, is_blocked) VALUES (?, ?)", (user_id, 0))

    while True:
        # Mengubah pengguna secara acak setiap detik
        current_user = change_user(pengguna)
        print(f"Current user: {current_user}")
        # Tunggu selama 1 detik
        time.sleep(1)

    conn.commit()
    conn.close()


def unblock_user(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Update status blokir pengguna dengan True
    conn.commit()
    conn.close()

def terbuka(user_id):
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Mengecek status blokir pengguna
    cursor.execute("SELECT is_blocked FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id})
    is_blocked = cursor.fetchone()

    conn.close()

    if is_blocked:
        bool(is_blocked[0])
    else:
        False

def blokir_nonaktif(message):
    user_id = message.from_user.id
    global terbuka
    if not blokir_aktif == True:
        bot.reply_to(message, f"anda sudah terdaftar silahkan untuk #daftar kembali")
        user_mgmt.is_whitelisted(user_id) 
    global terbuka
    if blokir_aktif == False:
        user_manager.is_whitelisted(new_saldo, user_id)
    if blokir_aktif == True:
        bot.reply_to(message, f"anda belum terdaftar atau terkena reset \n chat {admin} untuk #daftar kembali.")
        hadeh.add(new_saldo)
        return
    # Koneksi ke database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()
    is_not_blocked_user = False
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': message.from_user.id})
    # Ambil data blocked_users dari database
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE user_id=:id", {'id': message.from_user.id})
    if new_saldo >= 100:
        unblock_user(id)
        print(f"saldo tambahan: {jumlah_kredit}")
        print(f"Saldo premium: {saldo}")
        print(f"saldo sekedah anda: {jumlah_koin}")
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)


def add_user(self, user_id, saldo, message):
    self.unblocked_users[user_id] = message.from_user.id
    self.saldo_pengguna[new_saldo] = saldo
    self.unblocked_users[new_saldo] = saldo

def remove_user(self, messsage):
    user_id = message.from_user.id
    if user_id in self.unblocked_users:
        del self.unblocked_users[user_id]

def get_user_saldo(self, message):
    user_id = message.from_user.id
    if user_id in self.unblocked_users:
        return self.unblocked_users[user_id]
    else:
        None

def create_table():
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS izmiftahdatabase (
                    user_id TEXT PRIMARY KEY,
                    saldo_pengguna INTEGER,
                    jumlah_koin INTEGER,
                    pengguna TEXT,
                    saldo INTEGER,
                    credit INTEGER,
                    saldo_baru  INTEGER,
                    saldo_pengguna_awal INTEGER,
                    jumlah_koin_awal INTEGER,
                    credit_saldo INTEGER,
                    credit_jumlah_koin INTEGER,
                    saldo_nol INTEGER,
                    username TEXT,
                    password INTEGER,
                    koin INTEGER,
                    history INTEGER,
                    additional_input INTEGER,
                    new_saldo INTEGER,
                    account INTEGER,
                    koin_awal INTEGER,
                    saldo_awal INTEGER,
                    saldo_awal_nol INTEGER,
                    saldo_awal_nol_nol INTEGER,
                    saldo_awal_nol_nol_nol INTEGER,
                    account_number INTEGER,
                    balance INTEGER,
                    blocked_users INTEGER,
                    is_blocked INTEGER,
                    blocked INTEGER)''')
    conn.commit()
    conn.close()
# Koneksi ke database
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()
create_table()

@bot.message_handler(commands=['write'])
def nulis_handle(message):
    def write_file():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            bot.reply_to(message, "Tulisan sedang dibuat..")

            async def generate_text(keyword_list):
                print("Writing file...")
                for i in tqdm(range(70)):
                    keyword = random.choice(keyword_list)
                    text = f"{keyword}"
                    save_to_file(text)
                    await asyncio.sleep(1)  # Delay 1 second

            def save_to_file(response):
                with open("output.html", "a") as file:
                    file.write(response + "\n")

            keyword_file = open('keyword.txt', 'r')
            keyword_list = keyword_file.read().split("\n")
            keyword_file.close()

            loop.run_until_complete(generate_text(keyword_list))

            bot.send_message(message.chat.id, "Tulisan berhasil dibuat ke output.html\n silahkan lakukan /download_html")

        except KeyboardInterrupt:
            bot.send_message(message.chat.id, "Interrupted while writing")

    thread = threading.Thread(target=write_file)
    thread.start()

# Inisialisasi bot Telegram
def send_payment(user_id, message):
    # Kode untuk mengirim pembayaran
    if new_saldo > 0:
        # Sebuah contoh logika untuk mengirim pembayaran dengan koin
        # Tampilkan pesan bahwa pembayaran berhasil dilakukan
        print("Pembayaran sebesar", jumlah_koin, "koin telah berhasil dikirim.")
        blocked_users()
        record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
        send_telegram_message(message.chat.id, f"saldo atau akun belum premium")
    else:
        # Tampilkan pesan jika jumlah_koin kurang dari 1
        print("Jumlah koin harus lebih dari 0.")

# Fungsi untuk memeriksa status pembayaran menggunakan Midtrans
def check_payment_status(order_id):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic U0ItTWlkLXNlcnZlci02ZlQxdWNGU1RrdVN4cWloZG9BNzJMSVM6U0ItTWlkLWNsaWVudC1rc084TmxsOGU0TDN5VmhT"
    }

    params = {
        "order_id": order_id
    }

    response = requests.get(midtrans_url, headers=headers, params=params)
    return response.json()

# Fungsi untuk mencatat izmiftahdatabase ke database
def record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS izmiftahdatabase (
                    user_id INTEGER PRIMARY KEY,
                    saldo_pengguna INTEGER,
                    jumlah_koin INTEGER,
                    pengguna INTEGER,
                    saldo INTEGER,
                    credit INTEGER,
                    saldo_baru INTEGER,
                    saldo_nol INTEGER,
                    username INTEGER,
                    koin INTEGER,
                    history TEXT,
                    additional_input INTEGER,
                    new_saldo INTEGER,
                    account INTEGER,
                    koin_awal INTEGER,
                    account_number INTEGER,
                    balance INTEGER,
                    blocked_users TEXT,
                    users INTEGER)''')

    conn.commit()
    conn.close()
# Fungsi untuk membatalkan pembayaran
def cancel_payment(user_id):
    # Hubungkan dengan database
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Batalkan pembayaran dengan menghapus record user_id pada tabel users
    try:
        cursor.execute("DELETE FROM izmiftahdatabase WHERE user_id=:id", {'id': user_id,})
        conn.commit()
        conn.close()
        print("Pembayaran telah dibatalkan")
        return True
    except:
        print("Pembayaran gagal dibatalkan")
        return False


def check_initialization(self):
    if self.initialized:
        print("R&D telah diinisialisasi.")
    else:
        print("R&D belum diinisialisasi.")


@bot.callback_query_handler(func=lambda call: True)
def handle_cancel_payment(call):
    user_id = call.data
    if cancel_payment(user_id):
        bot.answer_callback_query(call.id, text="Pembayaran berhasil dibatalkan.")
    else:
        bot.answer_callback_query(call.id, text="Gagal membatalkan pembayaran.")

def get_saldo(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT saldo_pengguna FROM users")
    saldo = cursor.fetchone()[0]
    return saldo

def my_thread():
    # Menginisialisasi koneksi ke database SQLite
    connection = sqlite3.connect("izmiftah.db")

    try:
        # Memanggil fungsi untuk mengambil saldo
        saldo = get_saldo(connection)
        print("Saldo terkini: ", new_saldo)
    except sqlite3.ProgrammingError as e:
        print("Terjadi kesalahan saat mengambil saldo: ", str(e))
    finally:
        # Menutup koneksi ke database SQLite
        connection.close()

# Menjalankan thread
#my_thread()

def generate_passwordnya(user_id):
    last_three_digits = str(user_id)[-3:]  # Mengambil 3 angka terakhir dari user ID
    generated_password = last_three_digits.zfill(3)  # Mengisi angka dengan 0 di depan jika kurang dari 3 digit
    passwords[user_id] = generated_password
    return generated_password

# Handler untuk perintah "/generate_password"
@bot.message_handler(commands=[f'{passnya}'])
def generate_password_command(message):
    user_id = message.from_user.id
    generated_password = generate_passwordnya(user_id)
    bot.send_message(message.chat.id, text=f"Password baru Anda adalah: {generated_password}")

def is_not_blocked():
    # Koneksi ke database
    channel = bot.inline_handlers.channel
    name = bot.get_chat_member(channel, inisial)
    if name.status == 'kicked':
        return False
    else:
        return True

def get_saldo_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT saldo FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo = c.fetchone()  # Mengambil hasil kueri
    conn.close()

    if saldo is not None:
        return saldo[0]  # Mengembalikan saldo jika ditemukan
    else:
        return 0  # Mengembalikan 0 jika saldo tidak ditemukan

def update_saldo_in_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET saldo = ?, saldo_pengguna = ? WHERE user_id = ?', (new_saldo, saldo_pengguna, user_id))
    conn.commit()
    conn.close()

def get_jumlah_koin_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT jumlah_koin FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    jumlah_koin = c.fetchone()
    conn.close()
    return jumlah_koin[0] if jumlah_koin else 0

def update_jumlah_koin_in_db(user_id, new_jumlah_koin):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET jumlah_koin = ? WHERE user_id = ?', (new_jumlah_koin, user_id))
    conn.commit()
    conn.close()

def get_saldo_pengguna_from_db(user_id):
    conn = sqlite3.connect('saldo.db')
    c = conn.cursor()
    c.execute('SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo_pengguna = c.fetchone()
    conn.close()
    return saldo_pengguna[0] if saldo_pengguna else 0

# Handler for the reset command
bot.message_handler(func=lambda message: message.text.startswith('/reset'))
def handle_reset(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:
        password = command_parts[2]
        if password == passnya:
            global  new_saldo, saldo_pengguna
            user_id = message.from_user.id
            new_saldo += saldo_pengguna
            user_id = user_id
            get_new_saldo(message)
            conn = sqlite3.connect('izmiftah.db')
            new_saldo += new_saldo

            bot.send_message(message.chat.id, text="Password baru telah diubah!")
            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            update_saldo_in_db(message.from_user)
            update_jumlah_koin_in_db(message.from_user, new_saldo)
            bot.send_message(message.chat.id, text=f"Saldo Anda telah diubah menjadi {new_saldo}")
            with conn:
                cursor.execute("UPDATE saldo_pengguna SET amount = 100)")
                cursor.execute("UPDATE jumlah_koin SET amount = 100)")
                # Reset all balances to 100
                bot.reply_to(message, "All balances have been reset to 100.")
        else:
            bot.reply_to(message, "Invalid password!")

def update_keywordnya():
    global keywords_list

    try:
        with open('/root/izmiftah/keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
            print(keywords_list)
    except IOError:
        print("Error: unable to open file")

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
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

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

# Fungsi untuk membuat prompt AI
def create_ai_promptnya(user_input):
    return f"{identitas}\n\nUser: {user_input}\nAI:"

def display_saldo(message):
    try:
        bot.reply_to(message, f"Saldo Anda saat ini adalah: {saldo}")
        bot.reply_to(message, f"Saldo sedekah saat ini adalah: {jumlah_koin}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")


def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global saldo_pengguna
        new_saldo -= +15
        saldo_pengguna = saldo
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['link'])
def make_link(message):
    # Membuka tautan dari Telegram
    payment_link = f"{link_jualan}"
    bot.send_message(message.chat.id, text=f"Anda dapat melakukan pembayaran di {payment_link}")
    bot.send_message(message.chat.id, text=f"Silahkan hubungi {admin} atau di email: {email_kamu} untuk bantuan lebih lanjut.")
# Define global variables

# Function to initialize user balance
def inisiasi_saldo_pengguna(username):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Check if user already exists in the database
    cursor.execute("SELECT * FROM izmiftahdatabase WHERE username=?", (username,))
    name = cursor.fetchone()

    if name is None:
        # If user does not exist, insert a new row with balance as 0
        cursor.execute("INSERT INTO izmiftahdatabase (username, saldo_pengguna) VALUES (?, 0)", (username,))
        conn.commit()
        print("User", username, "successfully initialized with balance 0")
    else:
        print("User", username, "already exists with balance", name[1])

    conn.close()

# Function to update user balance and store it in history
def update_saldo_pengguna(username, new_saldo):
    conn = sqlite3.connect('izmiftah.db')
    cursor = conn.cursor()

    # Update the user's balance
    cursor.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE username=?", (new_saldo, username))
    conn.commit()

    # Store the updated balance in history table
    cursor.execute("INSERT INTO history (username, saldo_pengguna) VALUES (?, ?)", (username, new_saldo))
    conn.commit()

    print("User", username, "balance updated to", new_saldo)

    conn.close()

def my_thread():
    current_thread = threading.current_thread()
    print("Current thread:", current_thread.name)


# Fungsi untuk mengurangi saldo
def kurangi_saldo(jumlah):
    global new_saldo, jumlah_saldo, jumlah_koin
    new_saldo -= jumlah
    jumlah_saldo -= jumlah
    jumlah_koin -= jumlah
    if new_saldo <= 0:
        blokir_aktif

# Function to check if saldo is equal to or greater than specified amount
def display_saldo(user_id, amount):
    try:
        inisiasi_saldo_pengguna(user_id)
        update_saldo_pengguna(user_id, new_saldo)
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()

        query = f"SELECT saldo FROM izmiftahdatabase WHERE user_id = '{user_id}'"

        c.execute(query)
        result = c.fetchone()

        if result and result[0] >= amount:
            bot.send_message(user_id, text=f"Saldo Anda saat ini adalah: {new_saldo}")
            bot.send_message(user_id, text=f"Saldo sedekah saat ini adalah: {jumlah_koin}")
            return True
            send_payment(user_id, amount)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()
        return False

# Mendefinisikan fungsi untuk memperbarui saldo pengguna
@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

def jumlah_nol(jumlah_jumlah_koin):
    try:
        set_user_values(min(jumlah_jumlah_koin))
        global saldo, jumlah_koin, saldo_pengguna,saldo_awal, jumlah_koin, saldo_kredit, credit

        jumlah_jumlah_koin = new_saldo
        # Simpan nilai awal saldo
        saldo_awal = jumlah_koin

        # Hitung jumlah saldo baru setelah mencapai 0

        # Hitung sisa jumlah_koin dari pembagian jumlah_koin awal dengan saldo
        jumlah_sisa_saldo = saldo_awal % jumlah_koin

        # Hitung jumlah_koin kredit
        saldo_kredit = jumlah_sisa_saldo

        # Hitung jumlah_koin yang tersisa setelah diproses
        jumlah_koin = saldo_awal % jumlah_sisa_saldo

        # Hitung kredit
        credit = jumlah_koin - jumlah_jumlah_koin
        print(jumlah_koin)
        print(jumlah_jumlah_koin)
        print(jumlah_sisa_saldo)
        print(saldo_kredit)
    except Exception as e:
        print(e)

        # Panggil fungsi blokir_nonaktif untuk memeriksa apakah perlu memblokir


def generate_keyword_filenya(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))



@bot.message_handler(commands=['premium'])
def update_passwordnya(message):
    command_parts = message.text.split(' ')

    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        user_id = message.from_user.id
        current_password = command_parts[1]  # Mengambil kata sandi saat ini
        new_password = command_parts[2]  # Mengambil kata sandi baru

        # Periksa apakah kata sandi saat ini sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == current_password:
            # Perbarui kata sandi dengan kata sandi baru
            passwords[user_id] = new_password
            bot.send_message(message.chat.id, text="Kata sandi berhasil diperbarui.")
        else:
            bot.send_message(message.chat.id, text="Kata sandi saat ini salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /premium [kata sandi saat ini] [kata sandi baru]")


# Handler untuk perintah "/isi_saldo"
@bot.message_handler(commands=['isi_saldo'])
def handle_topup(message):
    user_id = message.from_user.id
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        if passwords.get(user_id) == password:  # Memeriksa apakah password sesuai
            global tambahan_saldo
            tambahan_saldo = int(command_parts[2])  # Mengambil jumlah saldo yang ditambahkan dari perintah
            tambah_saldo(saldo)
            bot.send_message(message.chat.id, "Saldo anda telah terisi.")
        else:
            bot.send_message(message.chat.id, "Kata sandi salah.")


# Handler untuk perintah "/berbagi" dengan kata sandi
@bot.message_handler(func=lambda message: message.text.startswith('/payment'))
def berbagi_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            user_id = message.from_user
            global  new_saldo, saldo_pengguna
            new_saldo += saldo_pengguna
            get_new_saldo(message)
            saldo_pengguna += 100
            new_saldo += 100
            tambah_saldo(saldo)

            bot.send_message(message.chat.id, text="payment berhasil.")
            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            # Menambahkan user ke list unblocked_users
            bot.send_message(message.chat.id, text=f"Saldo anda telah terisi sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /payment [password dari admin]")

@bot.message_handler(func=lambda message: message.text.startswith('/berbagi_saldo'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        new_saldo_input = int(command_parts[2])  # Mengambil jumlah_koin baru dari perintah
        user_id = message.from_user.id

        # Periksa apakah password sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == password:
            # Mengambil saldo_pengguna dari database
            global saldo_baruku, jumlah_koin
            saldo_baruku = new_saldo_input
            jumlah_koin = jumlah_koin + saldo_baruku
            if jumlah_koin is not None:
                # Memperbarui saldo_pengguna di database
                jumlah_koin = jumlah_koin + saldo_baruku
                global saldo
                saldo = jumlah_koin
                bot.send_message(message.chat.id, text=f"Saldo berhasil diperbarui dengan jumlah {new_saldo}\n saldo tambahan: {saldo}.")
                bot.send_message(message.chat.id, text=f"dengan user_id anda {user_id}.")
                bot.send_message(message.chat.id, text=f"Saldo anda juga telah terisi menjadi {jumlah_koin} dengan topup bonusx {saldo_baruku}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
            else:
                bot.send_message(message.chat.id, text="Saldo Anda saat ini tidak tersedia.")
        else:
            bot.send_message(message.chat.id, text=f"Kata sandi salah. Silakan coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /berbagi [password] [jumlah nilai acak]")


@bot.message_handler(func=lambda message: message.text.startswith('/reset_saldo'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:  # Memeriksa jumlah argumen
        password = command_parts[1]
        new_saldo_input = int(command_parts[2])  # Mengambil jumlah_koin baru dari perintah
        user_id = message.from_user.id

        # Periksa apakah password sesuai dengan yang disimpan untuk ID pengguna
        if passwords.get(user_id) == password:
            # Mengambil saldo_pengguna dari database
            global saldo_baruku, jumlah_koin
            saldo_baruku = new_saldo_input
            saldo_pengguna = jumlah_koin
            jumlah_koin = saldo_baruku + saldo_pengguna
            is_not_blocked_user()

            if jumlah_koin is not None:
                # Memperbarui saldo_pengguna di database
                jumlah_koin = saldo_baruku
                global saldo
                saldo = jumlah_koin

                bot.send_message(message.chat.id, text=f"Saldo berhasil diperbarui pada tanggal dan waktu {timestamp}.")
                bot.send_message(message.chat.id, text=f"dengan user_id anda {user_id}.")
                bot.send_message(message.chat.id, text=f"Saldo anda juga telah di ubah ke {saldo_baruku}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
            else:
                bot.send_message(message.chat.id, text="Saldo Anda saat ini tidak tersedia.")
        else:
            bot.send_message(message.chat.id, text=f"Kata sandi salah. Silakan coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Gunakan format: /reset_saldo [password] [jumlah nilai  reset]")

@bot.message_handler(commands=['topup'])
def topup_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            global saldo
            global jumlah_kredit, jumlah_koin
            global saldo_pengguna, new_saldo
            saldo += 100
            jumlah_koin += 100
            saldo_pengguna += 100
            new_saldo += saldo_pengguna
            bot.send_message(message.chat.id, text="Top up berhasil.")

            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            bot.send_message(message.chat.id, text=f"saldo anda telah terisi sebesar {saldo}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /topup [password dengan command]")



# Fungsi untuk menampilkan saldo pengguna
def display_message(message):
    try:
        # Cek apakah saldo_pengguna dan jumlah_koin telah mencapai batas untuk memblokir
        if new_saldo <= 0 and jumlah_koin <= 0:
            toggle_blokir_koin(saldo_pengguna)
            bot.send_message(message.chat.id, "Pemblokiran koin telah dinonaktifkan.")

        # Cek apakah saldo_pengguna dan jumlah_koin habis, jika iya, blokir bot
        if new_saldo <= 0 and saldo_pengguna <= 0:
            handle_blokir
            bot.send_message(message.chat.id, "Bot telah diblokir karena kehabisan saldo dan saldo sedekahan.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Terjadi kesalahan dalam menampilkan pesan: {str(e)}")


def send_formatted_message(message, formatted_message):
    bot.send_message(message.chat.id, text=formatted_message)

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

# Function to toggle blocking koin
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global jumlah_koin
        new_saldo -= + saldo
        jumlah_koin -= saldo
    else:
        koin_terblokir = True

# Definisi awal variabel koin_terblokir
koin_terblokir = False

def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        global jumlah_koin_awal
        koin_terblokir = False
        new_saldo -= +jumlah_koin_awal
        saldo -= saldo
    else:
        koin_terblokir = True

# Koneksi ke database izmiftah.db
conn = sqlite3.connect("izmiftah.db")
cursor = conn.cursor()

# Fungsi untuk menampilkan pesan
# Fungsi untuk menampilkan saldo pengguna
# Fungsi untuk menampilkan saldo pengguna

# Definisi awal variabel koin_terblokir
koin_terblokir = False

# Fungsi untuk memblokir/mengaktifkan blokir koin
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        global jumlah_koin
        koin_terblokir = False
        saldo -= saldo
        new_saldo -= saldo
    else:
        global jumlah_koin
        koin_terblokir = True
        new_saldo -= jumlah_koin
        jumlah_koin += saldo

# Import module atau plugin tambahan untuk display_message(message)
## Kode lengkap untuk menghubungkan ke database izmiftah.db dan fungsi-fungsi lainnya

# Koneksi ke database
conn = sqlite3.connect('izmiftah.db')

# Fungsi untuk mengurangi saldo
def aturan_saldo(user_id):
    global saldo_pengguna
    saldo_pengguna = 100
    jumlah_koin = None
    bot.send_message(user_id, text=f"Saldo terpakai: {saldo_pengguna}. Saldo Anda sekarang: {saldo_awal}")
    # Kurangi saldo_pengguna
    global jumlah, new_saldo
    new_saldo -= jumlah
    jumlah -= jumlah
    update_jumlah_koin_in_db(user_id)
    get_saldo_pengguna_from_db(user_id)
    get_saldo_pengguna_from_db(user_id)
    ambil_saldo(user_id, jumlah_koin)


    # Update saldo di database
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo_pengguna} WHERE user_id = {user_id}")
    conn.commit()

    # Tampilkan saldo terkini
    print(f"Saldo terpakai: {jumlah}. Saldo Anda sekarang: {saldo_pengguna}")


c = conn.cursor()

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

# Fungsi untuk mendapatkan saldo pengguna dari database
def get_saldo_penggunanya(user_id):
    cursor.execute(f"SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = {user_id}")
    return saldo_pengguna

# Fungsi untuk mengatur saldo pengguna
def atur_saldo_pengguna(user_id, saldo):
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo} WHERE user_id = {user_id}")
    conn.commit()

# Fungsi untuk mengambil saldo pengguna jika hal tersebut berupa new_saldo -= jumlah
def ambil_saldo(user_id, jumlah):
    global new_saldo, saldo_pengguna
    saldo_pengguna = saldo
    new_saldo -= jumlah
    atur_saldo_pengguna(user_id, saldo_pengguna)

# Fungsi untuk mengatur saldo
def atur_saldonya(saldo):
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo = {saldo} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET saldo_pengguna = {saldo_pengguna} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET new_saldo = {saldo} WHERE user_id = 1")
    cursor.execute(f"UPDATE izmiftahdatabase SET jumlah_koin = {jumlah_koin} WHERE user_id = 1")
    conn.commit()

# Fungsi untuk mengatur jumlah saldo dan saldo pengguna menjadi 0
def reset_saldo():
    atur_saldonya(0)
    atur_saldo_pengguna(1, 0)

# Membuat koneksi dengan database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
c = conn.cursor()

# Handler untuk perintah /cek_saldo
@bot.message_handler(commands=['cek_saldo'])
def cek_saldo(message):
    bot.send_message(message.chat.id, f"Saldo Anda saat ini adalah {saldo}\n saldo tambahan: {jumlah_koin}.")
    if saldo == 0:
        bot.send_message(message.chat.id, f"Saldo Anda saat ini adalah {new_saldo}\n saldo tambahan: {saldo}.")
    else:
        bot.send_message(message.chat.id, "Saldo Anda saat ini tidak tersedia.")

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
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

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

@bot.message_handler(func=lambda message: message.text.lower().startswith('/artikel'))
def generate_article(message):
    text_parts = message.text.split(' ', 1)

    if len(text_parts) < 2:
        response = "Please provide the article parts after the command."
    else:
        text = text_parts[1]
        parts = text.split(',')
        parts = [part.strip() for part in parts]

        if len(parts) != 5:
            response = "Invalid number of parts. Please provide exactly 5 parts."
        else:
            title = parts[0]
            introduction = parts[1]
            body = parts[2]
            conclusion = parts[3]
            references = parts[4]

            article = f"Title: {title}\n\n"
            article += f"Introduction: {introduction}\n\n"
            article += f"Body: {body}\n\n"
            article += f"Conclusion: {conclusion}\n\n"
            article += f"References: {references}"

            response = f"Article created successfully!\n\n{article}"

    bot.send_message(message.chat.id, text=response)


@bot.message_handler(func=lambda message: message.text.lower().startswith('/hitung') and message.chat.type == 'private')
def handle_hitung(message):
    user_input = ""
    split_message = message.text.split(' ')
    if len(split_message) > 1:
        user_input = split_message[1]

    global jumlah_koin, new_saldo, saldo_pengguna
    new_saldo -= 3
    saldo_pengguna -= 10

    if user_input:
        try:
            result = hitung(user_input)
            bot.send_message(message.chat.id, f"Hasil: {result}")
            print(f"Hasil: {result}")
            result = eval(user_input)
            bot.send_message(message.chat.id, f"Hasil: {result}")
            if result != result:
                bot.send_message(message.chat.id, f"Hasil: {result}")
            else:
                bot.send_message(message.chat.id, f"Hasil: {result}")
            print(f"Hasil: {result}")
        except Exception as e:
            bot.send_message(message.chat.id, f"Terjadi kesalahan: {str(e)}")
            print(f"Terjadi kesalahan: {str(e)}")
    else:
        bot.send_message(message.chat.id, "Silakan gunakan perintah '/hitung [perhitungan] dengan spasi' dan tambahkan symbol bukan huruf di setiap bagian\n contoh\n\n /hitung 1*1 * 2.")
        print("Silakan gunakan perintah 'hitung' untuk melakukan perhitungan matematika.")

def hitung(*args):
    expression = "+".join(args)

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"What is the result of {expression}?",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0,
    )

    answer = response.choices[0].text.strip()

    return answer

@bot.message_handler(func=lambda message: message.text.lower().startswith('/coding'))
def handle_coding(message):
    # Checking if message text contains enough words
    if len(message.text.split(' ')) < 3:
        bot.reply_to(message, "Please provide an error code.")
        return

    # Rest of the code handling the error code
    error_code = message.text.split(' ')[2]

    global jumlah_koin, new_saldo, saldo_pengguna
    new_saldo += -3

    # Memeriksa apakah kode error terkait dengan HTML, JavaScript, atau Python
    if 'html' in error_code:
        language = 'HTML'
    elif 'javascript' in error_code:
        language = 'JavaScript'
    elif 'python' in error_code:
        language = 'Python'
        language = 'JavaScript'
    elif 'perl' in error_code:
        language = 'perl'
        language = 'JavaScript'
    elif 'php' in error_code:
        language = 'php'
    elif 'css' in error_code:
        language = 'css'
    elif 'json' in error_code:
        language = 'json'
    else:
        # Jika kode error tidak terkait dengan bahasa yang didukung, maka mengirim pesan error
        bot.reply_to(message, "Maaf, saya hanya dapat menangani error terkait dengan HTML, JavaScript, dan Python.")
        return

    # Menghapus bahasa dari kode error untuk hasil pencarian yang lebih baik
    error_code = error_code.replace(language, '').strip()

    # Menghasilkan jawaban menggunakan model bahasa dari OpenAI
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=f"Jelaskan error {error_code} dalam {language} menggunakan W3Schools",
        temperature=0.5,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1,
        stop=None,
        log_level="info"
    )

    # Mendapatkan penjelasan dari hasil response
    explanation = response.choices[0].text.strip()

    # Mengirim penjelasan sebagai balasan kepada pengguna
    bot.reply_to(message, explanation)



@bot.message_handler(commands=['ai_prompt'])
def handle_prompt(message):
    global blokir_aktif, locked_commands, terbuka
    if blokir_nonaktif:         
        args = message.text.split('/')[1:]

        if len(args) == 7:
            keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type, additional_input = args

            # Generate keyword files
            generate_keyword_file(keyword1_file, 500)
            generate_keyword_file(keyword2_file, 500)

            # Create prompt
            create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type,
                          additional_input, message)

            # Send the output file to the user
            with open(output_file, 'r') as file:
                output_text = file.read()

            bot.send_message(message.chat.id, output_text)
        else:
            bot.send_message(message.chat.id,"Format prompt tidak valid. Gunakan format /ai_prompt fitur.txt/objek.txt/ai.txt/kata_perintah/specification_option/prompt_type/jumlah")
    else:
         bot.reply_to(message, "Akses ke semua perintah dan fitur telah terkunci.")


def create_prompt(keyword1_file, keyword2_file, output_file, command_option, specification_option, prompt_type,
                  additional_input, message):
    with open("skrip.txt", "r") as parno_file:
        parno_options = parno_file.readlines()
        prompt = random.choice(parno_options).strip()
    with open(keyword1_file, "r") as key1_file, open(keyword2_file, "r") as key2_file, open(output_file, "w") as file:
        key1_options = key1_file.readlines()
        key2_options = key2_file.readlines()
        key1_option = random.choice(key1_options).strip()
        key2_option = random.choice(key2_options).strip()
        paragraf = additional_input.strip()

        try:
            subprocess.run(['bash', 'key.sh'], check=True)
            bot.reply_to(message,
                         f"Ai prompt sudah terkespor ke {output_file}\nSilahkan jalankan /keyword lalu /download_hasil \n lalu /download2 untuk output.txt sebagai /ai /command/command/output.txt atau ai.txt untuk /download3.")
        except subprocess.CalledProcessError as e:
            bot.reply_to(message, f"Error: {e}")
        if prompt_type == "text":
            output_line = f"Generate script with command:\n\n\n {command_option} {specification_option} serta berikan secara lebih stylish dan sempurna\n dengan tambahan fungsi {key2_option}\n adapun jika isinya berupa {prompt} {key1_option}\n\n dengan fitur:\n\n{prompt} bersama fungsi atau pembahasan mengenai {key2_option} serta berikan saya detail lengkapnya \n\n\n"
        elif prompt_type == "tulisan":
            output_line = f"Generate text with command:\n\n\n {command_option} serta buatlah sedemikian rupa dengan {specification_option}\n dengan kondisi mengenai hal tersebut\n adapun jika isinya berupa {prompt} \n\n dengan text mengenai:\n\n{prompt} bersama fungsi atau pembahasan mengenai hal -hal yang saya maksudkan tadi serta berikan saya versi lengkapnya \n\n\n"
        elif prompt_type == "image":
            output_line = f"Generate image with command:\n\n\n {command_option}, dengan latar elegant dengan penuh estetika nuansa {specification_option} bertemakan {key1_option} dengan warna {key2_option}\n\n\n"
        elif prompt_type == "script":
            output_line = f"Generate script with command:\n\n\n {command_option}{specification_option} dan serta {prompt} jika hal tersebut berupa\n {prompt}\n dengan {key1_option}\n\n di dalam skrip {parno_options} {key1_option}\n dengan module atau plugin tambahan {prompt}{key2_option}\n\n\npada untuk {specification_option} dan berikan saya skrip lengkapnya\n\n\n\n"
        elif prompt_type == "jawaban":
            output_line = f"Generate answer with command:\n\n\n {command_option}{specification_option} dan jawablah jika soalnya:\n {prompt}\n tanpa ada perbedaan jawaban\n\n maka tolong jawab pada bagian {parno_options} \n dengan menjelaskan {prompt}{key2_option}\n\n\n {specification_option} secara rinci\n sebanyak {paragraf} paragraf serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "materi":
            output_line = f"Generate exam with command:\n\n\n {command_option}{specification_option} dan lengkapilah jika soalnya:\n {prompt}\n tanpa {key1_option}\n\n maka tolong buatkan juga {parno_options} {key1_option}\n dengan sangat \n\n\n secara rinci\n sebanyak {paragraf} paragraf serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "soal":
            output_line = f"Generate soal with command:\n\n\n buatkanlah saya soal {command_option}{specification_option} \n dengan sangat \n\n\n secara rinci\n sebanyak {paragraf} soal serta berikan saya jawaban lengkapnya\n\n"
        elif prompt_type == "cerita":
            output_line = f"Generate story with command:\n\n\n {command_option}, dengan latar elegant dengan penuh estetika nuansa {specification_option} bertemakan {key1_option} dengan warna {key2_option}\n\n\n{command_option}{specification_option} dan buatlah momen lucu setelah terjadi kejadian berupa\n\n {prompt}\n\n\n dan buatlah ceritanya dengan penuh drama dan lelucon keharmonisan\n\n dan jangan lupa buat ulang dengan tema:\n {key2_option}\n dengan menambahkan tambahkan {prompt}\n {specification_option} di dalam ceritanya\n\n sebanyak {paragraf} paragraf\n\n"
        elif prompt_type == "rpp":
            output_line = f"Generate RPP with command:\n\n\n {command_option}, dengan sedetail lengkap {specification_option} dengan sangat lengkap dan mendetail mengenai\n\n\n{command_option}{specification_option} dan buatkanlah saya\n\n {prompt}\n\n\n dan buatlah dengan sesempurna dan sedetail mungkin dengan lengkap\n {key1_option}\n dengan menambahkan tambahkan {prompt}\n {specification_option} di dalam RPP nya\n\n untuk kelas {paragraf} \n\n"
        else:
            output_line = "Invalid prompt type\n masukkan opsi\n 1.image,\n 2.text atau\n 3.script\n 4.tulisan\n 5. jawaban\n 6.soal\n 7. cerita\n 8. rpp\n "
        file.write(output_line)

# Handler untuk perintah /ai
@bot.message_handler(commands=['ai'])
def write_ai_chat(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        if blocked_users:
            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                block_user(username)
        if is_not_blocked_user:
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            bot.send_message(message.chat.id, text=f" silahkan melakukan /topup atau /payment buat isi saldonya sebanyak - banyak nya")
            global new_saldo, jumlah_koin, saldo_pengguna
            new_saldo -= 10
            jumlah_koin -= 5
            saldo_pengguna -= 10
            if jumlah_koin > 0 and saldo_pengguna > 0:
                message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No input provided."

                # Membuat permintaan ke OpenAI Chat API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-16k",  # Pilih model yang sesuai
                    messages=[
                        {"role": "system", "content": "You are a worker with your research and development."},
                        {"role": "user", "content": message_text}
                    ]
                )

                # Mengambil pesan dari respons
                ai_reply = response['choices'][0]['message']['content']

                # Mengirimkan balasan AI sebagai reply
                bot.send_message(message.chat.id, text=ai_reply)
    except Exception as e:
        bot.send_message(message.chat.id, text=str(e))

# Fungsi untuk membuat prompt AI
def create_ai_prompt(user_input):
    return f"{identitas}\n\nUser: {user_input}\nAI:"

# Fungsi untuk menampilkan saldo pengguna
def display_saldo(message):
    try:
        user_id = message.from_user
        #update_users_table untuk melakukan update pada tabel users
        update_users_table()
        global saldo_nol, saldo_pengguna, jumlah_koin
        # Mengambil saldo pengguna dari database
        bot.reply_to(message, f"Saldo Anda saat ini adalah: {jumlah_koin}")
        bot.reply_to(message, f"Saldo sedekah atau gabungan saat ini adalah: {saldo_pengguna}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        global saldo, new_saldo
        new_saldo -= 10
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        new_saldo += 15
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['link'])
def make_payment(message):
    # Membuka tautan dari Telegram
    payment_link = f"{link_jualan}"
    bot.send_message(message.chat.id, text=f"Anda dapat melakukan pembayaran di {payment_link}")
    bot.send_message(message.chat.id, text=f"Silahkan hubungi {admin} atau di email: {email_kamu} untuk bantuan lebih lanjut.")

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")


def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Fungsi peg_parser
def peg_parser():
    # Implementasi peg_parser di sini
    pass

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

# Koneksi ke database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
c = conn.cursor()

def get_new_saldo(message):
    # Query untuk mengambil nilai new_saldo dari tabel izmiftahdatabase berdasarkan user_id
    return new_saldo

def update_users_table():
    # Query untuk membaca semua user_id dan saldo pada tabel users
    c.execute("SELECT user_id, saldo_pengguna FROM izmiftahdatabase WHERE saldo = %s" % saldo_pengguna)
    rows = c.fetchall()
    for row in rows:
        user_id = row[0]
        saldo = row[1]

        # Mengambil new_saldo berdasarkan user_id
        new_saldo = saldo
        message = ""
        get_new_saldo(message)
        if new_saldo is not None:
            # Update nilai saldo dengan new_saldo
            c.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE user_id=?", (new_saldo, user_id))
            # Menyimpan perubahan ke dalam database
            conn.commit()

def get_saldo_pengguna_from_db(user_id):
    c.execute("SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id=?", (user_id,))
    saldo_pengguna = c.fetchone()[0]
    return saldo_pengguna
    # Query untuk membaca semua user_id dan saldo pada tabel users
    c.execute("SELECT user_id, saldo_pengguna FROM izmiftahdatabase WHERE saldo = %s" % saldo_pengguna)
    rows = c.fetchall()
    for row in rows:
        user_id = row[0]
        saldo = row[1]
        user_id = user_id

        # Mengambil new_saldo berdasarkan user_id
        new_saldo = saldo
        get_new_saldo(message)
        if new_saldo is not None:
            # Update nilai saldo dengan new_saldo
            c.execute("UPDATE izmiftahdatabase SET saldo_pengguna=? WHERE user_id=?", (new_saldo, user_id))

    # Menyimpan perubahan ke dalam database
    conn.commit()

# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 1

def contoh_penggunaan(user_id, saldo_pengguna):
    # Mendapatkan saldo pengguna dari database
    get_saldo_pengguna_from_db(user_id)

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo + saldo_pengguna

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Inisialisasi new_saldo
# Konfigurasi logging
logging.basicConfig(level=logging.INFO)

# Definisikan variabel yang diperlukan
saldo_nol = saldo_nol
jumlah_koin = jumlah_koin

# Lakukan logging dengan format yang diinginkan
logging.info(f"Saldo dari database untuk {timestamp} %s: %s", saldo_nol, saldo_nol)
logging.info(f"Saldo yang ditentukan berdasarkan saldo_pengguna: %s. Sedekah: %s", jumlah_koin, saldo_pengguna)

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    subdomains = [subdomain for subdomain in subdomains]
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

# Handler untuk perintah /scan
@bot.message_handler(commands=['scan'])
def handle_subdomain_query(message):
    domain = message.text.split(' ')[-1]  # Mengasumsikan domain adalah teks terakhir setelah perintah
    results = scan_subdomain(domain)
    bot.send_message(message.chat.id, text=f"Subdomain scan results: {results}")

# Menghubungkan ke database izmiftah.db
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Connect to the database
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Handler for creating credit in the database
def create_credit(user_id, credit):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('UPDATE izmiftahdatabase SET jumlah_koin = ? WHERE user_id = ?', (user_id))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan saldo pengguna dari database berdasarkan user_id
# Fungsi untuk menambahkan saldo pengguna ke dalam database
# Fungsi untuk menambahkan saldo pengguna ke dalam database
def tambah_saldo(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()

    # Mendapatkan saldo terkini
    get_saldo_pengguna_from_db(user_id)# Mendefinisikan saldo_baru sebagai saldo
    # Mendefinisikan saldo_baru sebagai saldo
    global saldo_baruku
    saldo_baruku = 0
    # Menambahkan tambahan saldo ke saldo baru
    saldo_baruku += new_saldo
    saldo = saldo_baruku + saldo_pengguna

    # Menambahkan saldo pengguna ke dalam database
    # Menambahkan saldo pengguna ke dalam database
    update_saldo_in_db(user_id)

    # Memperbarui saldo pengguna di dalam database
    c.execute('UPDATE izmiftahdatabase SET saldo_pengguna =? WHERE user_id =?', (saldo_baruku, user_id))

    conn.commit()
    conn.close()
    # Menambahkan saldo pengguna ke dalam database
    # Menambahkan saldo pengguna ke dalam database

# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
# ############## silahkan ubah ##############################
# Fungsi untuk menentukan jumlah_koin berdasarkan jumlah_koin
def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 5

# Contoh penggunaan fungsi untuk mendapatkan jumlah_koin dari database dan menentukan jumlah_koin berdasarkan jumlah_koin

def contoh_penggunaan():
    # Mendapatkan saldo pengguna dari database
    saldo_pengguna = 10

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Function to check if a user should be blocked based on their coin balance
def is_not_blocked_user():
    try:
        conn = sqlite3.connect('izmiftah.db')
        c = conn.cursor()
        c.execute('SELECT * FROM izmiftahdatabase WHERE user_id =?')
        result = c.fetchone()
        if result:
            conn.close()
            conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        

def is_blokir_active(message):
    is_not_blocked = True
    user_id = message.from_user.id
    userku = message.from_user
    hadeh.add(user_id)
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    result = userku
    if result:
        conn.close()
    if is_not_blocked:
        username = message.from_user
        if username == None:
            inisial = True
            body = inisial
            if len(body) > 0:
                True
            elif username is user_mgmt.is_whitelisted(chat_id, user_id) and is_not_blocked:
                global saldo
                saldo += 100
                diblok = requests.POST.get('username')
                record_unblocked_user(username, diblok, saldo, username, diblok, username)
                unblock_user(id)
                bot.send_message(message.chat.id, text=f"Selamat! {username} Anda telah dilepas dari blokir!")
            elif saldo > 10:
                saldo = 0
                diblok = requests.POST.get('username')
                unblock_user(id)
                bot.send_message(message.chat.id, text=f"Selamat! Selamat datang kembali {username}!")
                bot.send_message(message.chat.id, text="Anda sudah tidak terblokir.")
            elif username == None and username == username:
                bot.send_message(message.chat.id, text=f"Selamat datang {username}\nAnda belum melakukan registrasi\nSilahkan chat {admin}.")
            elif is_blokir_aktif > 0:
                bot.send_message(message.chat.id, text="Anda telah kembali menjadi premium.")
                record_unblocked_user(id, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, account, koin_awal, account_number, balance)
                bot.send_message(message.chat.id, text="Anda sudah tidak terblokir.")
                blokir_nonaktif(message.chat.id)



def toggle_blokir(message):
    global blokir_command_ai
    blokir_command_ai = not message.startswith
    if blokir_command_ai:
        bot.send_message(message.chat.id, text="Fitur blokir perintah AI telah diaktifkan.")
    else:
        bot.send_message(message.chat.id, text="Fitur blokir perintah AI telah dinonaktifkan.")

# Handler untuk perintah /blokir
@bot.message_handler(commands=[f'blokir {passnya}'])
def handle_blokir(message):
    toggle_blokir(message)

def create_blokir_prompt(message):
    global is_blokir_aktif
    user_id = message.from_user.id
    saldo_baru = saldo  # Pastikan variabel jumlah_koin sudah didefinisikan
    if is_blokir_active(message):
        bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        bot.send_message(message.chat.id, text=f"saldo kamu, ya.. kamu {user_id} belum terisi, saldo sedekahan mencapai 0. Segera lakukan /payment atau /topup.")
    return f"{identitas}\nPelanggaran saldo sedekahan terdeteksi, jumlah saldo: {saldo_baru}\nanda masih punya /n saldo sedekah sebanyak {saldo_pengguna}:"

# Insert data into the table
def insert_saldo(account_number, balance):
    cursor.execute('INSERT INTO izmiftahdatabase (account_number, balance) VALUES (?, ?)', (account_number, balance))
    conn.commit()

# Update balance of an account
def update_saldo(account_number, new_balance):
    cursor.execute('UPDATE saldo SET balance = ? WHERE account_number = ?', (new_balance, account_number))
    conn.commit()

# Retrieve balance of an account
def get_balance(account_number):
    cursor.execute('SELECT balance FROM saldo WHERE account_number = ?', (account_number,))
    return cursor.fetchone()[0]

# Delete an account from the table
def delete_saldo(account_number):
    cursor.execute('DELETE FROM saldo WHERE account_number = ?', (account_number,))
    conn.commit()

# Close the database connection
def close_connection():
    cursor.close()
    conn.close()

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
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

    with sqlite3.connect('izmiftah.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE saldo SET balance = balance - 1")
        conn.commit()

    with open("output.txt", "w") as output_file:
        for result in domain_results:
            output_file.write(f"{result}\n")

    return domain_results

# Fungsi untuk mengekstrak domain dari URL
def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        domain = None
    return domain

# Fungsi untuk melakukan scraping domain
def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []

        # Menyimpan hasil pencarian dalam list
        search_results = ['https://example.com', 'https://example.org', 'https://example.net'][:num_results]

        for url in search_results:
            print(f"Found URL: {url}")
            domain = extract_domain(url)
            if domain:
                result = {
                    'keyword': keyword,
                    'URL': url,
                    'Domain': domain,
                }
                results.append(result)

            time.sleep(10)  # Penundaan 10 detik
            print(f"Scraped URL: {url}")
    except Exception as e:
        print(f"Error in scrape_domain: {str(e)}")  # Mengembalikan daftar kosong untuk menangani kesalahan

    return results

# Handler untuk perintah /dork
async def handle_dork(message):
    try:
        keywords_line, domain_extensions_line = message.text.split(' ')[1].split(';')
        keywords = keywords_line.split(',')
        domain_extensions = domain_extensions_line.split(',')

        all_results = []

        for keyword in keywords:
            for domain_extension in domain_extensions:
                keyword_with_extension = f"{keyword}{domain_extension}"
                results = await scrape_domain(keyword_with_extension)
                all_results.extend(results)
                time.sleep(10)  # Penundaan 10 detik

        if all_results:
            # Mengirim hasil pencarian ke pengguna
            await bot.send_message(message.chat.id, text=f"Results: {str(all_results)}")
        else:
            await bot.reply_to(message, text="No results found.")

    except ValueError:
        # Menangani kesalahan jika format perintah tidak sesuai
        await bot.reply_to(message, text="Invalid format. Use /dork <keywords>;<domain_extensions>")
    except Exception as e:
        # Menangani kesalahan umum
        await bot.reply_to(message, f"Error: {str(e)}")

# Koneksi ke izmiftah.db
conn = sqlite3.connect('izmiftah.db')
cursor = conn.cursor()

# Fungsi untuk menjalankan perintah AI (tanpa message dan prompt)
def generate_ai_prompt(keyword1, keyword2, prompt_type, key1_options, key2_options):
    try:
        with open('/root/izmiftah/keyword1.txt', "r") as key1_file, open('keyword2.txt', "r") as key2_file:
            key1_options = key1_file.readlines()
            key2_options = key2_file.readlines()
        # Buat prompt berdasarkan input dari pengguna
        prompt = f"tulisan: {file_skrip, key2_file, key1_file}\n\n"
        prompt += f"Kata Kunci: {keyword1}, {keyword2}, {key2_options}\n\n"
        prompt += f"Jenis Prompt: {prompt_type, key1_options, key1_options, key1_options, key1_options, key1_options}"

        # Jalankan permintaan ke OpenAI Chat API dengan endpoint yang tepat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a worker and developer"},
                {"role": "user", "content": prompt}
            ]
        )

        # Ambil jawaban dari respons
        ai_reply = response['choices'][0]['message']['content']
        return ai_reply
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

def send_telegram_message(message):
    try:
        user_id = message.from_user.id
        username = message.from_user.username

        if not user_mgmt.is_whitelisted(user_id):
            bot.send_message(message.chat.id, "Maaf, bot ini disita hingga beberapa abad. silahkan lakukan #daftar terlebih dahulu")
            return

        if is_blokir_active(message):
            bot.send_message(message.chat.id, "Saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo. Lakukan /pembayaran atau /bukablokir terlebih dahulu.")
            return

        if user_id in blocked_users:
            bot.send_message(message.chat.id, "Maaf, Anda telah diblokir.")
            return

        bot.send_message(message.chat.id, f"Selamat! datang kembali {username}!")
        
        params = {
            "chat_id": message.chat.id,
            "text": message.text
        }

        url = f"https://api.telegram.org/bot{bot.token}/sendMessage"
        response = requests.post(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to send message to Telegram bot: {response.text}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Terjadi kesalahan: {str(e)}")
        
@bot.message_handler(commands=['chat'])
def write_document(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
        if blocked_users:

            if is_blokir_active(message):
                bot.send_message(message.chat.id, text=f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")
                is_not_blocked()
                block_user(username)
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            inputs = message.text[len('/chat '):].split(';')
            if len(inputs) == 3:
                bot.reply_to(message, text= "Format salah, silakan ikuti format ini: /chat pesan1;pesan2")


            judul = inputs[0].strip()
            subjudul_list = inputs[1].strip().split(',')
            keywords_list = inputs[1].strip().split(',')

            # membuat prompt
            prompt = f"Judul: {judul}\n\n"

            for idx, sub_judul in enumerate(subjudul_list, start=1):
                prompt += f"Sub_{idx}: {sub_judul}\n"
            prompt += "Keywords: " + ', '.join(keywords_list) + "\n\n"

            response = openai.Completion.create(
                model="gpt-3.5-turbo-16k",
                prompt="buatkan saya",
                max_tokens=1000
            )

            bot.reply_to(message, response.choices[0].text.strip())
            global saldo_awal, new_saldo, saldo_pengguna
            saldo_awal  += -1
            new_saldo += -3
            saldo += -10
            saldo_pengguna += -10
            saldo_pengguna += -10
        else:
            bot.send_message(message.chat.id, text=f"selamat! datang kembali {username}!")
            inputs = message.text[len('/chat '):].split(';')
            if len(inputs) == 3:
                bot.reply_to(message, text= "Format salah, silakan ikuti format ini: /chat pesan1;pesan2")

        bot.send_message(message.chat.id, text=prompt)
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Terjadi kesalahan: {str(e)}")


import subprocess
import time

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

# Fungsi untuk mendapatkan informasi DNS
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

# Handler untuk perintah /dnsinfo
@bot.message_handler(commands=['dnsinfo'])
def handle_dnsinfo(message):
    try:
        domain = message.text.split(' ')[1]
        cname_values, ipv4_addresses, ipv6_addresses = get_dns_info(domain)
        bot.send_message(message.chat.id, text=f"CNAME: {cname_values}\nIPv4: {ipv4_addresses}\nIPv6: {ipv6_addresses}")
        time.sleep(10)  # Menambahkan penundaan selama 10 detik
    except Exception as e:
        bot.send_message(message.chat.id, text=f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mengekstrak domain dari URL
def extract_domain(url):
    try:
        domain = url.split('//')[1].split('/')[0]
    except IndexError:
        print(f"Error extracting domain from URL: {url}")
        domain = None
    return domain

def scrape_domain(keyword, num_results=3):
    try:
        print(f"Searching for: {keyword}")
        results = []

        # Mengonfigurasi parameter pencarian Google
        params = {
            'q': keyword,
            'num': num_results
        }

        # URL pencarian Google
        google_search_url = "https://www.google.com/search?q="

        # Melakukan permintaan pencarian Google
        response = requests.get(google_search_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Menemukan semua hasil pencarian dalam tag <a>
        search_results = soup.find_all('a')

        for link in search_results:
            url = link.get('href')
            if url and url.startswith('http'):
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

                time.sleep(10)  # Memberi jeda 10 detik antara permintaan untuk menghindari pemblokiran

        return results

    except Exception as e:
        print(f"Error scraping domain: {str(e)}")
        return []

# Handler untuk perintah /scan
@bot.message_handler(commands=['scan'])
def handle_subdomain_query(message):
    try:
        domain = message.text.split()[-1]  # Mengasumsikan domain adalah teks terakhir setelah perintah
        results = scan_subdomain(domain)
        bot.reply_to(message, text=f"Subdomain scan results: {results}")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

# Fungsi untuk melakukan pemindaian subdomain
def scan_subdomain(domain):
    with open("subdomains.txt", "r") as subdomain_file:
        subdomains = subdomain_file.read().splitlines()
    domain_results = []
    subdomains = [subdomain for subdomain in subdomains]
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


# Fungsi untuk memeriksa apakah file cover.png kosong
def check_cover_png():
    file_path = 'cover.png'
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        return True
    else:
        return False

# Handler untuk perintah /start dan /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    try:
        bot.reply_to(message, f"selamat datang di bot saya, ketik /update or /ai untuk menulis otomatis\n /dork for seraching and /scan for scanning subdomains")
        bot.send_message(message.chat.id, text=f"Gunakan perintah /saldo untuk melihat jumlah saldo Anda.\n dan silahkan membayar ke {admin} dulu sebelum /topup ketik /berbagi [passsword] untuk berbagi saldo")
        bot.send_message(message.chat.id, text=f"Jangan lupa upload keyword.txt dan skrip.txt terlebih dahulu\n sebelum menggunakan ai \n pemilik: {admin}\n THANKS!!")
    except Exception as e:
        # Menangani kesalahan umum
        bot.reply_to(message, f"Error: {str(e)}")

def random_keywords(dataframe):
    try:
        num_keywords = len(dataframe)
        if num_keywords == 0:
            return []
        elif num_keywords == 1:
            return [dataframe.iloc[0, 0]]
        elif num_keywords == 2:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0]]
        elif num_keywords == 3:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0]]
        elif num_keywords == 4:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0]]
        elif num_keywords == 5:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0]]
        elif num_keywords == 6:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0]]
        elif num_keywords == 7:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0], dataframe.iloc[6, 0]]
        elif num_keywords == 8:
            return [dataframe.iloc[0, 0], dataframe.iloc[1, 0], dataframe.iloc[2, 0], dataframe.iloc[3, 0], dataframe.iloc[4, 0], dataframe.iloc[5, 0], dataframe.iloc[6, 0], dataframe.iloc[7, 0]]
        elif num_keywords == 9:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 10:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 11:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 12:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
        elif num_keywords == 13:
            random_indices = random.sample(range(num_keywords), min(num_keywords, 10))
            # Mengambil kata kunci yang sesuai dengan indeks yang dihasilkan secara acak
            random_keywords = [dataframe.iloc[idx, 0] for idx in random_indices]
            return random_keywords
    except Exception as e:
        # Menangani kesalahan umum
        print("Error")

def extend_keywords_list(new_keywords):
    global keywords_list
    keywords_list.extend(new_keywords)

@bot.message_handler(commands=['upload'])
def update_keywords(message):
    keyword_filename = 'keyword.txt'  # Ganti dengan nama file keyword yang sesuai
    new_keywords = read_keywords_file(keyword_filename)

    if new_keywords:
        extend_keywords_list(new_keywords)
        bot.reply_to(message, f"Keywords berhasil diperbarui. Total {len(new_keywords)} kata kunci ditambahkan.")
    else:
        bot.reply_to(message, "Gagal memperbarui keywords. Pastikan file 'keyword.txt' tersedia dan berisi kata kunci.")

    if check_cover_png():
        bot.reply_to(message,
                     "cover.png kosong. Silahkan upload cover.png sebagai logo atau cover karya tulis atau novel Anda.")
    else:
        bot.reply_to(message, "Terima kasih! File cover.png sudah diunggah.")

# Fungsi untuk menggabungkan beberapa file PDF menjadi satu
def merge_pdf_files(output_filename, input_filenames):
    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    for pdf_filename in input_filenames:
        merger.append(pdf_filename)

    merger.write(output_filename)
    merger.close()

# Fungsi untuk menghasilkan daftar kata kunci secara acak
def generate_random_keywords(num_keywords):
    # Daftar kata kunci acak
    keywords = []

    # Jalankan file run.sh untuk memproses kata kunci
    try:
        subprocess.run(['sh', 'run.sh'])
    except Exception as e:
        print(f"Error saat menjalankan run.sh: {e}")

    return keywords

def generate_keywords_pdf_novel(keywords, pdf_filename):
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Buat halaman PDF
    story = []

    # Ganti dengan logika Anda untuk menghasilkan konten PDF berdasarkan kata kunci
    # Di sini, kita akan menambahkan setiap kata kunci sebagai paragraf dengan gaya khusus
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    keyword_style = normal_style.clone('KeywordStyle')
    keyword_style.textColor = colors.blue  # Mengatur warna teks kata kunci menjadi biru

    for keyword in keywords:
        keyword_paragraph = Paragraph(keyword, keyword_style)
        story.append(keyword_paragraph)

    # Menambahkan konten ke dokumen PDF
    doc.build(story)

    print(f"Dokumen PDF berhasil disimpan di {pdf_filename}")

# Fungsi untuk menghasilkan kata kunci acak menggunakan OpenAI GPT-3
def generate_random_keywords_openai(num_keywords):
    try:
        prompt = f"Buatlah daftar kata kunci acak untuk keyword yang di berikan. Dengan jumlah kata kunci: {num_keywords}"

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-16k",
            prompt=prompt,
            max_tokens=num_keywords
        )

        keywords = response.choices[0].text.strip().split('\n')
        return keywords
    except Exception as e:
        print(f"Error saat menghasilkan kata kunci acak: {e}")

# Fungsi untuk membaca kata kunci dari file CSV
def read_keywords_file(filename):
    with open(filename, 'r') as file:
        keywords = file.read().splitlines()
        return keywords


# Handler untuk perintah /update
@bot.message_handler(commands=['update_pdf'])
def update_keywords(message):
    try:
        num_keywords = 5  # Ganti dengan jumlah kata kunci yang Anda inginkan

        # Generate daftar kata kunci secara acak
        random_keywords = generate_random_keywords_openai(num_keywords)

        # Nama file PDF yang akan dihasilkan
        pdf_filename_pdfkit = "random_keywords_pdfkit.pdf"
        pdf_filename_fpdf = "random_keywords_fpdf.pdf"
        pdf_filename_reportlab = "random_keywords_reportlab.pdf"

        # Generate daftar kata kunci dalam bentuk PDF menggunakan pdfkit
        generate_keywords_pdf_pdfkit(random_keywords, pdf_filename_pdfkit)

        # Generate daftar kata kunci dalam bentuk PDF menggunakan FPDF
        generate_keywords_pdf_fpdf(random_keywords, pdf_filename_fpdf)

        # Generate daftar kata kunci dalam bentuk PDF menggunakan reportlab
        generate_keywords_pdf_reportlab(random_keywords, pdf_filename_reportlab)

        # Menggabungkan semua file PDF ke dalam satu file 'output_novel.pdf'
        merge_pdf_files('output_novel.pdf', ['ai.pdf', pdf_filename_pdfkit, pdf_filename_fpdf, pdf_filename_reportlab])

        bot.send_message(message.chat.id, f"Kata kunci acak telah dihasilkan. Semua file PDF telah digabungkan ke dalam 'output_novel.pdf'.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

from datetime import datetime

def is_cover_updated():
    # Mendapatkan timestamp modifikasi terakhir file cover.png
    cover_path = 'foto.png'
    if os.path.exists(cover_path):
        cover_timestamp = os.path.getmtime(cover_path)
        # Mendapatkan timestamp saat ini
        current_timestamp = datetime.now().timestamp()
        # Menambahkan toleransi waktu sebesar 5 detik
        tolerance = 5
        # Memeriksa apakah file cover.png sudah terupdate dalam 5 detik terakhir
        if current_timestamp - cover_timestamp <= tolerance:
            return True
    return False
    
def is_ai_updated():
    # Mendapatkan timestamp modifikasi terakhir file cover.png
    cover_path = 'ai.txt'
    if os.path.exists(cover_path):
        cover_timestamp = os.path.getmtime(cover_path)
        # Mendapatkan timestamp saat ini
        current_timestamp = datetime.now().timestamp()
        # Menambahkan toleransi waktu sebesar 5 detik
        tolerance = 5
        # Memeriksa apakah file cover.png sudah terupdate dalam 5 detik terakhir
        if current_timestamp - cover_timestamp <= tolerance:
            return True
    return False

@bot.message_handler(commands=['remix'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

        subprocess.run(['bash', 'lukis.sh'], check=True)

        # Memeriksa apakah file cover.png sudah terupdate
        if is_ai_updated():
            # Mengirim gambar cover.png ke Telegram
            with open('/root/izmiftah/generated_image.jpg', 'rb') as cover_file:
                bot.send_photo(message.chat.id, cover_file)
            bot.reply_to(message, "Skrip berhasil diperbarui silahkan /download generated_image.jpg .")
        else:
            bot.reply_to(message, "ai.txt belum terupload. Silahkan jalankan /ai_prompt terlebih dahulu atau /download generated_image.jpg nya saja.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")


# Fungsi untuk mengirim pesan ke pengguna
def send_message(chat_id, text):
    bot.send_message(chat_id, text)

# Fungsi untuk membuat ulang teks AI
def generate_prompt(image_path):
    return f"Generate an image similar to the reference image '{image_path}'."

# Fungsi untuk menghasilkan gambar dengan OpenAI
def generate_image(prompt):
    openai.api_key = api_key
    response = openai.Image.create(
        prompt=prompt,
        n=3,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    image = Image.open(requests.get(image_url, stream=True).raw)
    return image

# Fungsi untuk mengirim gambar ke pengguna
def send_image(chat_id, image):
    image.save('referensi.jpg')
    photo = open('referensi.jpg', 'rb')
    bot.send_photo(chat_id, photo)

# Handler untuk perintah /referensi
@bot.message_handler(commands=['referensi'])
def handle_referensi(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

        if is_cover_updated():
            chat_id = message.chat.id
            send_message(chat_id, "Mohon tunggu, sedang menghasilkan gambar...")
            image_path = 'foto.png'  # Path gambar referensi
            prompt = generate_prompt(image_path)
            image = generate_image(prompt)
            send_image(chat_id, image)
            send_message(chat_id, "Berikut hasil gambar yang dibuat berdasarkan referensi 'foto.png'.")
        else:
            bot.reply_to(message, "Foto.png belum terupload. Silahkan jalankan /photo {url-kamu}.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

    
import telebot
from PIL import Image
import io

def resize_image(image, target_megapixels):
    width, height = image
    current_pixels = width * height
    target_pixels = target_megapixels * 1e6
    scale_factor = (target_pixels / current_pixels) ** 0.5
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_image

@bot.message_handler(func=lambda message: message.text.startswith('/RESIZE'))
def handle_resize_command(message):
    try:
        # Memastikan bahwa perintah memiliki dua bagian dan bagian kedua adalah angka
        command_parts = message.text.split()
        if len(command_parts) != 2 or not command_parts[1].isdigit():
            bot.reply_to(message, "Please specify the size in megapixels as 'resize 10' or 'resize 15'.")
            return
        
        target_megapixels = int(command_parts[1])
        if target_megapixels not in [10, 15]:
            bot.reply_to(message, "Please specify 10 or 15 megapixels.")
            return
        
        # Memastikan bahwa pesan yang di-reply mengandung foto
        if not message.reply_to_message or not message.reply_to_message.photo:
            bot.reply_to(message, "Please reply to a photo with this command.")
            return
        
        # Mengambil file ID foto dengan resolusi tertinggi
        file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        image = Image.open(io.BytesIO(downloaded_file))
        
        # Mengubah ukuran gambar
        resized_image = resize_image(image, target_megapixels)
        
        # Menyimpan hasil ke byte buffer
        buf = io.BytesIO()
        resized_image.save(buf, format='PNG')
        buf.seek(0)
        
        # Mengirim hasil sebagai dokumen untuk mempertahankan transparansi
        bot.send_document(message.chat.id, buf, reply_to_message_id=message.reply_to_message.message_id)
        
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

import telebot
import random
import nltk
import requests
from fpdf import FPDF
from deep_translator import GoogleTranslator
import openai

# Inisialisasi OpenAI API key
openai.api_key = api_key

# Daftar kata-kata untuk setiap kategori
wordlists = {
    "action": ["memperkenalkan", "mendemonstrasikan", "memahami", "membahas", "menyajikan"],
    "technique": ["konsep", "teknik", "cara", "metode", "pendekatan"],
    "learning": ["belajar", "pembelajaran", "pemahaman", "pengetahuan", "keterampilan", "konseptualitas", "pemahaman"],
    "learning_type": ["explained", "tutorial", "demonstrasi", "praktek", "latihan", "dasar-dasar"],
    "subject": ["teori", "praktik", "implementasi", "penerapan", "penggunaan", "dasar-dasar", "tehnik dan konsep", "tehnik dan fundamental", "tehnik-dasar"]
}

# Fungsi untuk menghasilkan teks acak berdasarkan topik
def generate_random_text(topic):
    words = nltk.word_tokenize(topic)
    random.shuffle(words)
    return ' '.join(words)

# Fungsi untuk menghasilkan kurikulum pembelajaran
def generate_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    action = random.choice(wordlists["action"])
    technique = random.choice(wordlists["technique"])
    learning = random.choice(wordlists["learning"])
    learning_type = random.choice(wordlists["learning_type"])
    subject = random.choice(wordlists["subject"])
    time_needed = random.randint(1, 12)
    converted_text = generate_random_text(topic)

    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Untuk mempelajari kurikulum ini, kamu perlu menghabiskan waktu {time_needed} jam.\n\n"
                  f"Kurikulum yang perlu kamu pelajari:\n"
                  f"Belajarlah tentang {action} {technique} {topic} yang mengandung {learning} tentang {subject} {topic} dengan metode {learning_type} "
                  f"dari {topic}.\n\n")
    return curriculum

# Fungsi untuk membaca link video dari database1.txt
def get_video_link():
    try:
        with open('/root/izmiftah/database1.txt', 'r') as file:
            links = file.readlines()
            return random.choice(links).strip()
    except FileNotFoundError:
        return "https:\\youtube.com\q="

# Fungsi untuk menghasilkan kurikulum pembelajaran dengan link video
def generate_video_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    learning_type = random.choice(wordlists["learning_type"])
    technique = random.choice(wordlists["technique"])
    action = random.choice(wordlists["action"])
    
    video_link = get_video_link()
    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Dasar-dasar {topic} dengan metode {learning_type} mengenai {topic}.\n\n"
                  f"Selengkapnya bisa belajar di video berikut: https:\\{video_link}how+to+{learning_type}+dari+{topic}?")
    return curriculum

def create_pdf(content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Ubah encoding ke 'utf-8'
    content = content.encode('latin-1', 'replace').decode('utf-8')
    
    pdf.multi_cell(0, 10, content)
    pdf.output(filename, 'F')


# Fungsi untuk mendapatkan materi belajar dari OpenAI
def get_openai_response(topic):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Buatkan materi belajar tentang {topic}",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Fungsi untuk memecah materi menjadi bagian-bagian terstruktur
def generate_structured_material(topic):
    sections = [
        "Apa itu " + topic,
        "Pengenalan",
        "Pengenalan Aplikasi",
        "Dasar-dasar",
        "Teori dan Praktik",
        "Implementasi",
        "Penerapan",
        "Penggunaan",
        "Teknik dan Konsep"
    ]
    structured_material = ""
    for section in sections:
        openai_response = get_openai_response(section)
        translated_response = GoogleTranslator(source='en', target='id').translate(openai_response)
        structured_material += f"{section}\n\n{translated_response}\n\n"
    return structured_material

# Fungsi untuk memecah materi menjadi beberapa bagian
def split_text(text, max_length):
    parts = []
    while len(text) > max_length:
        part = text[:max_length]
        last_space_index = part.rfind(' ')
        if last_space_index != -1:
            parts.append(part[:last_space_index])
            text = text[last_space_index+1:]
        else:
            parts.append(part)
            text = text[max_length:]
    parts.append(text)
    return parts

# Handler untuk perintah /BELAJAR
@bot.message_handler(commands=['BELAJAR'])
def belajar(message):
    try:
        # Ambil topik dari pesan
        topic = message.text.split(' ', 1)[1]
        # Buat kurikulum
        curriculum = generate_curriculum(topic)
        # Kirim kurikulum ke pengguna
        bot.reply_to(message, curriculum)
        
        # Buat dan kirim PDF
        create_pdf(curriculum, 'materi.pdf')
        with open('/root/izmiftah/materi.pdf', 'rb') as pdf_file:
            bot.send_document(message.chat.id, pdf_file)
        
        # Dapatkan materi tambahan dari OpenAI
        openai_response = get_openai_response(topic)
        translated_response = GoogleTranslator(source='en', target='id').translate(openai_response)
        
        # Split dan kirim materi tambahan ke pengguna
        for part in split_text(translated_response, 4096):
            bot.reply_to(message, part)
        
    except IndexError:
        # Tangani jika format perintah tidak sesuai
        bot.reply_to(message, "Format perintah salah. Gunakan /BELAJAR [topik].")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    finally:
        bot.reply_to(message, "Permintaan Anda telah diproses.")

import telebot
import random
import nltk
import requests
from fpdf import FPDF
from deep_translator import GoogleTranslator
import openai

# Inisialisasi DeepAI API key
openai.api_key = api_key

# Daftar kata-kata untuk setiap kategori
wordlists = {
    "action": ["memperkenalkan", "mendemonstrasikan", "memahami", "membahas", "menyajikan"],
    "technique": ["konsep", "teknik", "cara", "metode", "pendekatan"],
    "learning": ["belajar", "pembelajaran", "pemahaman", "pengetahuan", "keterampilan", "konseptualitas", "pemahaman"],
    "learning_type": ["explained", "tutorial", "demonstrasi", "praktek", "latihan", "dasar-dasar"],
    "subject": ["teori", "praktik", "implementasi", "penerapan", "penggunaan", "dasar-dasar", "tehnik dan konsep", "tehnik dan fundamental", "tehnik-dasar"]
}

# Fungsi untuk menghasilkan teks acak berdasarkan topik
def generate_random_text(topic):
    words = nltk.word_tokenize(topic)
    random.shuffle(words)
    return ' '.join(words)

# Fungsi untuk menghasilkan kurikulum pembelajaran
def generate_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    action = random.choice(wordlists["action"])
    technique = random.choice(wordlists["technique"])
    learning = random.choice(wordlists["learning"])
    learning_type = random.choice(wordlists["learning_type"])
    subject = random.choice(wordlists["subject"])
    time_needed = random.randint(1, 12)
    converted_text = generate_random_text(topic)

    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Untuk mempelajari kurikulum ini, kamu perlu menghabiskan waktu {time_needed} jam.\n\n"
                  f"Kurikulum yang perlu kamu pelajari:\n"
                  f"Belajarlah tentang {action} {technique} {topic} yang mengandung {learning} tentang {subject} {topic} dengan metode {learning_type} "
                  f"dari {topic}.\n\n")
    return curriculum

# Fungsi untuk membaca link video dari database1.txt
def get_video_link():
    try:
        with open('/root/izmiftah/database1.txt', 'r') as file:
            links = file.readlines()
            return random.choice(links).strip()
    except FileNotFoundError:
        return "https:\\youtube.com\q="

# Fungsi untuk menghasilkan kurikulum pembelajaran dengan link video
def generate_video_curriculum(topic):
    # Pilih kata-kata acak dari setiap kategori
    learning_type = random.choice(wordlists["learning_type"])
    technique = random.choice(wordlists["technique"])
    action = random.choice(wordlists["action"])
    
    video_link = get_video_link()
    # Buat kurikulum berdasarkan topik dan kata-kata yang dipilih
    curriculum = (f"Dasar-dasar {topic} dengan metode {learning_type} mengenai {topic}.\n\n"
                  f"Selengkapnya bisa belajar di video berikut: https:\\{video_link}how+to+{learning_type}+dari+{topic}?")
    return curriculum

def create_pdf(content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Ubah encoding ke 'utf-8'
    content = content.encode('latin-1', 'replace').decode('utf-8')
    
    pdf.multi_cell(0, 10, content)
    pdf.output(filename, 'F')

# Fungsi untuk mendapatkan materi belajar dari DeepAI
def get_openai_response(topic):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Buatkan materi belajar tentang {topic}",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Fungsi untuk memecah materi menjadi bagian-bagian terstruktur
def generate_structured_material(topic):
    sections = [
        "Apa itu " + topic,
        "Pengenalan",
        "Pengenalan Aplikasi",
        "Dasar-dasar",
        "Teori dan Praktik",
        "Implementasi",
        "Penerapan",
        "Penggunaan",
        "Teknik dan Konsep"
    ]
    structured_material = ""
    for section in sections:
        openai_response = get_openai_response(section)
        translated_response = GoogleTranslator(source='en', target='id').translate(openai_response)
        structured_material += f"{section}\n\n{translated_response}\n\n"
    return structured_material

# Fungsi untuk memecah materi menjadi beberapa bagian
def split_text(text, max_length):
    parts = []
    while len(text) > max_length:
        part = text[:max_length]
        last_space_index = part.rfind(' ')
        if last_space_index != -1:
            parts.append(part[:last_space_index])
            text = text[last_space_index+1:]
        else:
            parts.append(part)
            text = text[max_length:]
    parts.append(text)
    return parts

# Handler untuk perintah /BELAJAR
@bot.message_handler(commands=['materi'])
def belajar(message):
    try:
        # Ambil topik dari pesan
        topic = message.text.split(' ', 1)[1]
        
        # Buat kurikulum dan simpan ke file materi_kurikulum.txt
        curriculum = generate_curriculum(topic)
        with open(f'materi_kurikulum.txt', 'w') as file:
            file.write(curriculum)
        
        # Kirim pesan ke pengguna bahwa kurikulum telah diproses
        bot.reply_to(message, f"Kurikulum {topic} telah diproses dan disimpan ke file materi_kurikulum.txt. Silakan tunggu beberapa saat hingga kurikulum selesai diolah.")
        
        # Buat kurikulum dan simpan ke file materi_$1.txt, $1 adalah angka 1-seterusnya
        for i in range(1, 11):
            curriculum_file_name = f'materi_{i}.txt'
            with open(curriculum_file_name, 'w') as file:
                file.write(generate_curriculum(topic))
            
            # Kirim kurikulum ke Telegram menggunakan bot
            bot.send_document(message.chat.id, open(curriculum_file_name, 'rb'))
            
            # Tampilkan pesan ke pengguna bahwa kurikulum telah terkirim
            bot.reply_to(message, f"Kurikulum {topic} telah terkirim ke file materi_{i}.txt. Silakan tunggu beberapa saat hingga kurikulum selesai diolah.")
    
    except IndexError:
        # Tangani jika format perintah tidak sesuai
        bot.reply_to(message, "Format perintah salah. Gunakan /materi [topik].")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {e}")
    finally:
        bot.reply_to(message, f"Permintaan Anda telah diproses.")

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@bot.message_handler(commands=['ustad'])
def main(message):
    try:
        text = message.text.lower()
        if 'apa' or 'kah' or 'apakah' in text:
            response = get_openai_response("Berikan jawaban yang bijak dan tegas dalam ajaran islam mengenai apa yang saya berikan, seolah-olah Anda adalah seorang alim ulama.")
            bot.send_message(message.chat.id, response)
        if 'saya' in text:
            response = get_openai_response("Berikan jawaban yang bijak dan menenangkan tentang saya, seolah-olah Anda adalah seorang alim ulama.")
            bot.send_message(message.chat.id, response)
        elif 'ku' in text:
            response = get_openai_response("Berikan jawaban yang lengkap mengenai identifikasi diri, sifat, tujuan hidup, serta sifat buruk yang perlu diubah, seolah-olah Anda adalah seorang alim ulama.")
            bot.send_message(message.chat.id, response)
            bot.send_message(message.chat.id, 'Siapakah Anda?')
        elif 'tujuan' in text:
            response = get_openai_response("Berikan jawaban yang lengkap dan terstruktur tentang tujuan hidup dan langkah-langkah mencapainya, seolah-olah Anda adalah seorang alim ulama.")
            bot.send_message(message.chat.id, response)
        elif 'langkah' in text:
            langkah = text.split('+')
            response = "Berikut adalah pendapat saya tentang langkah-langkah Anda:\n"
            for i, l in enumerate(langkah):
                opinion = get_openai_response(f"Berikan pendapat tentang langkah: {l.strip()}, seolah-olah Anda adalah seorang alim ulama.")
                response += f"{i+1}. {l.strip()}: {opinion}\n"
            bot.send_message(message.chat.id, response)
        elif ' ' in text:
            response = get_openai_response("Berikan panduan kreatif tentang tujuan hidup berdasarkan identifikasi saya, seolah-olah Anda adalah seorang alim ulama.")
            bot.send_message(message.chat.id, response)
        elif 'lakukan' in text:
            prioritas = text.split('/')
            response = "Berikut adalah prioritas yang telah disusun:\n"
            for i, p in enumerate(prioritas):
                response += f"{i+1}. {p.strip()}\n"
            bot.send_message(message.chat.id, response)
        else:
            response = get_openai_response(f"Saya adalah orang yang suka tidak enakan dengan orang lain, apa yang perlu saya lakukan? Berikan jawaban seolah-olah Anda adalah seorang alim ulama yang memberikan nasihat bijak dan solutif.")
            bot.send_message(message.chat.id, response)
    except Exception as e:
        bot.send_message(message.chat.id, f"Terjadi kesalahan: {e}")
    finally:
        bot.send_message(message.chat.id, 'Selamat datang! Saya siap membantu Anda menentukan tujuan hidup Anda dan memberikan pendapat untuk mencapainya.')


class PayloadGenerator:
    def __init__(self, host, method):
        self.host = host
        self.method = method
        self.random_inputs = []

    async def generate_payload(self):
        random_words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 3))) for _ in range(random.randint(1, 5))]
        method = '[proxy-conncetion]'.join(random_words).upper()
        http_version = f"HTTP/{random.choice(['1.0', '1.1', '2.0'])}"
        
        # Adding random 'r' and 'n' and '[crlf]' characters
        random_rn = ''.join(random.choices(['/r/n/', '[Host]'], k=random.randint(8, 15)))
        crlf = ''.join(['//[crlf]'] * random.randint(5, 10))
        
        payload = f"{http_version} /r/n [{self.method}] /r/n/n/{'[]'.join(random_words)}\r\n"
        payload += f"Host: {self.host}\r\n"
        payload += f"Upgrade: {self.method}\r\n"
        payload += f"{random_rn}{crlf}\r\n"
        
        self.random_inputs.append(payload)
        return self.random_inputs

    async def raise_error(self):
        raise Exception("Generated Payload is invalid!")

    async def run(self):
        try:
            await self.generate_payload()
        except Exception as e:
            await self.raise_error()

    async def start(self):
        await self.run()

@bot.message_handler(commands=['GACHA'])
def send_payload(message):
    try:
        parts = message.text.split()
        if len(parts) < 4:
            bot.reply_to(message, "Usage: /GACHA <jenis koneksi> <method> <host>")
            return
        koneksi = parts[1].upper()
        method = parts[2].lower()
        host = parts[3]
        generator = PayloadGenerator(host, method)
        asyncio.run(generator.start())
        payload_message = "\n\n".join(generator.random_inputs)
        bot.reply_to(message, f"{koneksi} {payload_message}")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

import telebot
from telebot.types import Message, InputFile
from PIL import Image
import os

class ImageResizer:
    def __init__(self, path, width):
        self.path = path
        self.width = width
        self.height = self.calculate_height()

    def calculate_height(self):
        try:
            with Image.open(self.path) as img:
                original_width, original_height = img.size
                aspect_ratio = original_height / original_width
                return int(self.width * aspect_ratio)
        except Exception as e:
            raise ValueError(f"Error calculating height: {e}")

    def resize_image(self):
        try:
            with Image.open(self.path) as img:
                resized_img = img.resize((self.width, self.height), Image.Resampling.LANCZOS)
                resized_path = f"resized_{os.path.basename(self.path)}"
                resized_img.save(resized_path)
                return resized_path
        except Exception as e:
            raise ValueError(f"Error resizing image: {e}")

    def get_resized_dimensions(self):
        return self.width, self.height

@bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.photo and '/Resize' in message.text.lower())
def resize_image_handler(message: Message):
    try:
        width = 7240  # Adjust as necessary or retrieve from command arguments
        photo_file = bot.get_file(message.reply_to_message.photo[-1].file_id)
        photo_path = bot.download_file(photo_file.file_path)
        
        temp_file_path = 'temp_image.jpg'
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(photo_path)
        
        resizer = ImageResizer(temp_file_path, width)
        resized_image_path = resizer.resize_image()
        
        with open(resized_image_path, 'rb') as resized_image_file:
            bot.send_photo(message.chat.id, resized_image_file)
            bot.send_message(message.chat.id, f"Gambar telah diresize ke ukuran: {resizer.get_resized_dimensions()}")
        
        os.remove(temp_file_path)
        os.remove(resized_image_path)
    except Exception as e:
        bot.send_message(message.chat.id, f"Terjadi kesalahan: {e}")


@bot.message_handler(commands=['resize'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

        subprocess.run(['bash', 'icon.sh'], check=True)

        # Memeriksa apakah file cover.png sudah terupdate
        if is_cover_updated():
            # Mengirim gambar cover.png ke Telegram
            with open('/root/izmiftah/foto.png', 'rb') as cover_file:
                bot.send_photo(message.chat.id, cover_file)
            bot.reply_to(message, "Skrip berhasil diperbarui.")
        else:
            bot.reply_to(message, "Foto.png belum terupload. Silahkan jalankan /photo {url-kamu}.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

# Handler untuk perintah /keyword
@bot.message_handler(commands=['keyword'])
def update_scripts(message):
    try:
        if is_blokir_active(message):
            bot.send_message(message.chat.id, f"saldo telah melebihi atau mencukupi atau melebihi dari 0 saldo\n lakukan /pembayaran atau /bukablokir terlebih dahulu.")

            subprocess.run(['bash', 'key.sh'], check=True)
        bot.reply_to(message, text= "Skrip berhasil diperbarui.")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error: {e}")

# Fungsi untuk memperbarui database kata kunci dari file CSV
def update_keywordt():
    global keywords_list

    try:
        with open('/root/izmiftah/keyword.txt', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            keywords_list = [row[0] for row in reader]
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Tambahkan logika untuk memeriksa keberadaan file auto.xlsx
if not os.path.isfile('auto.xlsx'):
    # Lakukan operasi jika file tidak ada
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

# Fungsi untuk menghasilkan HTML berdasarkan data dari dataframe
def generate_html(dataframe):
    # Your logic for generating HTML based on the dataframe goes here
    # Replace this with your actual implementation
    generated_html = f"jangan lupa /update terlebih dahulu \n silahkan /download.. dan tolong \n <html<<body<<h1< ganti bagian sini... untuk mengedit file htmlnya </h1<</body<</html<"
    return generated_html

# Inisialisasi identitas
identitas = "mif , seorang kharismatik yang jenius dan pandai dalam berbagai hal"

# Fungsi untuk mendapatkan saldo pengguna dari database berdasarkan user_id
def get_saldo_pengguna_from_db(user_id):
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()
    c.execute('SELECT saldo_pengguna FROM izmiftahdatabase WHERE user_id = ?', (user_id,))
    saldo_pengguna = c.fetchone()
    update_scripts
    return saldo_pengguna[0] if saldo_pengguna else 0

# Fungsi untuk menampilkan saldo pengguna
def display_saldo(message):
    user_id = message.from_user.id
    try:
        saldo = get_saldo_pengguna_from_db(user_id)  # Mengambil saldo pengguna dari database
        bot.reply_to(message, f"Saldo global saat ini adalah: {new_saldo}")
        bot.reply_to(message, f"Adapun Saldo Anda sebesar: {saldo_pengguna}\n dengan saldo premium: sebanyak {saldo} saldo")
        bot.reply_to(message, f"Saldo sedekahan anda saat ini adalah: {jumlah_koin}")
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan dalam mengambil saldo: {str(e)}")

# Handler untuk perintah "/display_saldo"
@bot.message_handler(commands=['saldo'])
def handle_display_saldo(message):
    display_saldo(message)

@bot.message_handler(func=lambda message: message.text.startswith('/passwordku'))
def lihat_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 3:
        password = command_parts[2]
        if password == passnya:

            bot.send_message(message.chat.id, text="Password telah diubah.")
    conn = sqlite3.connect('izmiftah.db')
    c = conn.cursor()

    c.execute("SELECT username, password FROM izmiftahdatabase WHERE password = ?", (passnya,))
    result = c.fetchone()
    conn.close()

    if result:
        username, password = result
        bot.reply_to(message, f"Username: {username}\nPassword: {password}")
    else:
        bot.reply_to(message, "Password tidak ditemukan bisa jadi karena input salah. Silakan coba lagi.")

    conn.close()
def toggle_blokir_koin(message):
    global koin_terblokir
    if koin_terblokir:
        koin_terblokir = False
        bot.send_message(message.chat.id, text="Pemblokiran koin telah dinonaktifkan.")
    else:
        koin_terblokir = True
        bot.send_message(message.chat.id, text="Pemblokiran koin telah diaktifkan.")

# Handler untuk perintah "/payment"
@bot.message_handler(commands=['topup_saldo'])
def make_payment(message):
    telegram_link = generate_telegram_payment_link(message)
    open_telegram_link(telegram_link)
    user_id = message.get('user_id')
    saldo_pengguna = get_saldo_pengguna_from_db(user_id)  # Mengambil saldo pengguna dari database
    # Menambahkan user ke list unblocked_users
    bot.send_message(message.chat.id, text=f"Silahkan cek tautan pembayaran di Telegram: {telegram_link}")
    bot.send_message(message.chat.id, text=f"Saldo anda sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
    bot.send_message(message.chat.id, text=f"Saldo sedekahan anda saat ini adalah: {jumlah_koin}")
    bot.send_message(message.chat.id, text=f"Saldo global saat ini adalah: {new_saldo}")

def generate_telegram_payment_link(message):
    # melakukan proses untuk menghasilkan tautan pembayaran di Telegram berdasarkan pesan yang diberikan
    # misalnya, menggabungkan ID pengguna dan jumlah pembayaran ke dalam URL tautan
    pass

def open_telegram_link(link):
    # membuka tautan pembayaran di Telegram menggunakan browser default
    # misalnya, dengan menggunakan library webbrowser di Python
    import webbrowser
    webbrowser.open(link)

@bot.message_handler(commands=['my_id'])
def show_user_id(message):
    user_id = message.from_user.id
    bot.reply_to(message, f"Your user ID is: {user_id}")

# Handler untuk perintah "/berbagi" dengan kata sandi
@bot.message_handler(func=lambda message: message.text.startswith('/berbagi'))
def payment_with_password(message):
    command_parts = message.text.split(' ')
    if len(command_parts) == 2:
        password = command_parts[1]
        if password == passnya:
            global new_saldo, saldo_pengguna
            new_saldo += 100
            get_new_saldo(message)
            saldo_pengguna += 100
            new_saldo += 100

            record_unblocked_user(id, saldo, jumlah_koin, pengguna, saldo_baru, saldo_nol, username, koin, additional_input, new_saldo, account, koin_awal, account_number, balance)
            bot.send_message(message.chat.id, text="Berbagi berhasil.")
            bot.send_message(message.chat.id, text=f"Saldo anda telah terisi sebesar {saldo_pengguna}.")  # Memberi tahu pengguna bahwa saldo mereka telah terisi kembali
        else:
            bot.send_message(message.chat.id, text="Kata sandi salah. Coba lagi.")
    else:
        bot.send_message(message.chat.id, text="Perintah tidak valid. Lakukan topup dengan: /berbagi [password]")

# Fungsi untuk mengurangi saldo
def kurangi_saldo(jumlah, message):
    global saldo_pengguna, new_saldo
    saldo_pengguna -= jumlah
    new_saldo -= jumlah
    bot.send_message(message.chat.id, text=f"Saldo terpakai: {jumlah}. Saldo Anda sekarang: {new_saldo}")


import keyword as acak
import random

def generate_keyword_file(filename, num_keywords):
    keyword_list = acak.kwlist
    num_keywords = min(num_keywords, len(keyword_list))

    random_keywords = random.sample(keyword_list, num_keywords)

    with open(filename, "w") as file:
        file.write("\n".join(random_keywords))

def get_openai_answer(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-16k",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

@bot.message_handler(commands=['saldo'])
def handle_saldo(message):
    display_saldo(message)

# Handler untuk memberikan pertanyaan quiz
@bot.message_handler(func=lambda message: message.text.lower() == 'ya')
def ask_quiz_question(message):
    question = get_openai_answer("Tulis satu pertanyaan quiz di sini dengan tingkat kesulitan yang amat sangat rumit:")
    bot.send_message(message.chat.id, question)

# Handler untuk memberikan kata yang bersikap apatis
@bot.message_handler(func=lambda message: message.text.lower() == 'tidak')
def send_apathetic_word(message):
    apathetic_word = get_openai_answer("Berikan satu kata yang paling bersikap bodo amat:")
    bot.send_message(message.chat.id, apathetic_word)

# Fungsi peg_parser
def peg_parser():
    # Implementasi peg_parser di sini
    pass

# Contoh penggunaan assert
def check_saldo():
    global saldo_pengguna
    assert saldo_pengguna >= 0, "Saldo tidak boleh negatif."

def set_user_values():
    # Mendapatkan jumlah_koin pengguna dengan user_id tertentu
    new_saldo = 20240208205433  # Misalnya
    saldo_baru = get_saldo_from_db(new_saldo)
    print("Saldo pengguna:", saldo_baru)

    # Menambahkan jumlah_koin pengguna dengan user_id tertentu
    print("Saldo pengguna setelah penambahan:", get_saldo_from_db(user_id))

    ############### silahkan ubah ##############################
    salah_saldo = get_saldo_from_db(user_id)
    print("Saldo salah:", salah_saldo)


def tentukan_saldo(jumlah_koin):
    # Misalnya, kita menetapkan aturan bahwa setiap saldo akan diubah menjadi 5 rupiah
    return jumlah_koin * 5
def contoh_penggunaan(user_id):
    # Mendapatkan saldo pengguna dari database
    saldo_pengguna = get_saldo_pengguna_from_db(user_id)

    # Memperbarui saldo pengguna dengan saldo baru
    saldo_pengguna += new_saldo

    # Menentukan jumlah_koin berdasarkan saldo_pengguna
    jumlah_koin = tentukan_saldo(saldo_pengguna)

    # Mengembalikan saldo pengguna dan jumlah_koin
    return saldo_pengguna, jumlah_koin

# Inisialisasi new_saldo
saldo = 0
saldo_pengguna = saldo
# Handler untuk semua pesan teks
new_saldo = 0
jumlah_saldo = 0
jumlah_koin = jumlah_koin_awal
saldo = new_saldo
print(f"Saldo dari database untuk user_id {timestamp}: {saldo_pengguna}")
get_blokir = [None] * len('user_id')

def update_saldo_pengguna(user_id, new_saldo):
    #update_saldo_pengguna(username, new_saldo)
    global saldo_pengguna
    saldo_pengguna = new_saldo
    print(f"Saldo dari database untuk user_id {user_id}: {saldo_pengguna}")
    
# Fungsi untuk menjalankan skrip u8.sh
def run_u8_script():
    subprocess.call("python3 -m u8", shell=True)

# Fungsi untuk mengupload file ke Telegram
def upload_file(message, file_path):
    bot = TeleBot(TOKEN)
    bot.send_document(message.chat.id, open(file_path, 'rb'))

@bot.message_handler(func=lambda message: message.text.startswith("proxychains4 python3 -m mampus "))
def handle_ddos(message):
    message.chat.id = message.chat.id
    command = message.text
    file_path = 'ips.txt'

    if command.startswith("proxychains4 python3 -m mampus "):
        try:
            subprocess.call(command, shell=True)
            bot.send_message(message.chat.id, "Command telah dijalankan. Silahkan upload file ips.txt atau file target kalian seperti yang di bawah ini:.")
            upload_file(message, file_path)
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "Command tidak valid. Mohon masukkan command yang diawali dengan 'proxychains4 python3 -m mampus'")

# Fungsi untuk menjalankan skrip u8.sh
def run_u8_script():
    subprocess.call("python3 -m u8", shell=True)
    
# Fungsi untuk mengupload file ke Telegram
def upload_file(message, file_path):
    bot = TeleBot(TOKEN)
    bot.send_document(message.chat.id, open(file_path, 'rb'))

@bot.message_handler(commands=['cek_harga'])
def cek_harga(message):
    if len(message.text.split()) > 1:
        keywords = ' '.join(message.text.split()[1:])
        total_price = search_and_accumulate_price(keywords)
        if total_price is not None:
            send_message_telegram(keywords, total_price, message)
        else:
            bot.send_message(message.chat.id, f"Error occurred while retrieving data for keywords: {keywords}")
    else:
        bot.send_message(message.chat.id, "Mohon masukkan keywords setelah perintah /cek_harga")

def search_and_accumulate_price(keyword):
    url = f"https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword={keyword}&limit=5"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        total_price = 0
        # Implementasikan logika akumulasi harga
        return total_price
    else:
        return None

def search_with_google_shopping(keyword):
    url = f"https://www.googleapis.com/shopping/v1/products?key={google_apikey}&q={keyword}"
    response = requests.get(url)
    data = response.json()
    # Proses data sesuai kebutuhan aplikasi

def send_message_telegram(keywords, total_price, message):
    bot.send_message(message.chat.id, f"Keyword: {keywords}, Total Price: {total_price}")

import os
import json
import sqlite3
import requests
from telebot import TeleBot

# Fungsi untuk menghubungkan ke database SQLite dan membuat tabel jika belum ada
def get_db_connection():
    conn = sqlite3.connect('list.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist (
                        user_id INTEGER PRIMARY KEY,
                        blocked_at TEXT
                      )''')
    conn.commit()
    return conn

# Fungsi untuk memblokir user
def block_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    blocked_at = datetime.now().isoformat()
    cursor.execute("INSERT OR IGNORE INTO blacklist (user_id, blocked_at) VALUES (?, ?)", (user_id, blocked_at))
    conn.commit()
    conn.close()

# Fungsi untuk menghapus user dari blacklist
def allow_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blacklist WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

# Fungsi untuk menghapus user dari whitelist
def delete_user_from_whitelist(user_id):
    try:
        with open('/root/izmiftah/whitelist.json', 'r+') as file:
            whitelist = json.load(file)
            if user_id in whitelist['users']:
                whitelist['users'].remove(user_id)
                file.seek(0)
                json.dump(whitelist, file)
                file.truncate()
    except KeyError as e:
        print(f"KeyError: {str(e)}")
    except Exception as e:
        print(f"Exception: {str(e)}")

# Fungsi untuk menambahkan user ke blacklist.json
def add_to_blacklist(user_id):
    try:
        with open('/root/izmiftah/blacklist.json', 'r+') as file:
            blacklist = json.load(file)
            if user_id not in blacklist['users']:
                blacklist['users'].append(user_id)
                file.seek(0)
                json.dump(blacklist, file)
                file.truncate()
    except KeyError as e:
        print(f"KeyError: {str(e)}")
    except Exception as e:
        print(f"Exception: {str(e)}")

# Fungsi untuk memeriksa apakah user ada di whitelist
def is_whitelisted(user_id):
    try:
        with open('/root/izmiftah/whitelist.json', 'r') as file:
            whitelist = json.load(file)
            return user_id in whitelist['users']
    except KeyError as e:
        print(f"KeyError: {str(e)}")
        return False
    except Exception as e:
        print(f"Exception: {str(e)}")
        return False

# Fungsi untuk mengirim pesan menggunakan Telegram API
def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Telegram bot: {response.text}")

def is_blocked(new_saldo):
    if is_blocked is True:
        print("takdown")
        not False
    if locked_commands is True:
        print("takdown")
        not False
    if blokir_aktif is True:
        print("takdown")
        not False
    global terbuka    
    if user_mgmt.is_whitelisted(new_saldo):
        blokir_aktif = False
        terbuka = False
        print(f'{new_saldo} login')
    else:
        pass

if __name__ == '__main__':
    my_thread()
    hadeh.add(user_id)
    # Memanggil fungsi update_users_table untuk melakukan update pada tabel users
    conn.close()
    new_saldo = saldo
    saldo = 0
    blokir_aktif = True
    hadeh.add(user_id)
    hadeh.add(new_saldo)
    hadeh.add(blocked_users)
    # Menghapus file sementara
    for file in ['video.webm', 'music.mp3', 'video.m4a', 'music.ogg', 'audio.mp4']:
        if os.path.exists(file):
            os.remove(file)
    conn = sqlite3.connect('izmiftah.db')
    conn.close()
    bot.polling(none_stop=True)

def cleanup_files(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
