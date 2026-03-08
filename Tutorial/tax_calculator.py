# Request the constants as user inputs
TAX_RATE = float(input("Enter the tax rate: "))
STANDARD_DEDUCTION = float(input("Enter the standard deduction: "))
DEPENDENT_DEDUCTION = float(input("Enter the dependent deduction: "))

# Request the remaining inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)

# Basic check to ensure taxable income is not negative
if taxableIncome < 0:
    taxableIncome = 0

incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print("The income tax is $" + str(round(incomeTax, 2)))

