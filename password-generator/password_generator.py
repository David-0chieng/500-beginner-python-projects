import math
import secrets
import string
import sys


# Character sets
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS    = string.digits
SPECIAL   = string.punctuation

# Strength rating based on entropy bits
STRENGTH_LEVELS = [
    (28,  "very weak"),
    (36,  "weak"),
    (60,  "fair"),
    (128, "strong"),
]

def score_entropy(entropy_bits):
    for threshold, label in STRENGTH_LEVELS:
        if entropy_bits < threshold:
            return label
    return "very strong"

def compute_entropy(pool_size, length):
    if pool_size <= 1:
        return 0.0
    return math.log2(pool_size) * length


def generate_password(password_length, uppercase_chars, has_digits, special_chars):
    """Password Generation Logic — uses secrets instead of random for real security."""

    password_chars = ''

    # LENGTH VALIDATION
    if password_length < (uppercase_chars + has_digits + special_chars):
        raise ValueError('Password too short.')

    password_chars = ''

    # Guaranteeing password will include what users selected
    if uppercase_chars:
        password_chars += secrets.choice(UPPERCASE)
    if has_digits:
        password_chars += secrets.choice(DIGITS)
    if special_chars:
        password_chars += secrets.choice(SPECIAL)

    # Always include at least one lowercase letter
    password_chars += secrets.choice(LOWERCASE)

    # BUILDING THE CHARACTER SET
    characters = LOWERCASE
    if uppercase_chars:
        characters += UPPERCASE
    if has_digits:
        characters += DIGITS
    if special_chars:
        characters += SPECIAL

    # Fill the rest of the password up to the requested length
    for _ in range(password_length - len(password_chars)):
        password_chars += secrets.choice(characters)

    # SHUFFLING PASSWORD TO BE UNPREDICTABLE
    password = list(password_chars)
    secrets.SystemRandom().shuffle(password)
    return ''.join(password), len(characters)
    
    
def main():
    
    print("\n====================== WELCOME TO PASSWORD GENERATOR ==========================\n")

    # 1. INPUT COLLECTION
    try:
        password_length = int(input("How many characters would you like your password to have: "))
    except ValueError:
        print("Please enter a whole number.")
        sys.exit(1)

    uppercase_chars = input("Would you like your password to have uppercase characters? (y/n): ").lower().strip() == 'y'
    has_digits      = input("Would you like your password to have digits? (y/n): ").lower().strip() == 'y'
    special_chars   = input("Would you like your password to have special characters? (y/n): ").lower().strip() == 'y'

    # CALLING generate_password() WITH ERROR HANDLING
    try:
        final_password, pool_size = generate_password(password_length, uppercase_chars, has_digits, special_chars)
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)

    # Work out how strong the password is
    entropy = compute_entropy(pool_size, password_length)
    label   = score_entropy(entropy)

    # DISPLAYING OUTPUT
    print(f"\nHere's your password: {final_password}")
    print(f"Strength : {label.upper()}")
    print(f"Entropy  : {entropy:.1f} bits")
    print("\nPlease keep it somewhere safe!")

if __name__ == "__main__":
    main()