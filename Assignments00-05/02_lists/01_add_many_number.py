def sum_of_numbers(numbers):

    total = 0

    for num in numbers:
        total += num
    
    return total

def main():
    numbers_list = [10, 22, 38, 40, 55]

    total_sum = sum_of_numbers(numbers_list)

    print(f"The sum of the numbers in the list is: {total_sum}")

if __name__ == "__main__":
    main()