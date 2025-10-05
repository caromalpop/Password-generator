# Simple Class Registration System in Python

# Predefined list of available classes
available_classes = ["Math", "Science", "History", "English", "Art"]

# Dictionary to store student registrations
registrations = {}

def show_menu():
    print("\n=== CLASS REGISTRATION SYSTEM ===")
    print("1. View Available Classes")
    print("2. Register for a Class")
    print("3. View My Registered Classes")
    print("4. Exit")

def view_classes():
    print("\nAvailable Classes:")
    for idx, class_name in enumerate(available_classes, start=1):
        print(f"{idx}. {class_name}")

def register_class(student_name):
    view_classes()
    choice = input("Enter the class name you want to register for: ").strip()

    if choice not in available_classes:
        print("Class not found. Please enter a valid class name.")
        return

    # Adding student to the registration dictionary
    if student_name not in registrations:
        registrations[student_name] = []

    if choice in registrations[student_name]:
        print("⚠️ You are already registered for this class.")
    else:
        registrations[student_name].append(choice)
        print(f"✅ {student_name} successfully registered for {choice}.")

def view_my_classes(student_name):
    if student_name not in registrations or not registrations[student_name]:
        print("You are not registered for any classes.")
    else:
        print("\nYour Registered Classes:")
        for cls in registrations[student_name]:
            print(f"{cls}")


print("Welcome to the School Class Registration System!")
student_name = input("Please enter your name: ").strip()

while True:
    show_menu()
    option = input("Choose an option (1-4): ")

    if option == "1":
        view_classes()
    elif option == "2":
        register_class(student_name)
    elif option == "3":
        view_my_classes(student_name)
    elif option == "4":
        print("Goodbye! 👋")
        break
    else:
        print("❗ Invalid option. Please choose 1, 2, 3, or 4.")
