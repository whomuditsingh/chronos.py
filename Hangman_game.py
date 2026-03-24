import random

HANGMAN_STAGES = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    --------
    """
]

def get_valid_guess(already_guessed):
    while True:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in already_guessed:
            print(f"You already guessed '{guess}'. Try something else!")
        else:
            return guess

def play_hangman():
    words = ["python", "algorithm", "jupyter", "variable", "function", "bytecode"]
    target_word = random.choice(words)
    hidden_word = ["_"] * len(target_word)
    lives = 6
    guessed_letters = set()

    print("🎮 WELCOME TO HANGMAN PRO 🎮")

    while lives > 0 and "_" in hidden_word:
        print(HANGMAN_STAGES[lives])
        print(f"Word: {' '.join(hidden_word)}")
        print(f"Guessed so far: {', '.join(sorted(guessed_letters))}")

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in target_word:
            print(f"✅ Yes! '{guess}' is in the word.")
            for i, letter in enumerate(target_word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            lives -= 1
            print(f"❌ No '{guess}'. You lost a life!")

# End Game Logic
    if "_" not in hidden_word:
        print("\n🏆 CONGRATULATIONS!")
        print(f"You saved the man! The word was: {target_word.upper()}")
    else:
        print(HANGMAN_STAGES[0])
        print("\n💀 GAME OVER")
        print(f"The word was: {target_word.upper()}")

if __name__ == "__main__":
    play_hangman()