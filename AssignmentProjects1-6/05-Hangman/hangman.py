import random
from words import words

def hangman():
    
    word = random.choice(words)
    
    word_letters = set(word)
    
    guessed_letters = set()
    
    attempts = 6  # total allowed wrong guesses

    print("\nWelcome to Hangman!")
    
    print(f"The word has {len(word)} letters.")

    while len(word_letters) > 0 and attempts > 0:

        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        
        print("\nCurrent word:", ' '.join(display_word))
        
        print(f"You have {attempts} attempts to guess the word.")

        if guessed_letters:
            print("Guessed letters:", ' '.join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Correct guess!")
        
        else:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print(f"\nYou ran out of attempts! The word was: {word}")
    
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

hangman()
