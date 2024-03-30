import os
import openai
import requests
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def set_openai_credentials():
    openai.organization = org_entry
    openai.api_key = api_key_entry

def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_image():
    set_openai_credentials()
    prompt = read_prompt_from_file('ai.txt')
    global response
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

    image = Image.open("image.jpg")
    image = image.resize((7240, 7240))
    return image

def save_image(image):
    file_path = "image.jpg"
    plt.imsave(file_path, np.array(image))

    return "Image saved successfully."

org_entry = ''
api_key_entry = ''

image = generate_image()

# Display the image using matplotlib
plt.imshow(image)
plt.axis('off')
plt.show()

save_image(image)
