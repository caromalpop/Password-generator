#Password generator!
import random
import string

length = int(input("Enter the length of the password: "))
use_letters = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

characters = ""

if use_letters:
    characters += string.ascii_letters  # a-z + A-Z
if use_digits:
    characters += string.digits         # 0-9
if use_special:
    characters += string.punctuation    # !@#$%^&*() etc.

if not characters:
    print("You need to choose at least one character type!")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))
print("Generated Password:", password)