def main():

    list = []

    val = input("Enter a value to add to the list (or press Enter to finish): ")

    while val:
    
        list.append(val)
        
        val = input("Enter a value to add to the list (or press Enter to finish): ")
    
    print("The list is:", list)

if __name__ == "__main__":
    main()

