import requests
import random
import base64
import telebot
from telebot import types

# Token dari bot Telegram Anda
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Inisialisasi objek bot
bot = telebot.TeleBot(TOKEN)

# Api key dari DeepAI (ganti dengan api key Anda)
api_key = 'YOUR_DEEPAI_API_KEY'

def generate_prompt(prompt, api_key):
    try:
        url = "https://api.deepai.org/api/text-generator"
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key
        }
        data = {
            "text": prompt
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if 'output' in result:
                return result['output']
            else:
                return f"Error in DeepAI response: {result}"
        else:
            error_message = response.json().get('details', {}).get('input', {}).get('failedConstraints', 'Unknown error')
            return f"Error in DeepAI request. Status code: {response.status_code}. Details: {error_message}"
    except Exception as e:
        return f"Error in DeepAI request. Exception: {str(e)}"

def generate_image(prompt, api_key):
    try:
        url = "https://api.deepai.org/api/text2img"
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key
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

@bot.message_handler(commands=['ai'])
def handle_ai_prompt(message):
    try:
        message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No prompt provided."

        # Generate content based on the provided prompt
        generated_content = generate_prompt(message_text, api_key)

        # Send generated content as a reply
        send_formatted_message(message, generated_content)

    except Exception as e:
        bot.send_message(message.chat.id, str(e))

@bot.message_handler(commands=['ai2'])
def handle_ai2_prompt(message):
    try:
        message_text = message.text.split(' ', 1)[1] if len(message.text.split()) > 1 else "No prompt provided."
        generated_image = generate_image(message_text, api_key)

        if generated_image.startswith('data:image/jpeg;base64,'):
            image_data = base64.b64decode(generated_image.replace('data:image/jpeg;base64,', ''))
            bot.send_photo(message.chat.id, image_data)
        else:
            bot.send_message(message.chat.id, generated_image)

    except Exception as e:
        bot.send_message(message.chat.id, str(e))

# Menjalankan bot
bot.polling()
