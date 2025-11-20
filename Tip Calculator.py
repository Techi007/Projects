#Tip Calculator

#Concept: The user enters the total bill amount and the percentage they want to tip. 
#The program calculates the tip and total cost.

#Example: $75.20, 5% of the total bill, (75.20*5 // 100) = result

billAmount = float(input("Enter bill amount: $"))
print("bill amount: $",billAmount)

tip_amount = float(input("Percentage you would like to tip: %"))
totalBill = (billAmount * tip_amount / 100) + billAmount

print("Total Bill: ",totalBill)

# maybe an if-statement deciding whether to tip or not.