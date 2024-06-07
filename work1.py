"""
A password generator is a useful tool that generates strong and random passwords for users.
This project aims to create a password generator application using Python, allowing users to
specify the length and complexity of the password.
"""
import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password of the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            print("Invalid input. Please enter a positive integer.")
            return

        generated_password = generate_password(desired_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

