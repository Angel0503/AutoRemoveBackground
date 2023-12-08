import requests
import os

path = os.getcwd()+"\\AutoRemoveBackground\\"

def remove_bg_classic(image):
    response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(f'{path}BaseImage/{image}', 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'RccN4cB4cctAQWFe5janPUgL'},
        )
    if response.status_code == requests.codes.ok:
        with open(f'{path}RemoveBgImage/{image}', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

def remove_bg_with_color(image, color):
    response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(f'{path}BaseImage/{image}', 'rb')},
            data={f'size': 'auto', 'bg_color': {color}},
            headers={'X-Api-Key': 'RccN4cB4cctAQWFe5janPUgL'},
        )
    if response.status_code == requests.codes.ok:
        with open(f'{path}RemoveBgImage/{image}', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

def get_all_images():
    
    listImg = os.listdir(path+"BaseImage")
    listNomImg = []
    for img in listImg:
        listNomImg.append(img.replace('.PNG', ''))
    return listNomImg

def remove_bg(type, images, color=None):
    if len(images) != 0:
        if type == "classic":
            for image in images:
                remove_bg_classic(image)
        elif type == "color":
            for image in images:
                remove_bg_with_color(image, color)
        else:
            print("Mauvais type de remove")
    else:
        print("Le dossier d'images est vide")


remove_bg("classic", get_all_images())