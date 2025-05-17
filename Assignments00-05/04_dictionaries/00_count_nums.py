def main():
    
    count = {}

    while True:
        
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        num = int(user_input)

        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    print("Number counts:")
    
    for num, cnt in count.items():
        print(f"Number {num} appears {cnt} times")

if __name__ == "__main__":
    main()
