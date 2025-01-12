from os.path import commonpath

from post import *

def Command(client):
    command = input("Command: ")

    match command:
        case 'help':
            print("List of commands")
            print('exit: quit')
            print('random: post random')
            print('specific: post specific')
            print('path: path settings')
            print('get: get specific post and preview')
            Command(client)
            specific_caption = ''
            post = ''
        case "exit":
            exit()
        case "random":
            specific_caption = ''
            post = Random_post(client)
        case "specific":
            image_name = input("image name:")
            specific_caption = input("caption (leave blank for no caption):")
            post = Specific_post(client, image_name, specific_caption)
        case "path":
            Commandpath()
            Command(client)
            specific_caption = ''
            post = ''
        case "get":
            image_name = input("image name:")
            specific_caption = ''
            post, caption = Get(image_name)
    return post, specific_caption


def Commandpath():
    c_p = input('Command-path: ')
    match c_p:
        case 'help':
            print("List of commands")
            print('exit: quit')
            print('esc: escape')
            print('path: show existing path')
            print('new: create new path')
            Commandpath()
        case "exit":
            exit()
        case "esc":
            return None
        case "path":
            f = open("path.py", "r")
            print(f.read())
            f.close()
        case "new":
            new_path = input('new path:')
            with open('path.py', 'w') as f:
                f.write('path = ' + "'" + new_path + "'")

    return None