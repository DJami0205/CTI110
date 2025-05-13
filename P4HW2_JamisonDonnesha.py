# Donnesha Jamison
#04/30/2025
#P4Hw2
# Done into program.

total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter the employee's name (or 'Done' to finish): ")
    
    if employee_name.lower() == "done":  
        break
    
    hours_worked = float(input("Enter the number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: $"))

    overtime_hours = 0
    regular_pay = 0
    overtime_pay = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40  
        regular_pay = 40 * pay_rate 
        overtime_pay = overtime_hours * (pay_rate * 1.5)  
    else:
        regular_pay = hours_worked * pay_rate  

    gross_pay = regular_pay + overtime_pay

    
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

    
    print("\n" + "-" * 75)
    print(f"{'Employee Name':<20} {'Pay Rate':<10} {'Hours Worked':<15} {'Overtime Hours':<15} {'Overtime Pay':<15} {'Regular Pay':<15} {'Gross Pay':<15}")
    print("-" * 75)  
    print(f"{employee_name:<20} ${pay_rate:<9.2f} {hours_worked:<15} {overtime_hours:<15} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<14.2f}")
    print("-" * 75)

# Print totals after exiting the loop
print("\nTotal Results")
print(f"Number of Employees: {employee_count}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
