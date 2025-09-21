annual_salary = 75000

if annual_salary >= 100000:
    bracket = "High Income"
    tax_rate = 0.25
elif annual_salary >= 75000:
    bracket = "Upper Middle Income"
    tax_rate = 0.22
elif annual_salary >= 50000:
    bracket = "Middle Income"
    tax_rate = 0.18
elif annual_salary >= 30000:
    bracket = "Lower Middle Income"
    tax_rate = 0.15
else:
    bracket = "Low Income"
    tax_rate = 0.10

print(f"Salary: ${annual_salary:,}")
print(f"Income Bracket: {bracket}")
print(f"Tax Rate: {tax_rate*100}%")