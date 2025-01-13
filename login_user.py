from instagrapi import Client
def Login_User():
    """
    :param username: username of the account
    :param password: password of the account
    :return: client acces
    """
    cl = Client()
    username, password = get_login_info()
    try:
        cl.login(username=username, password=password)
        print("Successfully logged in")
        login_status = True
        return cl, login_status
    except Exception as e:
        print(e)
        print("Login failed")
        login_status = False
        if input("Retry login? (y/n) \t").lower() == "y":
            Login_User()
        else:
            return cl, login_status
    return cl, login_status

def get_login_info():
    """
    :return: username and password
    """
    login = input("Login: ")  # TODO: automatic login
    password = input("Password: ")
    print('Client Connected')
    return login, password