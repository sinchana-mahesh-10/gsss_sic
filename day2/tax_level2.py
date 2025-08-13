'''
Level2:
Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.
'''

import tax_level1

Standard_Deduction = 50000
Taxable_Income = tax_level1.annual_gross_salary - Standard_Deduction

print('Standard_Deduction : ', Standard_Deduction)
print('Taxable_Income : ', Taxable_Income)




