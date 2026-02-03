import random
from data import DATA
from os import system

def clear_console():
    """Clear console output."""
    system('cls' if system().lower() == 'windows' else 'clear')

def format_item(item: dict) -> str:
    """Return formatted string of an item."""
    return f"{item['name']}, a {item['description']} from {item['country']}"

def check_guess(guess: str, a_followers: int, b_followers: int) -> bool:
    """Return True if guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def higher_lower_game():
    print(" Welcome to Higher Lower Game!")
    score = 0
    game_should_continue = True
    item_b = random.choice(DATA)

    while game_should_continue:
        item_a = item_b
        item_b = random.choice(DATA)
        while item_b == item_a:
            item_b = random.choice(DATA)

        print(f"Compare A: {format_item(item_a)}")
        print("VS")
        print(f"Against B: {format_item(item_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

        a_followers = item_a['followers']
        b_followers = item_b['followers']

        is_correct = check_guess(guess, a_followers, b_followers)

        clear_console()
        if is_correct:
            score += 1
            print(f" Correct! Current score: {score}")
        else:
            game_should_continue = False
            print(f" Wrong. Final score: {score}")

if __name__ == "__main__":
    higher_lower_game()
