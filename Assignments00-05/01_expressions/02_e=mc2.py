C: int = 299792458 
def main():

    mass_in_kg = float(input("Enter mass in kilograms: "))

    energy = mass_in_kg * (C ** 2)

    print("e = m*C^2\n")

    print(f"Mass: {mass_in_kg} kg\n")

    print(f"Speed of light: {C} m/s\n")

    print(f"Energy: {energy} Joules in energy\n")

if __name__ == "__main__":
    main()