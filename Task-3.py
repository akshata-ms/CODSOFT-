import random
import string

def generate_password(length, include_uppercase, include_digits, include_symbols):
    # Start with lowercase letters
    characters = string.ascii_lowercase

    # Add character types based on user preferences
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get the desired password length from the user
    length = int(input("Enter the desired length of the password: "))

    # Ask the user what types of characters to include in the password
    print("Type 'y' for yes and 'n' for no")
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, include_uppercase, include_digits, include_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
