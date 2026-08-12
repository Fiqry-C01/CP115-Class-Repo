# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
#This is the pricing of item
coffee = 3.50
muffin = 2.10
water = 1.05
#This is the quantity that the customer ask
coffeeQty = int(input("How many coffe you need?: "))
muffinQty = int(input("How many muffin you need?: "))
waterQty = int(input("How many water you need?: "))
coffeeTtl = 3.5 * coffeeQty
muffinTtl = 2.10 * muffinQty
waterTtl = 1.05 * waterQty
subtotal = ((coffee * coffeeQty) + (muffin * muffinQty) + (water * waterQty))
tax = subtotal * 0.06
total = subtotal + tax
print (f"========== RECEIPT ==========\nItem\tPrice\tQty Total")
print (f"Coffee\t${coffee:.2f}\t{coffeeQty}   ${waterTtl}")
print (f"Muffin\t${muffin}\t{muffinQty}   ${muffinTtl}")
print (f"Water\t${water}\t{waterQty}  ${waterTtl}")
print ("------------------------------")
print (f"Subtotal\t${subtotal}")
print (f"Tax(6%)\t        ${tax}")
print (f"Total\t      ${total}")

"""
Hello
"""
