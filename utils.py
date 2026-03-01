#Utilītu bibliotēka
def capitalize_first_letter(text):
    """Capitalizes the first letter of a string.
    
    Args:
        text (str): The input string to capitalize.
    
    Returns:
    str: The input string with the first letter capitalized.

    Example:
    >>> capitalize_first_letter("hello")
    "Hello"
    """
    if not text:
        return text
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text[0].upper() + text[1:]

def truncate_string(s, max_len=20):
    """Truncates a string to a specified maximum length.
    
    Args:
        s (str): The input string to truncate.
        max_length (int): The maximum length of the truncated string.
    
    Returns:
        str: The truncated string, with "..." appended if it was truncated.
    Example:
    >>> truncate_string("This is a long string", 10)
    "This is a..."
    """
    if len(s) > max_len:
        return s[:max_len - 3] + "..."
    else:
        return s
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def count_words(s):
    """Counts the number of words in a string.
    
    Args:
        s (str): The input string to count words in.
    
    Returns:
        int: The number of words in the input string.
    Example:
    >>> count_words("Hello world")
    2
    """

    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    words = s.split()
    return len(words)

def clamp(num, low, high):
    """Clamps a number between a low and high value.
    
    Args:
        num (float): The number to clamp.
        low (float): The lower bound of the clamp.
        high (float): The upper bound of the clamp.   
    """
    if num < low:
        return low
    elif num > high:
        return high
    else:
        return num
    if not (isinstance(num, (int, float)) and isinstance(low, (int, float)) and isinstance(high, (int, float))):
        raise ValueError("All inputs must be numbers")
    
def is_prime(n):
    """Checks if a number is prime.
    
    Args:
        n (int): The number to check for primality.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

def factorial(n):
    """Calculates the factorial of a number.
    
    Args:
        n (int): The number to calculate the factorial of.
    
    Returns:
        int: The factorial of the input number.
    Example:
    >>> factorial(5)
    120
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
def total(numbers):
    """Calculates the total sum of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to sum.
    
    Returns:
        float: The total sum of the input numbers.
    Example:
    >>> total([1, 2, 3, 4])
    10
    """
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All items in the list must be numbers")
    
def average(numbers):
    """Calculates the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to calculate the average of.
    
    Returns:
        float: The average of the input numbers.
    Example:
    >>> average([1, 2, 3, 4])
    2.5
    """
    if len(numbers) == 0:
        return 0
    total_sum = total(numbers)
    return total_sum / len(numbers)
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All items in the list must be numbers")

# =========================================
# Demonstrācija
# =========================================
def main ():
    print("Demonstrācijas izsaukumi:")
    print(capitalize_first_letter("hello"))
    print(truncate_string("This is a long string", 10))
    print(count_words("Hello world"))
    print(clamp(5, 1, 10))
    print(is_prime(7))
    print(factorial(5))
    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))

if __name__ == "__main__":    main()

