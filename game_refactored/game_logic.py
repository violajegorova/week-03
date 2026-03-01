def generate_secret (low=1, high=100):
    #---Ģenerē slepeno skaitli---
    """Generates a random secret number between low and high (inclusive).
    
    Args:
        low (int): The lower bound of the range (default is 1).
        high (int): The upper bound of the range (default is 100).

    Returns:
        int: A random secret number between low and high.
    """
    import random
    return random.randint(low, high)

def check_guess(guess, secret):
    #---Pārbauda minējumu---
    """Checks if the guess is correct, too low, or too high compared to the secret number.
    
    Args:
        guess (int): The player's guess.
        secret (int): The secret number to compare against.

    Returns:
        str: A message indicating whether the guess is correct, too low, or too high.
    """
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!" 
    else:        
        return "Correct! You've guessed the secret number!"

def is_game_over(attempts, max_attempts=10):
    #---Pārbauda, vai spēle ir beigusies---
    """Checks if the game is over based on the number of attempts made.
    
    Args:
        attempts (int): The number of attempts made by the player.
        max_attempts (int): The maximum number of allowed attempts.

    Returns:
        bool: True if the game is over (attempts >= max_attempts), False otherwise.
    """
    return attempts >= max_attempts

if __name__ == "__main__":
    #---Testē spēles loģiku---
    secret = generate_secret()
    assert 1 <= secret <= 100, "Secret number should be between 1 and 100"
    assert check_guess(50, secret) in {"Too low!", "Too high!", "Correct! You've guessed the secret number!"}
    assert is_game_over(10) == True, "Game should be over after 10 attempts"
    assert is_game_over(9) == False, "Game should not be over after 9 attempts"
    print("All tests passed!")