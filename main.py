from login_user import *
from Commands import *
from database import insert_image, check_image
from PIL import Image

def main():
    """
    Main function to handle user login, command execution, and posting images.
    """
    login = input("Login: ") #TODO: automatic login
    password = input("Password: ")
    client = Login_User(login, password)
    # TODO: days/hours since last post
    #TODO: UI implementation
    print('Client Connected')

    post_path, specific_caption = Command(client)

    if post_path == 'image not found':
        print("return whitout posting...")
    else:
        if post_path != '':
            # Load an image
            img = Image.open(post_path)
            # Display the image
            img.show()
            Post(post_path, client, specific_caption)
            print('photo uploaded')
    return None

while True:
    main()