# Multiple independent health checks - use multiple if statements
weight = 100  # kg
height = 1.75  # meters
age = 17
exercise_hours = 2  # per week

bmi = weight / (height * height)

# Each check is independent - multiple can be True
if bmi >= 25:
    print("Recommendation: Consider weight management")
    print(f"BMI = {bmi}")
if age >= 40:
    print("Recommendation: Schedule regular health checkups")
    
if exercise_hours < 3:
    print("Recommendation: Increase physical activity")
    
if bmi < 18.5:
    print("Recommendation: Consider increasing caloric intake")