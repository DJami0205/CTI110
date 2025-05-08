def display_multiplication_table(num):
    # Display the multiplication table for the given number
    for i in range(1, 13):  # Loop from 1 to 12
        print(f"{num} x {i} = {num * i}")  # Print the multiplication result

def main():
    while True:  # Start a loop to allow the user to run the program multiple times
        try:
            user_input = int(input("Enter an integer: "))  # Ask the user for input
            
            if user_input < 0:  # Check if the number is negative
                print("Negative values are not accepted.")  # Inform the user
            else:
                # If the number is zero or higher, display the multiplication table
                display_multiplication_table(user_input)

        except ValueError:
            print("Please enter a valid integer.")  # Handle invalid input

        # Ask the user if they want to run the program again
        again = input("Do you wish to run it again? (yes/no): ").strip().lower()
        if again != "yes":  # If the user types anything other than "yes", break the loop
            break

# Call the main function to start the program
main()
