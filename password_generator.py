import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): True if uppercase letters should be included.
        use_numbers (bool): True if numbers should be included.
        use_symbols (bool): True if symbols should be included.

    Returns:
        str: The generated password, or an error message if criteria are invalid.
    """
    # Start with lowercase letters as the base set
    characters = string.ascii_lowercase

    # Add other character types based on user's choices
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        # Common punctuation marks. You can customize this if needed.
        characters += string.punctuation

    # --- Input Validation ---
    if not characters:
        return "Error: No character types selected for password generation. Please choose at least one."

    if length <= 0:
        return "Error: Password length must be a positive number."
    # --- End Input Validation ---

    # Generate the password
    # random.choice(characters) picks a random character from the 'characters' string.
    # The loop runs 'length' times to build the password.
    # ''.join() efficiently concatenates all the chosen characters into a single string.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    """
    Helper function to get a 'y' or 'n' (or 'yes'/'no') input from the user.
    Keeps prompting until valid input is received.
    """
    while True:
        user_input = input(prompt).strip().lower() # .strip() removes leading/trailing whitespace
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    print("----------------------------------------")
    print("  Python Command-Line Password Generator")
    print("----------------------------------------\n")

    # Get password length from the user
    while True:
        try:
            password_length = int(input("Enter desired password length: "))
            if password_length <= 0:
                print("Password length must be a positive number.")
                continue # Ask again
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get character type preferences
    include_uppercase = get_yes_no_input("Include uppercase letters (A-Z)? (y/n): ")
    include_numbers = get_yes_no_input("Include numbers (0-9)? (y/n): ")
    include_symbols = get_yes_no_input("Include symbols (!@#$%^&*...)? (y/n): ")

    # Ensure at least one character type is selected (beyond default lowercase)
    # If not, warn the user and give option to proceed with lowercase only.
    if not (include_uppercase or include_numbers or include_symbols):
        print("\n--- WARNING ---")
        print("You have not selected to include uppercase, numbers, or symbols.")
        print("Your password will only contain lowercase letters.")
        confirm_lowercase_only = get_yes_no_input("Do you want to proceed with a lowercase-only password? (y/n): ")
        if not confirm_lowercase_only:
            print("Password generation cancelled. Please re-run and select more character types.")
            exit() # Exit the script

    # Generate the password
    generated_password = generate_password(
        password_length,
        include_uppercase,
        include_numbers,
        include_symbols
    )

    # Print the result
    print(f"\nYour generated password: {generated_password}")
    print("\n----------------------------------------")
    print("Remember to store your password securely!")
    print("----------------------------------------")
