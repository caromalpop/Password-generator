# 🌦️ Weather Display App
# This program shows real-time weather info for any city using OpenWeatherMap API.

import requests  # This lets Python send web requests (make sure requests is installed)

# Step 1: Add your API key from OpenWeatherMap
API_KEY = "8129b82efef7908190b95bf83850d1e2"  # ← Replace with your actual key
BASE_URL = "https://home.openweathermap.org/api_keys"

# Step 2: Start the main program loop
while True:
    print("\n--- 🌍 Weather Display App ---")
    city = input("Enter a city name (or type 'exit' to quit): ")

    if city.lower() == "exit":
        print("👋 Goodbye!")
        break  # Exit the loop and end the program

    # Step 3: Build the API URL with the city name, key, and metric units
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    # Step 4: Send a request to the API
    try:
        response = requests.get(url)
        data = response.json()  # Convert the JSON response into a Python dictionary

        # Step 5: Check if city exists
        if response.status_code == 200:
            # Extract key information
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()
            wind_speed = data["wind"]["speed"]

            # Step 6: Display the weather details
            print(f"\n📍 Location: {city_name}, {country}")
            print(f"🌡️ Temperature: {temperature}°C")
            print(f"🥵 Feels like: {feels_like}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬️ Wind Speed: {wind_speed} m/s")
            print(f"☁️ Condition: {description}")

        elif response.status_code == 404:
            print("❌ City not found. Please check the spelling and try again.")
        else:
            print("⚠️ Unable to fetch data. Please try again later.")
    except Exception as e:
        print("🚫 Error:", e)
