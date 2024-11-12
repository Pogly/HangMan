import random

class hangman:
    def __init__(self):
        self.wordlist = ["apple","Bannana","strawberry","kiwi","Mango"]
        self.num_lives = 5
        self.word = random.choice(self.wordlist)
        self.num_letters = len(set(self.word))
        
        self.word_guessed = []
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input():
            while True:
                guess = input("Please select what letter would you like to guess?")

                if len(guess) == 1 and guess.isalpha() == True:
                    break
                
                elif guess == self.list_of_guesses:
                    print("You already tried that letter!")

                else:
                    print("Invalid letter. Please, enter a single alphabetical character.")
        
    check_guess(guess)

        

