import os
from caption_generation import *
from path import *
import random
from PIL import Image

def Specific_post(client, image_name, specific_caption):
    """
    Find a specific image by name and return its path.

    :param client: Client access
    :param image_name: Name of the specified photo
    :param specific_caption: Caption for the specific post
    :return: Path of the specified photo if found, 'image not found' otherwise
    """
    images = os.listdir(path)
    if image_name in images:
        print('photo found')
        image_path = os.path.join(path, image_name)
    else:
        print('photo not found')
        image_path = 'image not found'
    return image_path

def Random_post(client):
    """
    Select a random image from the directory and return its path.

    :param client: Client access
    :return: Path of the randomly selected photo
    """
    images = os.listdir(path)
    index = random.randint(0, len(images)-1)
    image_path = os.path.join(path, images[index])
    return image_path

def Post(image_path, client, specific_caption = ''):
    """
    Post an image with a generated caption and remove the image from the directory.

    :param image_path: Path of the image to post
    :param client: Client access
    :param specific_caption: Specific caption for the post
    """
    caption = Caption_generation(image_path, specific_caption)
    client.photo_upload(path=image_path, caption=caption)
    os.remove(image_path) # TODO: instead of removing puting in database
    print(f"Posted and removed image: {image_path}")

def Get(image_name):
    """
    Get a specific image by name, generate its caption, and display the image.

    :param image_name: Name of the specified photo
    :return: Tuple containing the path of the specified photo and its caption
    """
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