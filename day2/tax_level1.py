'''
Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
• Output:
o Display the employee details, gross monthly salary, and annual gross salary.

'''

print('employee details')
name = input('Enter Name of Employee: ')
emp_id = input('Enter ID of Employee: ')
basic_salary = int(input('Enter salary of Employee: '))
special_allowances = int(input('Enter allowance of Employee: '))
bonus_percentage = float(input('Enter bonus percentage of Employee: '))

gross_monthly_salary = basic_salary + special_allowances
annual_gross_salary = (gross_monthly_salary * 12) + (bonus_percentage/100) * (gross_monthly_salary * 12)

print("\n----- Employee Salary Report -----")
print("Name: ", name)
print("Employee ID: ", emp_id)
print("Gross Monthly Salary: ", gross_monthly_salary)
print("Annual Gross Salary: ", annual_gross_salary)


