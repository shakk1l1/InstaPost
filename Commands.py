from os.path import commonpath
from database import *
from login_user import *

from post import *

def Command(client, login_status, login_status_string):
    """
    Handle user commands and return the image path and caption.

    :param client: Client access
    :return: Tuple containing the image path and caption
    """
    f = open("path.py", "r")
    if f.read() == "path = ''":
        print("Path to folder not specified.")
        print("please specify the folder path using: path -> new.")
    f.close()

    command = input(login_status_string+" >> ")

    match command:
        case 'help':
            print("List of commands")
            print('exit: quit')
            print('random: post random')
            print('specific: post specific')
            print('path: path settings')
            print('get: get specific post and preview')
            print('add: add image to database')
            print('list: list all images in database')
            print('connect: connect to instagram')
            Command(client, login_status, login_status_string)
        case "exit":
            try:
                print("Logging out...")
                client.logout()
            except Exception as e:
                print('User was not logged in')
            exit()
        case "random":
            if login_status:
                specific_caption = ''
                post = Random_post()
            else:
                print("Please login to use this command")
                Command(client, login_status, login_status_string)
        case "specific":
            if login_status:
                image_name = input("image name:")
                specific_caption = input("caption (leave blank for no caption):")
                post = Specific_post(image_name)
            else:
                print("Please login to use this command")
                Command(client, login_status, login_status_string)
        case "path":
            Commandpath()
            Command(client, login_status, login_status_string)
        case "get":
            image_name = input("image name:")
            specific_caption = ''
            post, caption = Get(image_name)
            Command(client, login_status, login_status_string)
        case "add":
            image_name = input("image name:")
            insert_image(image_name)
            print("Image added to database")
            Command(client, login_status, login_status_string)
        case "list":
            list_images()
            Command(client, login_status, login_status_string)
        case "connect":
            if not login_status:
                client, login_status = Login_User()
                if login_status:
                    login_status_string = "(connected)"
                else:
                    login_status_string = "(not connected)"
            else:
                print("Already connected")
            Command(client, login_status, login_status_string)
        case _:
            print("unknown command")
            print("use help for commands list")
            Command(client, login_status, login_status_string)
    return post, specific_caption


def Commandpath():
    """
    Handle path-related commands for setting and displaying the folder path.
    """
    c_p = input('>> -path ')
    match c_p:
        case 'help':
            print("List of commands")
            print('esc: escape')
            print('show: show existing path')
            print('new: create new path')
            Commandpath()
        case "esc":
            return None
        case "show":
            f = open("path.py", "r")
            print(f.read())
            f.close()
            Commandpath()
        case "new":
            new_path = input('new path:')
            with open('path.py', 'w') as f:
                f.write('path = ' + "'" + new_path + "'")
            print("Path saved!")
            Commandpath()
        case _:
            print("unknown command")
            print("use help for commands list")
            Commandpath()

    return None