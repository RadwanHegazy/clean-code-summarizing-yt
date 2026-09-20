
users = []

# wrong
def save_user (username, gmail, password) : 

    # validation 
    if len(password) < 8 : 
        raise Exception("Password length must be greater than 8")

    if not gmail.endswith("@gmail.com") : 
        raise Exception("Please enter a valid gmail account")

    # save user
    users.append(username)

    # send welcome message
    print(f"Sending welcome email to user : ", gmail)


