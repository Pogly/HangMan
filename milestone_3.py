import milestone_2

while True:
    guess = input("Please select what letter would you like to guess?")

    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
print("noloop")

if guess in milestone_2.word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")