def get_first_element(lst):

    print("The first element in the list is:", lst[0])

def main():
    
    n = int(input("Enter the number of elements in the list: "))
    
    if n <= 0:
        
        print("The list must contain at least one element.")
        
        return

    lst = []
    
    for i in range(n):
        
        element = input(f"Enter element {i+1}: ")
        
        lst.append(element)

    get_first_element(lst)

if __name__ == '__main__':
    main()
