import random
import time
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# Dictionary of fact categories
facts = {
    "Science": [
        "Bananas are slightly radioactive due to their potassium content!",
        "Honey never spoils — archaeologists found 3000-year-old edible honey in Egyptian tombs.",
        "Octopuses have three hearts and blue blood.",
        "A day on Venus is longer than a year on Venus.",
        "There are more trees on Earth than stars in the Milky Way galaxy!"
    ],
    "Technology": [
        "The first computer virus was created in 1986 and was called the Brain virus.",
        "The first email was sent in 1971 by Ray Tomlinson to himself.",
        "There’s more computing power in your phone than was used to land Apollo 11 on the moon.",
        "You can fit the entire internet from 1997 on a modern USB stick!",
        "Every minute, 500+ hours of content are uploaded to YouTube."
    ],
    "Animals": [
        "Cows have best friends and get stressed when separated.",
        "Sloths can hold their breath longer than dolphins can!",
        "Penguins propose to their mates with pebbles.",
        "Butterflies taste with their feet.",
        "An ostrich’s eye is bigger than its brain."
    ],
    "Space": [
        "Neutron stars can spin 600 times per second!",
        "If you could fly a plane to Pluto, it would take over 800 years.",
        "The footprints on the Moon will likely stay there for millions of years.",
        "Saturn could float in water if there was a bathtub big enough.",
        "In space, astronauts grow up to 2 inches taller due to lower gravity."
    ]
}

def display_header():
    print(Fore.CYAN + Style.BRIGHT + "\n🌍✨ Welcome to the Random Facts App! ✨🌍")
    print(Fore.YELLOW + "------------------------------------------")

def show_categories():
    table_data = [[i+1, category] for i, category in enumerate(facts.keys())]
    print(tabulate(table_data, headers=[Fore.GREEN + "No.", Fore.GREEN + "Category"], tablefmt="fancy_grid"))

def get_random_fact(category):
    fact = random.choice(facts[category])
    return fact

def main():
    while True:
        display_header()
        show_categories()

        try:
            choice = int(input(Fore.WHITE + "\n👉 Choose a category number (or 0 to exit): "))
            if choice == 0:
                print(Fore.MAGENTA + "\nThanks for using the Random Facts App! Goodbye 👋\n")
                break

            category_list = list(facts.keys())
            if 1 <= choice <= len(category_list):
                selected_category = category_list[choice - 1]
                print(Fore.CYAN + f"\n💡 Random {selected_category} Fact:\n")
                print(Fore.LIGHTWHITE_EX + get_random_fact(selected_category))
                print(Fore.YELLOW + "\n------------------------------------------")
                time.sleep(1)
            else:
                print(Fore.RED + "⚠️ Invalid choice, please select a valid number.\n")

        except ValueError:
            print(Fore.RED + "⚠️ Please enter a valid number.\n")

        input(Fore.GREEN + "\nPress Enter to continue...\n")
        print("\n" * 2)

if __name__ == "__main__":
    main()

