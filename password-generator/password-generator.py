import random
import string 

def generate_password(password_length, uppercase_chars, has_digits, special_chars):
    """Password Generation Logic"""

    password_chars = ''

    # LENGTH VALIDATION
    if password_length < (uppercase_chars + has_digits + special_chars):
        raise ValueError('Password too short.')

    # Guaranteeing password will include what users selected
    if uppercase_chars:
        password_chars += random.choice(string.ascii_uppercase)
    if has_digits:
        password_chars += random.choice(string.digits)
    if special_chars:
        password_chars += random.choice(string.punctuation)

    # BUILDING THE CHARACTER SET
    characters = string.ascii_lowercase
    if uppercase_chars:
        characters += string.ascii_uppercase
    if has_digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    # Generate the full password based on users password length with any remaining characters after the user chooses uppercase, numbers, and special characters.
    for _ in range(password_length - len(password_chars)):
        password_chars += random.choice(characters)

    # SHUFFLING PASSWORD TO BE UNPREDICTABLE
    password = list(password_chars)
    random.shuffle(password)
    return ''.join(password)
    
    
def main():
    
    print("\n====================== WELCOME TO PASSWORD GENERATOR ==========================\n")

    # 1. INPUT COLLECTION
    password_length = int(input("How many characters would you like your password to have: "))
    uppercase_chars = input("Would you like your password to have uppercase characters? (y/n): ").lower().strip() == 'y'
    has_digits = input("Would you like your password to have digits? (y/n): ").lower().strip() == 'y'
    special_chars = input("Would you like your password to have special characters? (y/n): ").lower().strip() == 'y'

    # CALLING generate_password() WITH ERROR HANDLING
    try:
        final_password = generate_password(password_length, uppercase_chars, has_digits, special_chars)
    except ValueError as e:
        print(e)

    # DISPLAYING OUTPUT
    print(f"\nHere's your password: {final_password}")
    print("Please keep it somewhere safe!")

if __name__ == "__main__":
    main()