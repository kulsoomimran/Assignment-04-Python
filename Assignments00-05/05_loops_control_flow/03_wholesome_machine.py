AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():

    print("Please type the following Affirmation:", AFFIRMATION)

    user_feedback = input()

    while user_feedback != AFFIRMATION:
        
        print("Please type the following Affirmation:", AFFIRMATION)

        user_feedback = input()
    print("Great job! You typed the affirmation correctly.")

if __name__ == "__main__":
    main()