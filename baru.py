import os
import openai
import requests
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import telebot

# Set OpenAI credentials (placeholders for the purpose of this example)
org_entry = ''
api_key_entry = ''

# Function to set OpenAI credentials
def set_openai_credentials():
    openai.organization = org_entry
    openai.api_key = api_key_entry

# Function to read prompt from a file
def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

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

# Command handler for the Telegram bot to generate an image based on the input number
@bot.message_handler(commands=['gambarin'])
def handle_gambarin_command(message):
    # Extract the number from the message text
    try:
        # Split the message text by space and get the second part as the number
        file_number = int(message.text.split()[1])
        if 1 <= file_number <= 3:
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
        bot.reply_to(message, "Please send a valid command followed by a number between 1 and 3. Example: /gambarin 2")

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

# Command handler for the Telegram bot to generate an image based on the input text
@bot.message_handler(commands=['ai_image'])
def handle_gambarin_command(message):
    # Use the message text after the command as the prompt
    prompt = message.text.partition(' ')[2]  # This will get the text after the command
    if prompt:
        image = generate_image(prompt)
        if image:
            save_image(image)
            with open("temp.png", "rb") as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.reply_to(message, "Failed to generate image.")
    else:
        bot.reply_to(message, "Please send a prompt after the command. Example: /ai_image your prompt here")