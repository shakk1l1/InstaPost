from os.path import commonpath

from post import *

def Command(client):
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

    command = input(">> ")

    match command:
        case 'help':
            print("List of commands")
            print('exit: quit')
            print('random: post random')
            print('specific: post specific')
            print('path: path settings')
            print('get: get specific post and preview')
            Command(client)
        case "exit":
            client.logout()
            exit()
        case "random":
            specific_caption = ''
            post = Random_post()
        case "specific":
            image_name = input("image name:")
            specific_caption = input("caption (leave blank for no caption):")
            post = Specific_post(image_name)
        case "path":
            Commandpath()
            Command(client)
        case "get":
            image_name = input("image name:")
            specific_caption = ''
            post, caption = Get(image_name)
        case _:
            print("unknown command")
            print("use help for commands list")
            Command(client)
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