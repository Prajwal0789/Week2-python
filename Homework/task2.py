import re
print("Enter the email to be checked ")
email=input()

def is_valid_email(email):
    valid=re.match(r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$',email)
    if valid:
        print("The email is valid")
    else:
        print("The email is not Valid")

is_valid_email(email)
