from instagrapi import Client
def Login_User(username, password):
    """
    :param username: username of the account
    :param password: password of the account
    :return: client acces
    """
    cl = Client()
    cl.login(username=username, password=password)
    print("Successfully logged in")
    return cl