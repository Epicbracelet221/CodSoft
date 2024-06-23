import string
import random

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Ensure the password has at least one lowercase letter, one uppercase letter, one digit, and one special character
    characters = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with a mix of all character types
    all_characters = string.ascii_letters + string.digits + string.punctuation
    characters += random.choices(all_characters, k=length - 4)

    # Shuffle the characters to ensure randomness
    random.shuffle(characters)

    # Join the list into a string
    password = ''.join(characters)
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number greater than or equal to 4.")

if __name__ == "__main__":
    main()
