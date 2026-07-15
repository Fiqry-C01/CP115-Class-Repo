income = int(input())
if income <= 50000:
    totalTax = 0
else:
    if income > 50000 and income <= 100000:
        totalTax = income * 0.01
    else:
        totalTax = income * 0.02
print(totalTax)
