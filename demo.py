from utils import capitalize_first_letter, factorial, total, average, truncate_string, count_words, is_prime, clamp
from validators import is_email, is_phone_number, is_valid_age, is_strong_password, is_valid_date

def run_case(func, *args, label=None):
    """Helper function to run a test case and print the result."""
    try:
        result = func(*args)
        print(f"{func.__name__}({', '.join(map(str, args))}) -> {result}")
    except Exception as e:
        print(f"{func.__name__}({', '.join(map(str, args))}) -> Error: {e}")

def main():
    print("===Utils demonstrācija===")
    run_case(capitalize_first_letter, "hello")
    run_case(truncate_string, "This is a long string", 10)
    run_case(count_words, "Hello there")
    run_case(clamp, 5, 1, 10)
    run_case(is_prime, 7)
    run_case(factorial, -5)
    run_case(total, [1, 2, 3, 4])
    run_case(average, [1, 2, 3, 4])
    run_case(is_email, "vj.com")

if __name__ == "__main__":    main()