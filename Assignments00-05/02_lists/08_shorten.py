MAX_LENGTH = 5

def shorten(lst):

    if len(lst) <= MAX_LENGTH:
        
        print("No need to shorten the list.")
        
        return
    
    while len(lst) > MAX_LENGTH:
        
        last_item = lst.pop()

        print(f"Removed: {last_item}")
    

def main():

    lst = []

    n = int(input("Enter the number of elements in the list: "))

    for i in range(n):
        
        value = input("Enter element: ")

        lst.append(value)

    print("List before shortening:", lst)

    shorten(lst)

    print("List after shortening:", lst)

if __name__ == "__main__":
    main()
