import math

usr_balance = float(input("Enter your balance: "))
apl_price = float(input("Enter the price of an apple: "))

max_no_apl = math.floor(usr_balance/apl_price)
change = float(usr_balance%apl_price)

print(f"\nYou can buy {max_no_apl} apples and your change is {change: .2f} pesos.")