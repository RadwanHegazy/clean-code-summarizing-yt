
users = []

def validate_data (gmail : str, password : str) -> None :

    if len(password) < 8 : 
        raise Exception("Password length must be greater than 8")

    if not gmail.endswith("@gmail.com") : 
        raise Exception("Please enter a valid gmail account")


def send_welcome_msg(gmail : str) -> None :
    print(f"Sending welcome email to user : ", gmail)








def save_user (username : str, gmail : str, password : str) -> None: 
    validate_data(gmail, password)
    users.append(username)
    send_welcome_msg(gmail)

