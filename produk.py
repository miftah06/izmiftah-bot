import openai
from PIL import Image
import numpy as np
import pandas as pd
import requests

def identify_image(image_path, openai_apikey):
    try:
        # Mengatur kunci API OpenAI
        openai.api_key = openai_apikey

        # Membaca gambar sebagai objek PIL
        image = Image.open(image_path)

        # Mengonversi gambar ke dalam format yang dapat digunakan oleh OpenAI
        image_data = np.array(image)
        image_data = image_data.tolist()

        # Memanggil API Vision OpenAI
        response = openai.Image.create(model="image-classification-v3", images=image_data)

        # Mengambil label-label hasil identifikasi
        labels_list = response["output"]["labels"]
        return "This image contains: {}".format(", ".join(labels_list))
    except Exception as e:
        print(e)
        return "Failed to identify the image."

def process_image(image_path, openai_apikey):
    try:
        # Identifikasi gambar menggunakan OpenAI
        result = identify_image(image_path, openai_apikey)
        return result
    except Exception as e:
        print(e)
        return "Failed to process the image."

# Contoh penggunaan
if __name__ == "__main__":
    foto_path = 'temp.png'
    result = process_image(foto_path, openai_apikey)
    print(result)
