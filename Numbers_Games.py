import random
import time
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display fireworks in the terminal
def terminal_fireworks():
    firework_patterns = [
        "     *\n    ***\n   *****\n    ***\n     *",
        "      *\n     * *\n    * * *\n   * * * *\n    * * *\n     * *\n      *",
        "      *\n     ***\n    *****\n   *******\n    *****\n     ***\n      *"
    ]
    
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]  # ANSI color codes
    reset = "\033[0m"

    for _ in range(10):  # Show 10 random fireworks
        clear_screen()
        firework = random.choice(firework_patterns)
        color = random.choice(colors)
        print(f"{color}{firework}{reset}")
        time.sleep(0.3)
    
    clear_screen()
    print("🎉 Congratulations! 🎉")
    time.sleep(2)

# Number Guessing Game
def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            player_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            terminal_fireworks()  # Show terminal fireworks when the player wins
            break

# Run the game
guess_number()

