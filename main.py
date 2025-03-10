# main.py
import asyncio
from login_user import *
from Commands import *
from database import create_table, check_image, insert_image
from PIL import Image

async def main():
    """
    Main function to handle user login, command execution, and posting images.
    """
    if input("Do you want to login? (y/n) \t").lower() == "y":
        client, login_status = await Login_User()
        login_status_string = "(connected)" if login_status else "(not connected)"
    else:
        client = None
        login_status = False
        login_status_string = "(not connected)"

    try:
        db.get_connection()
        print("Database found")
    except Exception as e:
        print("Database not found")
        print("Creating database...")
        create_table()
        print("Database created")

    post_path, specific_caption = await Command(client, login_status, login_status_string)

    if post_path == 'image not found':
        print("return without posting...")
    else:
        if post_path != '':
            if check_image(post_path):
                print("Image already posted!")
                print("If not, try changing the image name.")
                print("return without posting...")
                return
            # Load and display the image
            img = Image.open(post_path)
            img.show()
            await Post(post_path, client, specific_caption)
            insert_image(post_path)
            print('Photo uploaded')
    return None

print("Welcome to the Instagram Bot")
asyncio.run(main())