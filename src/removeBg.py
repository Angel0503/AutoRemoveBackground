import importlib

# Check if the library is installed, if not, install it
def check_install_library(library_name):
    try:
        importlib.import_module(library_name)
    except ImportError:
        print(f"The library {library_name} is not installed. Installation in progress...")
        try:
            import pip
            pip.main(['install', library_name])
            print(f"The library {library_name} has been installed successfully.")
        except:
            print(f"An error occurred while installing the library {library_name}.")

import requests
import os
from dotenv import load_dotenv

check_install_library('requests')
check_install_library('os')
check_install_library('dotenv')

load_dotenv()

path = os.getcwd()
apiKey = os.getenv("API_KEY")

# Remove background from image
def remove_bg_classic(image):
    response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(f'{path}/Images/{image}', 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': f'{apiKey}'},
        )
    if response.status_code == requests.codes.ok:
        with open(f'{path}/RemoveBgImages/{image}', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

# Remove background from image with color
def remove_bg_with_color(image, color):
    response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(f'{path}/Images/{image}', 'rb')},
            data={f'size': 'auto', 'bg_color': {color}},
            headers={'X-Api-Key': f'{apiKey}'},
        )
    if response.status_code == requests.codes.ok:
        with open(f'{path}/RemoveBgImages/{image}', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

# Get all images in Images folder
def get_all_images():
    listImg = os.listdir(path+"\Images")
    listNomImg = []
    for img in listImg:
        listNomImg.append(img.replace('.PNG', ''))
    return listNomImg

# Remove background from all images in Images folder
def remove_bg(type, images, color=None):
    if len(images) != 0:
        if type == "classic":
            for image in images:
                remove_bg_classic(image)
        elif type == "color":
            for image in images:
                remove_bg_with_color(image, color)
        else:
            print("Error in type")
    else:
        print("No images in Images folder")