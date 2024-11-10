import random


words_list = ["apple","Bannana","strawberry","kiwi","Mango"]

print(words_list)

word = random.choice(words_list)

print(word)

def check_letter():
    guess = input("enter you letter here ")

    if len(guess) == 1 and guess.isalpha() == True:
        print(guess)
    else:
        print("Oops! That is not a valid input.")

check_letter()