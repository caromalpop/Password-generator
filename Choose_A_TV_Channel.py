channels = ["HBO", "CNN", "ESPN", "FOX", "NBC"]
print("Available TV Channels:")
for index, channel in enumerate(channels, start=1):
    print(f"{index}. {channel}")
choice = int(input("Select a channel by entering its number (1-5): "))
if 1 <= choice <= len(channels):
    print(f"You have selected {channels[choice - 1]}. Enjoy your show!")
else:
    print("Invalid selection. Please choose a number between 1 and 5.")     
    