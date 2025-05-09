import hashlib

user_database={

}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username,password):
    if username in user_database:
        print("Username already exists. Please choose a different username")
    else:
        hashed_password=hash_password(password)
        user_database[username]=hashed_password
        print("User register successfully!")
def login_user(username, password):
    if username not in user_database:
        print("Username not found. Please register first")
    else:
        hashed_password=hash_password(password)
        if user_database[username]==hashed_password:
            print("Login successful! Welcome back!")
        else:
            print("Incorrect password. Please try again")

while True:
    print('Select: 1. register 2. Login  3. Exit')
    choice=int(input("Enter your choice:"))

    if choice==1:
        username=input("Enter a username")
        password=input("Enter a password")
        register_user(username,password)
    elif choice==2:
        username=input("Enter your Username: ")
        password=input("Enter your password: ")
        login_user(username, password)
    elif choice==3:
        print("Exit")
        break
    else:
        print("Invalid choice. Try again")

