# RegPas: Password Policy to Regular expression

**RegPas** is a simple Python tool designed to help you generate commands based on a given password policy. By specifying the required password rules such as minimum length, number of uppercase letters, lowercase letters, numeric digits, and special characters, this tool generates a series of `grep -E` commands that can be used to filter passwords in a file based on your policy.

---

## Features

- **Password Length**: Specify a minimum length for the password.
- **Uppercase Letters**: Enforce a minimum number of uppercase letters.
- **Lowercase Letters**: Enforce a minimum number of lowercase letters.
- **Numeric Digits**: Require a minimum number of numeric digits.
- **Special Characters**: Set a minimum number of special characters from a customizable list of allowed characters.
---

## Installation

 **Clone the repository** (or download the script file):

   ```bash
   git clone https://github.com/kasem545/RegPas.git
   ```

   OR if you have the Python script directly, simply place it in your working directory.

---

## Usage Instructions

### Step-by-Step Guide

1. **Run the Script**: 
   Navigate to the directory containing the `regpas.py` script (or use the filename provided) and run the script:

   ```bash
   python3 regpas.py
   ```

2. **Provide Your Password Policy**:
   When prompted, enter the desired password policy:
   - Minimum password length.
   - Minimum number of uppercase letters.
   - Minimum number of lowercase letters.
   - Minimum number of numeric digits.
   - Minimum number of special characters (optional list provided).

3. **Generated Output**:
   The tool will generate a series of `grep -E` commands for filtering passwords based on your specified policy. The output will look like this:

   ```bash
   grep -E "^.{8,}$" <FILENAME> | grep -E "[A-Z]" | grep -E "[a-z]" | grep -E "[0-9]" | grep -E "([!@#\$].*){2,}"
   ```

---

## Example

**Input**:
```
Minimum password length: 8
Minimum number of uppercase letters: 1
Minimum number of lowercase letters: 1
Minimum number of numeric digits: 2
Minimum number of special characters: 2
Allowed special characters (default: !@#$%^&*): !@#$
```

**Generated Output**:
```
Generated Command:
grep -E "^.{8,}$" <FILENAME> | grep -E "[A-Z]" | grep -E "[a-z]" | grep -E "[0-9]" | grep -E "([!@#\$].*){2,}"

Use this command to filter passwords based on the specified policy.
```

---

## Command Breakdown

- **`grep -E "^.{min_length,}$" <FILENAME>`**: Ensures the password meets the minimum length requirement.
- **`grep -E "[A-Z]"`**: Ensures the password contains at least one uppercase letter.
- **`grep -E "[a-z]"`**: Ensures the password contains at least one lowercase letter.
- **`grep -E "[0-9]"`**: Ensures the password contains at least one numeric digit.
- **`grep -E "([{escaped_special_chars}].*){{special_count,}}"`**: Ensures the password contains the specified number of special characters from the allowed set.

---
