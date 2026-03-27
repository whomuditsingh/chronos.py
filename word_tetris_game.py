import threading
import time
import random
import os

class WordTetris:
    def __init__(self):
        self.words = ["PYTHON", "GRAVITY", "DYNAMIC", "NETWORK", "THREADING"]
        self.word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.word)
        self.lives = 6
        self.game_over = False
        self.start_time = time.time()
        self.interval = 10  # Seconds before gravity strikes!

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def gravity_clock(self):
        while self.lives > 0 and "_" in self.guessed_word and not self.game_over:
            time.sleep(1)
            elapsed = int(time.time() - self.start_time)
            
            if elapsed >= self.interval:
                self.lives -= 1
                self.start_time = time.time() # Reset clock
                if self.lives > 0:
                    print(f"\n GRAVITY STRIKE! -1 Life. Quick, guess a letter!")
                else:
                    self.game_over = True
                    print("\n💀 GRAVITY CRUSHED YOU! Press Enter to exit.")

    def play(self):
        self.clear()
        print("🧱 WORD TETRIS: THE GRAVITY GUESSING GAME 🧱")
        print(f"Rules: Every {self.interval}s, gravity drops a block (lose 1 life).")
        timer_thread = threading.Thread(target=self.gravity_clock, daemon=True)
        timer_thread.start()

        while self.lives > 0 and "_" in self.guessed_word:
            print(f"\nLIVES: {'❤️' * self.lives} | TIME UNTIL DROP: {self.interval - int(time.time() - self.start_time)}s")
            print(f"WORD: {' '.join(self.guessed_word)}")
            
            guess = input("Enter letter: ").upper()
            
            if self.game_over: break # Exit if gravity killed us during input

            if guess in self.word:
                print(f"✨ Nice! Gravity reset.")
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        self.guessed_word[i] = guess
                self.start_time = time.time() # Reward: Reset the gravity timer
            else:
                self.lives -= 1
                print(f"❌ Wrong! Lives: {self.lives}")

        if "_" not in self.guessed_word:
            self.game_over = True
            print(f"\n🏆 YOU DEFIED GRAVITY! The word was {self.word}.")
        elif self.lives <= 0:
            print(f"\n💀 GAME OVER. The word was {self.word}.")

if __name__ == "__main__":
    game = WordTetris()
    game.play()