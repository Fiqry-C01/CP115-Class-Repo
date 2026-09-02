# Complex BODMAS example
expression = 3 + 2 ** 2 * 4 - 6 / 2
print(f"3 + 2 ** 2 * 4 - 6 / 2 = {expression}")

# Let's break it down step by step
step1 = 2 ** 2    
step2 = step1 * 4  
step3 = 6 / 2     
final = 3 + step2 - step3 
print(f"Step 1 (Powers): 2 ** 2 = {step1}")
print(f"Step 2 (Multiply): {step1} * 4 = {step2}")
print(f"Step 3 (Division): 6 / 2 = {step3}")
print(f"Final: 3 + {step2} - {step3} = {final}")