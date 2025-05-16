import math

def main():

    AB = float(input("Enter the length of AB: "))

    AC = float(input("Enter the length of BC: "))

    BC = math.sqrt(AB ** 2 + AC ** 2)

    print("The length of BC(The Hypotenuse) is: ", BC)

if __name__ == "__main__":
    main()


