import csv
import os
from datetime import datetime
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

FILENAME = "clinic_patients.csv"

# -------------------------------
# Helper Functions
# -------------------------------

def load_data():
    """Load existing patient records from the CSV file."""
    data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data

def save_data(data):
    """Save all patient data back to the CSV file."""
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Date", "Patient ID", "Name", "Age", "Gender", "Condition", "Doctor", "Phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(Fore.YELLOW + "\nPress Enter to continue...")

# -------------------------------
# App Features
# -------------------------------

def add_patient(data):
    clear_screen()
    print(Fore.CYAN + "➕ Add New Patient Record\n")

    patient_id = f"PT-{len(data) + 1:04d}"
    name = input("Enter full name: ")
    age = input("Enter age: ")
    gender = input("Enter gender (M/F): ").upper()
    condition = input("Enter patient condition or reason for visit: ")
    doctor = input("Enter attending doctor's name: ")
    phone = input("Enter contact number: ")

    new_record = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Patient ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Condition": condition,
        "Doctor": doctor,
        "Phone": phone
    }

    data.append(new_record)
    save_data(data)
    print(Fore.GREEN + f"\n✅ Patient record added successfully! (ID: {patient_id})")
    pause()

def view_patients(data):
    clear_screen()
    if not data:
        print(Fore.RED + "No patient records found.")
        pause()
        return

    table = [
        [d["Patient ID"], d["Name"], d["Age"], d["Gender"], d["Condition"], d["Doctor"], d["Phone"], d["Date"]]
        for d in data
    ]

    print(Fore.CYAN + "📋 Patient Records\n")
    print(tabulate(
        table,
        headers=["ID", "Name", "Age", "Gender", "Condition", "Doctor", "Phone", "Date"],
        tablefmt="fancy_grid"
    ))
    pause()

def search_patient(data):
    clear_screen()
    keyword = input("🔍 Enter patient name or ID to search: ").strip().lower()

    results = [
        d for d in data
        if keyword in d["Name"].lower() or keyword in d["Patient ID"].lower()
    ]

    if results:
        print(Fore.CYAN + f"\nFound {len(results)} record(s):\n")
        table = [
            [r["Patient ID"], r["Name"], r["Age"], r["Gender"], r["Condition"], r["Doctor"], r["Phone"], r["Date"]]
            for r in results
        ]
        print(tabulate(
            table,
            headers=["ID", "Name", "Age", "Gender", "Condition", "Doctor", "Phone", "Date"],
            tablefmt="rounded_grid"
        ))
    else:
        print(Fore.RED + "⚠️ No matching patient found.")
    pause()

def delete_patient(data):
    clear_screen()
    view_patients(data)
    pid = input(Fore.YELLOW + "\nEnter the Patient ID to delete: ").strip().upper()

    for record in data:
        if record["Patient ID"] == pid:
            data.remove(record)
            save_data(data)
            print(Fore.GREEN + f"🗑️ Record for {pid} deleted successfully.")
            pause()
            return

    print(Fore.RED + "⚠️ Patient ID not found.")
    pause()

# -------------------------------
# Main Menu
# -------------------------------

def main():
    data = load_data()

    while True:
        clear_screen()
        print(Fore.YELLOW + "========= CLINIC SUBMISSION FORM =========")
        print(Fore.CYAN + "1." + Style.RESET_ALL + " Add new patient")
        print(Fore.CYAN + "2." + Style.RESET_ALL + " View all patients")
        print(Fore.CYAN + "3." + Style.RESET_ALL + " Search for a patient")
        print(Fore.CYAN + "4." + Style.RESET_ALL + " Delete a record")
        print(Fore.CYAN + "5." + Style.RESET_ALL + " Exit")
        print(Fore.YELLOW + "==========================================")

        choice = input(Fore.GREEN + "Choose an option (1–5): ").strip()

        if choice == "1":
            add_patient(data)
        elif choice == "2":
            view_patients(data)
        elif choice == "3":
            search_patient(data)
        elif choice == "4":
            delete_patient(data)
        elif choice == "5":
            clear_screen()
            print(Fore.MAGENTA + "💾 All data saved. Goodbye! 🏥👋")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice.")
            pause()

if __name__ == "__main__":
    main()
