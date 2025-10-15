import csv
import os
from datetime import datetime
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

FILENAME = "calories.csv"

# ------------------------------
# Helper Functions
# ------------------------------

def load_calories():
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data

def save_calories(data):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Date", "Meal", "Calories"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")

# ------------------------------
# Core App Functions
# ------------------------------

def add_meal(data):
    clear_screen()
    print(Fore.CYAN + "➕ Add a Meal")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    meal = input("Enter meal name: ")
    try:
        calories = float(input("Enter calories: "))
    except ValueError:
        print(Fore.RED + "⚠️ Invalid number for calories!")
        pause()
        return

    data.append({
        "Date": date,
        "Meal": meal,
        "Calories": f"{calories:.2f}"
    })
    save_calories(data)
    print(Fore.GREEN + "✅ Meal added and saved!")
    pause()

def view_meals(data):
    clear_screen()
    if not data:
        print(Fore.RED + "No meals recorded.")
        pause()
        return

    table_data = [[i+1, e["Date"], e["Meal"], f"{float(e['Calories']):,.2f}"] for i, e in enumerate(data)]
    print(Fore.CYAN + "📋 All Meals\n")
    print(tabulate(table_data, headers=["#", "Date", "Meal", "Calories"], tablefmt="fancy_grid"))
    pause()

def total_calories(data):
    clear_screen()
    total = sum(float(e["Calories"]) for e in data)
    print(Fore.MAGENTA + f"💪 Total Calories Consumed: {total:,.2f} kcal")
    pause()

def calories_by_day(data):
    clear_screen()
    if not data:
        print(Fore.RED + "No meals recorded.")
        pause()
        return

    day_totals = {}
    for e in data:
        day_totals[e["Date"]] = day_totals.get(e["Date"], 0) + float(e["Calories"])

    table_data = [[day, f"{total:,.2f}"] for day, total in day_totals.items()]
    print(Fore.CYAN + "📊 Calories by Day\n")
    print(tabulate(table_data, headers=["Date", "Total Calories"], tablefmt="rounded_grid"))
    pause()

def delete_meal(data):
    clear_screen()
    if not data:
        print(Fore.RED + "No meals to delete.")
        pause()
        return

    view_meals(data)
    try:
        index = int(input("Enter meal number to delete: ")) - 1
        if 0 <= index < len(data):
            removed = data.pop(index)
            save_calories(data)
            print(Fore.GREEN + f"✅ Deleted meal: {removed['Meal']} ({removed['Calories']} kcal)")
        else:
            print(Fore.RED + "⚠️ Invalid number.")
    except ValueError:
        print(Fore.RED + "⚠️ Enter a valid number.")
    pause()

# ------------------------------
# Main Menu
# ------------------------------

def main():
    data = load_calories()

    while True:
        clear_screen()
        print(Fore.YELLOW + "========= CALORIE TRACKER =========")
        print(Fore.CYAN + "1." + Style.RESET_ALL + " View all meals")
        print(Fore.CYAN + "2." + Style.RESET_ALL + " Add a meal")
        print(Fore.CYAN + "3." + Style.RESET_ALL + " View total calories")
        print(Fore.CYAN + "4." + Style.RESET_ALL + " View calories by day")
        print(Fore.CYAN + "5." + Style.RESET_ALL + " Delete a meal")
        print(Fore.CYAN + "6." + Style.RESET_ALL + " Exit")
        print(Fore.YELLOW + "===================================")

        choice = input(Fore.GREEN + "Choose an option (1–6): ").strip()

        if choice == "1":
            view_meals(data)
        elif choice == "2":
            add_meal(data)
        elif choice == "3":
            total_calories(data)
        elif choice == "4":
            calories_by_day(data)
        elif choice == "5":
            delete_meal(data)
        elif choice == "6":
            clear_screen()
            print(Fore.MAGENTA + "💾 All data saved. Goodbye! 👋")
            break
        else:
            print(Fore.RED + "⚠️ Invalid option. Try again.")
            pause()

if __name__ == "__main__":
    main()
