QuantApl = int(input("How many apples? \n> "))
QuantOrng = int(input("\nHow many oranges? \n> "))

apl_price = 20
orng_price = 25

ttlprc_apl = QuantApl*apl_price
ttlprc_orng = QuantOrng*orng_price
grnd_total = ttlprc_apl + ttlprc_orng

print(f"\nThe total amount is {grnd_total}.")
