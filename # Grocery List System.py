#  Grocery List System

# Step 1: Create an empty list to store grocery items
grocery_list = []

# Step 2: Start an infinite loop so the user can keep using the app
while True:
    # Step 3: Show the user a menu of options
    print("\n--- Grocery List Menu ---")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")

    # Step 4: Ask the user what they want to do
    choice = input("Enter your choice (1-4): ")

    # Step 5: Option 1 - Add item
    if choice == "1":
        item = input("Enter the item to add: ")
        grocery_list.append(item)  # Adds the item to the list
        print(f".'{item}' has been added to your grocery list.")

    # Step 6: Option 2 - View items
    elif choice == "2":
        if len(grocery_list) == 0:
            print("Your grocery list is empty.")
        else:
            print("\n Grocery List:")
            for i, item in enumerate(grocery_list, start=1):
                print(f"{i}. {item}")

    # Step 7: Option 3 - Remove item
    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f". '{item}' has been removed from your grocery list.")
        else:
            print("Item not found in your list.")

    # Step 8: Option 4 - Exit the program
    elif choice == "4":
        print("Goodbye! Thanks for using the Grocery List System.")
        break  # Stops the loop and ends the program

    # Step 9: Handle invalid inputs
    else:
        print("❗ Invalid choice. Please enter a number between 1 and 4.")
