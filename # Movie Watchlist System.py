#  Movie Watchlist System

# File name for saving your watchlist
filename = "movie_watchlist.txt"

# Function to load movies from file
def load_movies():
    try:
        with open(filename, "r") as file:
            movies = [line.strip() for line in file.readlines()]
            return movies
    except FileNotFoundError:
        return []  # Return empty list if no file yet

# Function to save movies to file
def save_movies(movies):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

# Loading any existing movies at startup
movie_list = load_movies()

# Main program loop
while True:
    print("\n--- Movie Watchlist Menu ---")
    print("1. Add a movie")
    print("2. View your watchlist")
    print("3. Remove a movie")
    print("4. Clear entire list")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    # Adding movie
    if choice == "1":
        movie = input("Enter the movie name to add: ")
        movie_list.append(movie)
        save_movies(movie_list)
        print(f". '{movie}' added to your watchlist.")

    # Viewing movies
    elif choice == "2":
        if not movie_list:
            print(" Your watchlist is empty.")
        else:
            print("\n Your Watchlist:")
            for i, movie in enumerate(movie_list, start=1):
                print(f"{i}. {movie}")

    # Removing a movie
    elif choice == "3":
        movie = input("Enter the movie name to remove: ")
        if movie in movie_list:
            movie_list.remove(movie)
            save_movies(movie_list)
            print(f" '{movie}' has been removed.")
        else:
            print(" Movie not found in your watchlist.")

    # Clearing the entire list
    elif choice == "4":
        confirm = input("Are you sure you want to clear the whole list? (y/n): ").lower()
        if confirm == "y":
            movie_list.clear()
            save_movies(movie_list)
            print("🧹 Watchlist cleared.")

    # Exitting program
    elif choice == "5":
        print(" Goodbye! Your watchlist has been saved.")
        break

    # Handling invalid inputs
    else:
        print("❗ Invalid choice. Please select a number between 1–5.")
