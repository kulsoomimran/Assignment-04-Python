def read_phone_book():
    
    phonebook = {}
    
    while True:
        
        name = input("Enter a name (or press Enter to quit): ")
        
        if name == "":
            break
        
        phone_number = input(f"Enter the phone number for {name}: ")
        
        phonebook[name] = phone_number

    return phonebook

def display_phone_book(phonebook):
    
    print("\nPhone Book:")
    
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

def lookup_phone_number(phonebook):
    
    name = input("\nEnter a name to look up: ")
    
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    
    else:
        print(f"{name} not found in the phone book.")

def main():

    phonebook = read_phone_book()
    
    display_phone_book(phonebook)
    
    lookup_phone_number(phonebook)

if __name__ == "__main__":
    main()