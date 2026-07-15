weight = float(input())
ticketPrice = int(input())
if weight <= 15:
    if weight == 0:
        finalPrice = ticketPrice - 10.0
    else:
        finalPrice = ticketPrice
else:
    extraCharge = weight - 15 * 4.0
    finalPrice = ticketPrice + extraCharge
print(finalPrice)
