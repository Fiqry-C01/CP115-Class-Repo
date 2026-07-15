hours = int(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours > 2 and hours <= 5:
        parkingFee = hours * 2
    else:
        parkingFee = hours * 3
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)
