# -------- 1 -------

x = [] # Wrong
lst = [] # Wrong
data_list = [] # Wrong

active_users = [] # correct
active_users_group = [] # correct


# -------- 2 -------

"""

Snake Case : variable_name , number_of_users

Pascal Case : Users, ClassName

Camel Case : className, variableName

"""

ActiveUsers = [] # wrong
active_users = [] # correct

def GetActiveUsers() :  # Wrong
    return []

def get_active_users() : # Correct
    return []


# Wrong
class class_name :
    pass


# Correct
class ClassName:
    pass

# -------- 3 -------


# Wrong Code

def calculate_discount(price) : 
    return price - (price * 0.10)


# Correct Code

DISCOUNT_RATE = 0.10

def calculate_discount(price) : 
    return price - (price * DISCOUNT_RATE)



    