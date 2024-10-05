import os
import telebot
import wget
from telebot.types import InputMediaPhoto

# Bot token
API_TOKEN = '7289248645:AAETipp-Z-YWFxP7LCT4Z9KhFNtQBpHxPOU'
bot = telebot.TeleBot(API_TOKEN)

# Directory to store downloaded images
IMAGE_DIR = 'downloaded_images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# Command handler for 'gambar'
@bot.message_handler(commands=['gambar'])
def handle_gambar(message):
    try:
        # Extract links from the message
        links = message.text.split(' ')[1].split('!')
        downloaded_files = []

        # Download each image using wget
        for link in links:
            filename = wget.download(link, out=IMAGE_DIR)
            downloaded_files.append(filename)

        # Send images in batches of 10
        for i in range(0, len(downloaded_files), 10):
            batch = downloaded_files[i:i+10]
            media_group = [InputMediaPhoto(open(file, 'rb')) for file in batch]
            bot.send_media_group(message.chat.id, media_group)

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Function to demonstrate 'not' operator and 'penuhi' command
@bot.message_handler(commands=['penuhi'])
def handle_penuhi(message):
    # Example usage of the 'not' operator
    some_condition = False  # Example condition
    if not some_condition:
        bot.reply_to(message, "Condition is not fulfilled (using 'not').")
    else:
        bot.reply_to(message, "Condition is fulfilled.")

# Start the bot
bot.polling()
