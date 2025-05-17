import random

def main():
    print("Welcome to the Number Guessing Game!")

    number_to_guess = random.randrange(1, 100)  
    print("I am thinking of a number between 1 and 99...")

    guess_count = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > 99 or user_guess < 1:
            print("Invalid input! Please enter a number between 1 and 99.")
            continue  

        guess_count += 1

        if user_guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the correct number '{number_to_guess}' in {guess_count} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")

if __name__ == "__main__":
    main()
