def main():

    list_of_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

    for i in range(len(list_of_no)):
        
        elem = list_of_no[i]
        
        list_of_no[i] = elem * 2

    print(list_of_no)

if __name__ == "__main__":
    main()
