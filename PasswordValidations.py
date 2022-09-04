# Program to check the validity of password given by user
import re

while True:
    user_name = input("Enter a Username : ")
    password = input("Enter a Password : ")
    is_valid = False

    if len(password) < 6 or len(password) > 12:
        print("Not valid. Total no. of characters should be between 6 and 12")
        continue
    elif not re.search("[A-Z]", password):
        print("Not valid. It should contain one letter between A-Z")
        continue
    elif not re.search("[a-z]", password):
        print("Not valid. It should contain one letter between a-z")
        continue
    elif not re.search("[0-9]", password):
        print("Not valid. It should contain one number between 0-9")
        continue
    elif not re.search("[$#@]", password):
        print("Not valid. It should contain at least one special character from $#@")
        continue
    else:
        is_valid = True
        break

if is_valid:
    print("Password is valid.")
