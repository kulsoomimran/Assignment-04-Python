def main():

    dividend =  int(input("Enter an integer to be dividend: "))

    divisor = int(input("Enter an integer to be divided by: "))

    quotient = dividend // divisor

    remainder = dividend % divisor

    print(f"The quotient of {dividend} divided by {divisor} is {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
    main()