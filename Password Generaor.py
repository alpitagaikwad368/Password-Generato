import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

print("Choose password type:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    characters = string.ascii_letters
elif choice == 2:
    characters = string.ascii_letters + string.digits
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)