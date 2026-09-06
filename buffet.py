"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: 09-03-2026
FILE: buffet.py
-----------------------------------------------------------------------

This program calculates a diner's buffet cost using user input of the day
of the week and the age of the diner to determine discounts to apply.
"""

# Set the child rate and Sunday promotion.
today_is = input(f"\n\n\tPlease enter current day of the week:\t")

match today_is.lower():
    case "tuesday":
        child_price_per_day = float(0.50)
    case "sunday":
        child_price_per_day = float(1.00)
        print(f"\n\tDrinks are free on Sundays!\n")
    case _:
        child_price_per_day = float(1.00)

# Categorize the diner and calculate the buffet price.
diner_age = int(input(f"\n\tPlease tell us your age:   \t"))

if diner_age < 1:
    final_price = float(0.00)
elif diner_age < 13:
    # Children pay their age multiplied by the daily rate.
    final_price = child_price_per_day * diner_age
elif diner_age < 65:
    final_price = float(16.95)
else:
    final_price = float(12.95)


# Display the final price.
print(f"\n\tYour cost today is:   \t\t${final_price:.2f}\n\n")
