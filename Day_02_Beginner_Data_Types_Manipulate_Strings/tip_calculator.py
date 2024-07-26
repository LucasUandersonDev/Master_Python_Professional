print("Welcome to the tip calculator!")
# tip_calculator.py
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = total_bill * (1 + tip / 100)
print(f"Your total bill with tip is: ${bill_with_tip:.2f}")


