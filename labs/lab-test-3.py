"""
This is a comment for calculating total bill based on monthly usage and discount.
"""
monthly_usage = float(input("Enter the monthly usage:"))# Monthly Usage 
total_bill = 0
if monthly_usage > 0: #Making sure the number is not negative
    if monthly_usage < 50: # 1 - 49
        total_bill = monthly_usage
    elif monthly_usage < 101: # 50 - 100
        total_bill = monthly_usage - (monthly_usage * 0.05)
    else: #100 and more
        total_bill = monthly_usage - (monthly_usage * 0.20)
    print (f"{total_bill:2n}")
else:
    ("Please input a positive number")