def is_email (text):
    """Checks if the input string is a valid email address.

    Criteria for a valid email address:
    - Contains exactly one "@" symbol.
    - Contains at least one "." symbol after the "@" symbol.
    - The "@" symbol must not be the first or last character of the string.
    - The "." symbol must not be the first or last character of the string.
    - The "@" symbol must come before the last "." symbol in the string.
    - The string must not contain any spaces.
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if the input string is a valid email address, False otherwise.

    Example:
    >>> is_email("user@example.com")
    True
    >>> is_email("invalid.email")
    False
    """

    if not isinstance(text, str):
        return False    
    
    if "@" in text and "." in text:
        return True
    else:
        return False

def is_phone_number (text):
    """Checks if the input string is a valid phone number.

    Criteria for a valid phone number:
    - Contains only digits, spaces, dashes, parentheses, and an optional leading "+".
    - Must contain at least 8 digits.
    
    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the input string is a valid phone number, False otherwise.

    Example:
    >>> is_phone_number("+371 12345678")
    """
    if not isinstance(text, str):
        return False
    
    allowed_characters = set("0123456789 -()+")
    for char in text:
        if char not in allowed_characters:
            return False
    
    digits_count = sum(char.isdigit() for char in text)
    if digits_count < 8:
        return False
    
    return True

def is_valid_age(age):
    """Checks if the input age is a valid age.

    Criteria for a valid age:
    - Must be an integer.
    - Must be between 0 and 150 inclusive.
    
    Args:
        age (int): The input age to check.

    Returns:
        bool: True if the input age is valid, False otherwise.

    Example:   
    >>> is_valid_age(25)
    """

    if not isinstance(age, int):
        return False
    if 0 <= age <= 150:
        return True
    else:
        return False
    
def is_strong_password(password):
    """Checks if the input password is a strong password.

    Criteria for a strong password:
    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    - Must contain at least one special character (e.g., !@#$%^&*).
    
    Args:
        password (str): The input password to check.

    Returns:
        bool: True if the input password is valid, False otherwise. 

    Example:
    >>> is_strong_password("P@ssw0rd")
    """
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False
    
def is_valid_date(date_str):
    """Checks if the input string is a valid date in the format YYYY-MM-DD.

    Criteria for a valid date:
    - Must be in the format YYYY-MM-DD.
    - Year must be between 1900 and 2100.
    - Month must be between 1 and 12.
    - Day must be valid for the given month and year (considering leap years).
    
    Args:
        date_str (str): The input string to check.

    Returns:
        bool: True if the input string is a valid date, False otherwise.

    Example:   
    >>> is_valid_date("2020-02-29")
    """
    if not isinstance(date_str, str):
        return False
    
    try:
        year, month, day = map(int, date_str.split("-"))
    except ValueError:
        return False
    
    if not (1900 <= year <= 2100):
        return False
    if not (1 <= month <= 12):
        return False
    
    # Check for valid day based on month and leap year
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 1 <= day <= 31
    elif month in {4, 6, 9, 11}:
        return 1 <= day <= 30
    elif month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap_year:
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:
        return False    
    
def main():
    # Example usage
    print(is_email("user@example.com"))         # Should return True
    print(is_email("invalid.email"))            # Should return False
    print(is_email("user@.com"))                # Should return False
    print(is_phone_number("+371 12345678"))     # Should return True
    print(is_phone_number("12345"))             # Should return False 
    print(is_phone_number("123-456-7890"))      # Should return True   
    print(is_valid_age(25))                     # Should return True
    print(is_valid_age(-5))                     # Should return False
    print(is_valid_age(200))                    # Should return False
    print(is_valid_age("twenty"))               # Should return False
    print(is_valid_age(15))                     # Should return False
    print(is_strong_password("P@ssw0rd"))        # Should return True
    print(is_strong_password("password"))        # Should return False
    print(is_strong_password("P@ssw0rd123"))     # Should return True
    print(is_strong_password("P@ss"))            # Should return False
    print(is_valid_date("2020-02-29"))          # Should return True
    print(is_valid_date("2021-02-29"))          # Should return False
    print(is_valid_date("2020-13-01"))          # Should return False
    print(is_valid_date("2020-00-10"))          # Should return False

if __name__ == "__main__":
    main()
    