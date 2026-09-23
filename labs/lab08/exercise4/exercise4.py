current_reading = int(input())
previous_reading = int(input())
consumption = current_reading - previous_reading
water_cost = 0
total_bill = 0

if consumption <= 20:
    water_cost = 0.57
elif consumption <= 35:
    water_cost = 1.03
else:
    water_cost = 1.40

water_cost = consumption * water_cost
total_bill = water_cost + 8 + 2

print(consumption)
print(water_cost)
print(total_bill)
