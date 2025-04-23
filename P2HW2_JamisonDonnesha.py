#Donnesha Jamison
#04/09/25
#P2Hw1
#Formatting

print("This program calculates and displays travel expenses")
budget=float(input("Enter Budget:"))
travel_destination=input("Enter your travel destination:")
gas=float(input("How much do you think you will spend on gas?"))
accomodation_hotel=float(input("Approximatelt,how much will you need for accomodation/hotel?:"))
food=float(input(" Last, how much do you need for food:?"))


print( 'Travel Expenses')

print(f"{'Location: ':<20}{travel_destination}")
print(f"{'Initial Budget:' :<20}${ budget:.2f}")
print (f"{'Fuel:':<20}${gas:.2f}")
print( f"{'Accomodation:':<20}${accomodation_hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")
remaining=budget-gas-accomodation_hotel-food

print(f"{'Remaining Balance:':<20}$ {remaining:.2f}")
