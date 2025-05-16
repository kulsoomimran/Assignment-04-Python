PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def can_vote():

    user_age = int(input("Enter your age: "))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo.")
    else:
        print("You cannot vote in Peturksbouipo.")
    
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau.")
    else:
        print("You cannot vote in Stanlau.")

    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua.")
    else:
        print("You cannot vote in Mayengua.")

if __name__ == "__main__":
    can_vote()