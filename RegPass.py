import re

def password_policy_to_grep_commands(
    min_length=0,
    max_length=None,
    upper=0,
    lower=0,
    digits=0,
    special=0,
    special_chars="!@#$%^&*",
    prohibited_chars="",
    no_repeated_chars=False,
    required_sequences=None
):
    """
    Generate regular expression-based grep commands based on the given password policy.
    """
    commands = []
    escaped_special_chars = re.escape(special_chars)
    escaped_special_chars = escaped_special_chars.replace('!', '\\!')
    prohibited_escaped = re.escape(prohibited_chars) if prohibited_chars else ""
    
    if min_length > 0:
        commands.append(f'grep -E "^.{{{min_length},}}$"')
    if max_length:
        commands.append(f'grep -E "^.{{,{max_length}}}$"')
    
    if upper > 0:
        commands.append(f'grep -E "([A-Z].*){{{upper},}}"')
    if lower > 0:
        commands.append(f'grep -E "([a-z].*){{{lower},}}"')
    if digits > 0:
        commands.append(f'grep -E "([0-9].*){{{digits},}}"')
    if special > 0:
        commands.append(f'grep -E "([{escaped_special_chars}].*){{{special},}}"')
    
    if prohibited_chars:
        commands.append(f'grep -v -E "[{prohibited_escaped}]"')
    
    if no_repeated_chars:
        commands.append(f'grep -v -E "(.)\\1"')
    
    if required_sequences:
        for sequence in required_sequences:
            commands.append(f'grep -E "{re.escape(sequence)}"')
    
    return " | ".join(commands)


def ask_yes_no(prompt, default=False):
    """Prompt the user for a yes/no response."""
    while True:
        answer = input(f"{prompt} (yes/no, default: {'yes' if default else 'no'}): ").strip().lower()
        if answer == "":
            return default
        if answer in ("yes", "no"):
            return answer == "yes"
        print("Please answer 'yes' or 'no'.")


def main():
    print("\nWelcome to RegPas!")
    print("This interactive tool helps you generate grep commands for any password policy.\n")
    
    try:
        print("Step 1: Length Constraints")
        min_length = input("Enter the minimum password length (default: 0): ").strip()
        min_length = int(min_length) if min_length.isdigit() else 0

        max_length = input("Enter the maximum password length (leave blank for no limit): ").strip()
        max_length = int(max_length) if max_length.isdigit() else None
        
        print("\nStep 2: Character Type Requirements")
        upper = input("Minimum number of uppercase letters (default: 0): ").strip()
        upper = int(upper) if upper.isdigit() else 0

        lower = input("Minimum number of lowercase letters (default: 0): ").strip()
        lower = int(lower) if lower.isdigit() else 0

        digits = input("Minimum number of numeric digits (default: 0): ").strip()
        digits = int(digits) if digits.isdigit() else 0

        special = input("Minimum number of special characters (default: 0): ").strip()
        special = int(special) if special.isdigit() else 0
        
        print("\nStep 3: Special Characters")
        special_chars = input("Enter allowed special characters (default: !@#$%^&*): ").strip()
        special_chars = special_chars if special_chars else "!@#$%^&*"
        
        print("\nStep 4: Prohibited Characters")
        prohibited_chars = input("Enter prohibited characters (leave blank if none): ").strip()
        
        print("\nStep 5: Additional Constraints")
        no_repeated_chars = ask_yes_no("Disallow repeated characters?", default=False)

        required_sequences = input("Enter required sequences (comma-separated, leave blank if none): ").strip()
        required_sequences = (
            [seq.strip() for seq in required_sequences.split(",")]
            if required_sequences
            else []
        )
        
        print("\nGenerating grep commands...")
        grep_commands = password_policy_to_grep_commands(
            min_length=min_length,
            max_length=max_length,
            upper=upper,
            lower=lower,
            digits=digits,
            special=special,
            special_chars=special_chars,
            prohibited_chars=prohibited_chars,
            no_repeated_chars=no_repeated_chars,
            required_sequences=required_sequences,
        )
        
        print("\nGenerated Command:")
        print(grep_commands)
        print("\nUse this command to filter passwords based on the specified policy.")
    except ValueError:
        print("Invalid input. Please provide numeric values where applicable.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
