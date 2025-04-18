# tip calculator.py
# This program calculates the total amount to be paid including tip and splits the bill among friends.

def main():
    # Welcome message
    print("Welcome to the tip calculator!")
    
    # Get the total bill amount from the user
    total_bill = float(input("What was the total bill? $"))
    
    # Get the tip percentage from the user
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    
    # Calculate the tip amount      
    tip_amount = total_bill * (tip_percentage / 100)
    
    # Calculate the total amount to be paid
    total_amount = total_bill + tip_amount
    
    # Get the number of friends to split the bill with
    num_friends = int(input("How many friends to split the bill? "))    
    
    # Calculate the amount each person needs to pay
    amount_per_person = round(total_amount / num_friends, 2)
    
    # Format the amount to 2 decimal places
    amount_per_person = f"{amount_per_person}"
    
    # Display the results   
    print(f"Each person should pay: ${amount_per_person}")
    print("Thank you for using the tip calculator!")

if __name__ == "__main__":
    main()