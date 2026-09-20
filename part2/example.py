
# Wrong
if len(password) < 8 : 
    raise Exception("Password length must be greater than 8")

if not gmail.endswith("@gmail.com") : 
    raise Exception("Please enter a valid gmail account")


# Correct

class PasswordLengthError(Exception) : ...
class InvalidGmail(Exception) : ...


if len(password) < 8 : 
    raise PasswordLengthError("Password length must be greater than 8")

if not gmail.endswith("@gmail.com") : 
    raise InvalidGmail("Please enter a valid gmail account")

