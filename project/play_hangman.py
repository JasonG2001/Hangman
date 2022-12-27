from hangman import Hangman

if __name__ == "__main__":
    total_lives: int = 6
    hangman = Hangman(total_lives)
    print(hangman.ask_for_word())