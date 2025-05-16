MIN_HEIGHT = 120

def can_ride():
    height = int(input("Enter your height in cm: "))
    
    if height >= MIN_HEIGHT:
        print("You are tall enough to ride!")
    
    else:
        print("Sorry! You're not tall enough to ride.")

if __name__ == "__main__":
    can_ride()