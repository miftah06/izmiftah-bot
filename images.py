import os
import pandas as pd
import numpy as np
import openai
from PIL import Image
import requests

def manipulate_image(image_path):
    try:
        # Manipulasi gambar menggunakan PIL
        img = Image.open(image_path)
        # Manipulasi gambar sesuai kebutuhan
        img = img.resize((800, 600))
        img = img.convert("L")  # Grayscale

        # Simpan gambar yang sudah dimanipulasi
        img.save('foto.png', 'wb')  # Menimpa foto.png yang sudah ada

        return "Image manipulated successfully."
    except Exception as e:
        print(e)
        return "Failed to manipulate the image."

def export_image(image_path):
    try:
        # Export gambar ke dalam 'foto.png'
        img = Image.open(image_path)
        # Manipulasi gambar sesuai kebutuhan
        img.save('foto.png', 'wb')  # Menimpa foto.png yang sudah ada

        return "Image exported successfully."
    except Exception as e:
        print(e)
        return "Failed to export the image."

def create_image_with_openai(image_path):
    try:
        # Menggunakan OpenAI API untuk membuat gambar dengan model GPT-3.5-turbo
        openai.api_key = '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'
        response = openai.Image.create(model="gpt-3.5-turbo", file=open(image_path, "rb"))
        image_url = response["url"]

        # Mendownload gambar hasil dari OpenAI API
        img_response = requests.get(image_url)
        with open('openai_image.png', 'wb') as img_file:
            img_file.write(img_response.content)

        return "Image created with OpenAI successfully."
    except Exception as e:
        print(e)
        return "Failed to create image with OpenAI."

class ImageExporter:
    def __init__(self, image_path):
        self.image_path = image_path

    def export_image(self):
        try:
            # Export gambar ke dalam 'foto.png'
            img = Image.open(self.image_path)
            # Manipulasi gambar sesuai kebutuhan
            img.save('foto.png')

            return "Image exported successfully."
        except Exception as e:
            print(e)
            return "Failed to export the image."

def notify_uploaded():
    try:
        # Notifikasi bahwa 'foto.png' sudah diunggah
        return "Terima kasih! File foto.png sudah diunggah."
    except Exception as e:
        print(e)
        return "Failed to notify."

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    image_path = "foto.png"
    manipulate_image(image_path)
    create_image_with_openai(image_path)
    export_image(image_path)
    image_exporter = ImageExporter(image_path)
    image_exporter.export_image()
    notify_uploaded()
