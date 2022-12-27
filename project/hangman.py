from typing import Set

class Hangman:

    def __init__(self, total_lives: int) -> None:

        self.lives: int = total_lives


    def ask_for_word(self) -> None: # O(1)

        word: str = input("Enter your word: ").lower() # O(n)
        hidden_word: str =  len(word) * "_" # O(1)
        print(hidden_word)
        return self.play(hidden_word, word)


    def play(self, current_word: str, word: str, chances: int=0) -> int: #O (n^3)

        if current_word == word: # O(n)
            return "You win!"
        if chances == self.lives: # O(1)
            return "You lose!"

        letter_guessed: str = input("Guess a letter: ").lower() # O(n)

        letters_in_word: Set(str) = set(word) # O(n)
        letters_in_current_word: Set(str) = set(current_word) # O(n)
        if letter_guessed in letters_in_word and letter_guessed not in letters_in_current_word: # O(1)
            i: int
            letter: str
            for i, letter in enumerate(word): # O(n)
                if letter == letter_guessed: # O(1)
                    current_word: str = current_word[:i] + letter + current_word[i+1:] # O(k+l)
        else:
            if letter_guessed in current_word: # O(n)
                print("You've already guessed this letter!!")
            chances += 1 # O(1)
            print(f"You have {self.lives - chances} lives left")

        print(current_word)

        return self.play(current_word, word, chances)