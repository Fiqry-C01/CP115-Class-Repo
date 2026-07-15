kwh = float(input())
if kwh <= 100:
    totalBill = kwh * 0.3
else:
    if kwh > 100 and kwh <= 200:
        totalBill = kwh * 0.5
    else:
        totalBill = kwh * 0.75
print(totalBill)
