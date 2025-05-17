def main():

    fruits = {
        "apple": 2,
        "banana": 3,
        "orange": 5,
        "grape": 4,
        "mango": 5,
        "kiwi": 2
    }

    print("Welcome to the Pop-Up Shop!")

    total_cost = 0

    while True:
        print("\nAvailable fruits:")
        for fruit, price in fruits.items():
            print(f"{fruit}: ${price}")

        selected_fruit = input("Enter the fruit you want to buy (or 'done' to finish): ").lower()

        if selected_fruit == "done":
            break

        if selected_fruit in fruits:
            quantity = int(input(f"How many {selected_fruit}s do you want to buy? "))
            cost = fruits[selected_fruit] * quantity
            total_cost += cost
            print(f"You bought {quantity} {selected_fruit}(s) for ${cost}.")
        else:
            print("Sorry, we don't have that fruit.")

    print(f"\nYour total cost is: ${total_cost}")

if __name__ == "__main__":
    main()