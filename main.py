from login_user import *
from post import *
from PIL import Image
from Commands import *

def main():
    login = input("Login: ") #TODO: automatic login
    password = input("Password: ")
    client = Login_User(login, password)

    print('Client Connected')

    post_path, specific_caption = Command(client)

    if post_path == 'image not found':
        print("Exiting whitout posting...")
        exit()
    else:
        if post_path != '':
            # Load an image
            img = Image.open(post_path)
            # Display the image
            img.show()
            Post(post_path, client, specific_caption)
            print('photo uploaded')
            exit()
    return None

main()