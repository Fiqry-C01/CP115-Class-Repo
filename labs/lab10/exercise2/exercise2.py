num_days = int(input())
danger_threshold = float(input())
i = 0
danger_days = 0
total_temperature = 0

for i in range (0,num_days):
    temperature = float(input())
    if temperature > danger_threshold:
        danger_days += 1
    total_temperature += temperature

average_temp = total_temperature / num_days

print(danger_days)
print(f"{average_temp:.1f}")
