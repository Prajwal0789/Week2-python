users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_users():
    user_id = int(input("Enter user ID: "))
    name = input("Enter name: ")
    email = input("Enter email: ")

    for user in users:
        if user["id"] == user_id:
            print("The user already exists.")
            return
    
    users.append({"id": user_id, "name": name, "email": email})
    print(f"New user {user_id} is added.")

def read_users():
    user_id = int(input("Enter the user ID to be read: "))
    for user in users:
        if user["id"] == user_id:
            print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")
            return
    print("User not found.")

def delete_users():
    user_id = int(input("Enter the user ID to be deleted: "))
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print(f"User {user_id} deleted.")
            return
    print("User not found.")

def update_users():
    user_id = int(input("Enter the user ID to be updated: "))
    for user in users:
        if user["id"] == user_id:
            user["name"] = input("Enter the updated name: ")
            user["email"] = input("Enter the updated email: ")
            print(f"User {user_id} updated.")
            return
    print("User doesn't exist.")

print("The CRUD operations")
N = 0
while N != 5:
    print("\nEnter 1 to Add a User")
    print("Enter 2 to Read User")
    print("Enter 3 to Delete the User")
    print("Enter 4 to Update user info")
    print("Enter 5 to Exit")
    
    N = int(input("Choose an option: "))
    
    if N == 1:
        add_users()
    elif N == 2:
        read_users()
    elif N == 3:
        delete_users()
    elif N == 4:
        update_users()
    elif N == 5:
        print("Exiting program.")
