def get_player_guess():
    """Prompts the player to enter their guess and validates the input.

    Returns:
        int: The player's guess as an integer if valid, None otherwise.
    """
    
    raw = input("Enter your guess (1-100): ")
    if raw == "":
        print("Input cannot be empty. Please enter a number between 1 and 100.")
        guess = int(input("Enter your guess (1-100): "))
        return None
    try:
        return int(raw)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None
    
def show_hint(result):
    """Displays a hint to the player based on the result of their guess.

    Args:
        result (str): The result message from checking the player's guess.

    Returns:
        None
    """
    if result == "Too low!":
        print("Hint: Try a higher number.")
    elif result == "Too high!":
        print("Hint: Try a lower number.")
    elif result == "Correct! You've guessed the secret number!":
        print("Great job! You've guessed the number!")
    else:
        print("Unexpected result. Please check the game logic.")

def show_game_over(secret, attempts, won):
    """Displays a game over message to the player, revealing the secret number.

    Args:
        secret (int): The secret number that was generated for the game.
        attempts (int): The number of attempts the player made.
        won (bool): Whether the player won the game or not.

    Returns:
        None
    """    
    if won:
        print(f"Congratulations! You've guessed the secret number {secret} in {attempts} attempts!")  
    else:
        print(f"Game over! The secret number was {secret}. You made {attempts} attempts.")  
    
def ask_play_again():
    """Asks the player if they want to play again.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    response = input("Do you want to play again? (yes/no): ").strip().lower()
    return response in {"yes", "y"}

if __name__ == "__main__":
    #---Testē UI funkcijas---
    show_hint("Too low!")
    show_hint("Too high!")
    show_hint("Correct! You've guessed the secret number!")
    show_game_over(42, 5, True)
    show_game_over(42, 10, False)
    print(f"Play again: {ask_play_again()}")