import random

def disperse_change(change):
    """Calculates and prints the change due in various denominations."""
    total_cents = int(change * 100) 

   
    if total_cents == 0:
        print("No change")
        return 
    
    
    dollars = total_cents // 100
    total_cents %= 100

  
    quarters = total_cents // 25
    total_cents %= 25


    dimes = total_cents // 10
    total_cents %= 10


    nickels = total_cents // 5
    pennies = total_cents % 5

 
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'y' if pennies == 1 else 'ies'}")

def main():
    owed_amount = round(random.uniform(1.00, 100.00), 2)  
    print(f"The total owed is: ${owed_amount:.2f}")  

    
    amount = float(input("Enter the amount of money you will put into the self-checkout: $"))

    if amount < owed_amount:
        print("Insufficient funds.")
    else:
        change = amount - owed_amount  
        disperse_change(change) 

if __name__ == "__main__":
    main()  # Call the main function to start the program
