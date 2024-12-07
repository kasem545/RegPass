import re

def password_policy_to_grep_commands(min_length=0, upper=0, lower=0, digits=0, special=0, special_chars="!@#$%^&*"):
    """
    Generate regular expression based on the given password policy, with escaped special characters for grep.

    Args:
        min_length (int): Minimum length of the password.
        upper (int): Minimum number of uppercase letters required.
        lower (int): Minimum number of lowercase letters required.
        digits (int): Minimum number of numeric digits required.
        special (int): Minimum number of special characters required.
        special_chars (str): Allowed special characters.
    """
    commands = []
    
    escaped_special_chars = re.escape(special_chars)
    
    escaped_special_chars = escaped_special_chars.replace('!', '\\!')
    
    if min_length > 0:
        commands.append(f'grep -E "^.{{{min_length},}}$" <FILENAME>')
    
    if upper > 0:
        commands.append(f'grep -E "[A-Z]"')
    
    if lower > 0:
        commands.append(f'grep -E "[a-z]"')
    
    if digits > 0:
        commands.append(f'grep -E "[0-9]"')
    
    if special > 0:
        commands.append(f'grep -E "([{escaped_special_chars}].*){{{special},}}"')
    
    return " | ".join(commands)

def main():
    print("Welcome to RegPas!")
    print("This tool helps you generate a regular expression and grep commands based on your password policy.\n")
    
    print("Usage:")
    print("1. Enter the desired minimum length for your password.")
    print("2. Specify the minimum number of uppercase letters, lowercase letters, numeric digits, and special characters.")
    print("3. Optionally define the allowed special characters (defaults to !@#$%^&*).")
    print("4. The program will output the corresponding regex and grep commands.\n")
    
    try:
        print("Please provide your password policy:")
        min_length = int(input("Minimum password length: "))
        upper = int(input("Minimum number of uppercase letters: "))
        lower = int(input("Minimum number of lowercase letters: "))
        digits = int(input("Minimum number of numeric digits: "))
        special = int(input("Minimum number of special characters: "))
        special_chars = input("Allowed special characters (default: !@#$%^&*): ") or "!@#$%^&*"
        
        grep_commands = password_policy_to_grep_commands(min_length, upper, lower, digits, special, special_chars)
        print("\nGenerated Command:")
        print(grep_commands)
        print("\nUse this command to filter passwords based on the specified policy.")
    except ValueError:
        print("Invalid input. Please enter numeric values for all the policy requirements where applicable.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

