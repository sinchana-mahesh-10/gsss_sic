'''
Level 3: Tax and Rebate Calculation
Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.
Output:
• Display a detailed tax breakdown, including slabs, cess, and total tax payable.
'''

print('Tax and Rebate Calculation')

tax = 0

if tax_level2.taxable_income <= 300000:
    tax = 0
elif tax_level2.taxable_income > 300000 and tax_level2.taxable_income <= 600000:
    
