def main():
    
    curr_val = int(input("Enter a number: "))

    MAX_VALUE = 100

    while curr_val < MAX_VALUE:
        curr_val *= 2

        print(curr_val, end=", ")

if __name__ == "__main__":
    main()