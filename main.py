from login_user import *
from Commands import *
from database import *
from PIL import Image
# TODO: days/hours since last post
# TODO: UI implementation
def main():
    """
    Main function to handle user login, command execution, and posting images.
    """
    print("Welcome to the Instagram Bot")
    if input("Do you want to login? (y/n) \t").lower() == "y":
        client, login_status = Login_User()
    else:
        client = None
        login_status = False
    try:
        create_connection()
    except Exception as e:
        print("Database not found")
        print("Creating database...")
        create_table()
        print("Database created")

    post_path, specific_caption = Command(client, login_status)

    if post_path == 'image not found':
        print("return whitout posting...")
    else:
        if post_path != '':
            if check_image(post_path):
                print("Image already posted!")
                print("If not try changing the image name.")
                print("return whitout posting...")
                return
            # Load an image
            img = Image.open(post_path)
            # Display the image
            img.show()
            Post(post_path, client, specific_caption)
            insert_image(post_path)
            print('Photo uploaded')
    return None

while True:
    main()