print("👋 Welcome to MindPal, your daily brain workout!")
print("1. Register")
print("2. Login")
print("3. Exit")

def register():
    print("📝 New User Registration")
    name = input("Enter your full name: ")
    username = input("Choose a username: ")
    if name and username:
        print("✅ Registration completed successfully!")

def login():
    print("🔐 User Login")
    username = input("Enter your username: ")
    print(f"✅ Welcome back, {username}!")

choice = input("Enter your choice: ")
if choice == "1":
    register()
elif choice == "2":
    login()
elif choice == "3":
    print("Exiting...")
else:
    print("Pick a damn choice from the menu!")





