employee_name = input("Enter the employee's name: ")
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


print(f"\nEmployee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Number of Hours Worked: {hours_worked}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
