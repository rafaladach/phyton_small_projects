print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

payment = (total_bill / people) + (total_bill * 0.01 * (tip / people))
new_payment = round(payment, 2)
print(f"Each person should pay: ${new_payment}")