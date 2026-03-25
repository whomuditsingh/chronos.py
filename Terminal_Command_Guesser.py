import random
import os

def clear_screen():
# Clears the terminal for a cleaner game experience
    os.system('cls' if os.name == 'nt' else 'clear')

def play_cmd_guesser():
# The "Library" of commands and their definitions
    library = {
        "enumerate": "Returns an index along with the value while iterating.",
        "isinstance": "Checks if an object is an instance of a specific class.",
        "zip": "Aggregates elements from two or more iterables into tuples.",
        "getattr": "Returns the value of a named attribute of an object.",
        "map": "Applies a function to all items in an input list.",
        "filter": "Constructs an iterator from elements that return true for a function."
    }

# Game Setup
    cmd_list = list(library.keys())
    target_cmd = random.choice(cmd_list)
    hidden_cmd = ["_"] * len(target_cmd)
    attempts = 6
    guessed = set()

    clear_screen()
    print("👨‍💻 TERMINAL COMMAND GUESSER 👨‍💻")
    print("Hint: It's a Python built-in function.")

# Game Loop
    while attempts > 0 and "_" in hidden_cmd:
        print(f"\nAttempts remaining: {'❤️' * attempts}")
        print(f"Command: {' '.join(hidden_cmd)}")
        print(f"Used keys: {', '.join(sorted(guessed))}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(">> Please enter a single letter.")
            continue

        if guess in guessed:
            print(f">> You already tried '{guess}'.")
            continue

        guessed.add(guess)

        if guess in target_cmd:
            print(f"✅ Success: '{guess}' found!")
            for i, letter in enumerate(target_cmd):
                if letter == guess:
                    hidden_cmd[i] = guess
        else:
            attempts -= 1
            print(f"Error: '{guess}' not in command.")

# Result and Learning Moment
    clear_screen()
    if "_" not in hidden_cmd:
        print(f"🏆 ACCESS GRANTED: {target_cmd}")
        print("-" * 30)
        print(f"DEFINITION: {library[target_cmd]}")
        print("-" * 30)
    else:
        print(f"💀 ACCESS DENIED. The command was: {target_cmd}")

if __name__ == "__main__":
    play_cmd_guesser()