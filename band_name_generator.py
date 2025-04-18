# Simple Hello World program
def main():
    
    print("Welcome to the Band Name Generator!")
    city = input("where did you grow up?\n")
    pet = input("What is the name of a pet?\n")
    band_name = city + " " + pet
    band_name.replace(" ", "")
    print(f"Your band name could be {band_name}!")
    print("Thank you for using the Band Name Generator!")
    print("Goodbye!")
    print(len(band_name))
    
if __name__ == "__main__":
    main()