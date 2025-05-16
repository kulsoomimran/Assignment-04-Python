import random

MIN_VALUE = 1
MAX_VALUE = 100
NUMBERS = 10

def generate_random_numbers():

    for _ in range(NUMBERS):
        
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        print(random_number)

if __name__ == "__main__":
    generate_random_numbers()