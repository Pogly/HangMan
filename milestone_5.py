import random

class hangman:
    def __init__(self,num_lives,wordlist):
        self.wordlist = ["apple","Bannana","strawberry","kiwi","Mango"]
        self.num_lives = 5
        self.word = random.choice(self.wordlist)
        self.num_letters = len(set(self.word))
        
        self.word_guessed = []
        for letter in self.word:
            self.word_guessed.append("_")

        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            letterindex = 0
            
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[letterindex] = guess
                
                letterindex = letterindex + 1
            
            self.num_letters = self.num_letters - 1

            print(self.word_guessed)
            print(self.num_letters)

        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please select what letter would you like to guess?")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
 
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
                self.check_guess(guess)
                break
def play_game(word_list):

    print("starting the game")
    
    
    num_lives = 5
    word_list = word_list
    game = hangman(num_lives,word_list)


    while True:
        if game.num_lives == 0:
            print("you lost")
            break
        
        elif game.num_letters != 0:
            game.ask_for_input()
        else:  
            print("Congratulations. You won the game!")
            break

my_list = ["apple","bannana","strawberry","kiwi","mango"]

play_game(my_list)