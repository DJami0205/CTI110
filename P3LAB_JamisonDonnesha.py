#Donnesha Jamison
#4/23/2025
#P3LAB1

# Prompt user for the amount of money and convert it to a float
amount = float(input("Enter the amount of money as a float: $"))

# Convert the float amount to cents by multiplying by 100 and then converting to an integer
total_cents = int(amount * 100)

# Check if the amount is zero
if total_cents == 0:
    print("No change")
else:
    # Calculate the number of dollars
    dollars = total_cents // 100  # Whole dollars
    total_cents %= 100  # Remaining cents after extracting dollars

    # Calculate the number of quarters
    quarters = total_cents // 25
    total_cents %= 25  # Remaining cents after extracting quarters

    # Calculate the number of dimes
    dimes = total_cents // 10
    total_cents %= 10  # Remaining cents after extracting dimes

    # Calculate the number of nickels
    nickels = total_cents // 5
    pennies = total_cents % 5  # Remaining cents, these are the pennies

    # Print out the number of each coin, checking for zero coins
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
