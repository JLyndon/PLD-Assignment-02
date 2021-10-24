QuantApl = int(input("How many apples? \n> "))
QuantOrng = int(input("\nHow many oranges? \n> "))

ttlprc_apl = float(QuantApl*20)
ttlprc_orng = float(QuantOrng*25)
grnd_total = ttlprc_apl + ttlprc_orng

print(f"\nThe total amount for apples is {ttlprc_apl: .2f} Php.")
print(f"The total amount for oranges is {ttlprc_orng: .2f} Php.")

print(f"\nThe total amount is {grnd_total:.2f} .")
