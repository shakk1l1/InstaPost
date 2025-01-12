import os
from caption_generation import *
from path import *
import random
from PIL import Image

def Specific_post(client, image_name, specific_caption):
    '''
    :param client: Client acces
    :param image_name: name of the specified photo
    :return: name of the specified photo if found, image not found otherwise
    '''
    images = os.listdir(path)
    if image_name in images:
        print('photo found')
        image_path = os.path.join(images, image_name)
    else:
        print('photo not found')
        image_path = 'image not found'
    return image_path

def Random_post(client):
    images = os.listdir(path)
    index = random.randint(0, len(images)-1)
    image_path = os.path.join(images, images[index])
    Post(client, image_path)
    return images[index]

def Post(image_path, client, specific_caption = ''):
    caption = Caption_generation(image_path, specific_caption)
    client.photo_upload(path=image_path, caption=caption)
    os.remove(image_path)
    print(f"Posted and removed image: {image_path}")

def Get(image_name):
    '''
    :param client: Client acces
    :param image_name: name of the specified photo
    :return: name of the specified photo if found, image not found otherwise
    '''
    images = os.listdir(path)
    if image_name in images:
        print('photo found')
        image_path = os.path.join(path, image_name)
        caption = Caption_generation(image_path)
        # Load an image
        img = Image.open(image_path)
        # Display the image
        img.show()
        print(caption)
    else:
        print('photo not found')
        image_path = 'image not found'
        caption = ''
    return image_path, caption