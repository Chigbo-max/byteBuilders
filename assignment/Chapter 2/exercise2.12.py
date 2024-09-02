number_of_years = int(input("Enter number of years: "))
principal = float(input("Enter principal amount: "))
RATE = 0.07

amount = principal * ((1 + RATE)**number_of_years)

print("The amount of deposit at the end of", number_of_years, "years is","$",round(amount,2))