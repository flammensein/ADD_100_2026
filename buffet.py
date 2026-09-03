"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: 09-03-2026
FILE: buffet.py
-----------------------------------------------------------------------
"""

# 1: Ask the user for the day of the week.
today_is = input(str(f"\n\n\tPlease enter what day of the week today is:\t"))

# 2: Use .lower() with the day input.
# ℹ️ Done as part of Match/Case statement below.

# 3: Use match/case to set child_price_per_year.
# Tuesday: $0.50 per year.
# Sunday: $1.00 per year and print the free-drinks notice.
# Every other day: $1.00 per year using the default case (case _).
match today_is.lower():
    case "tuesday":
        child_price_per_day = float(0.50)
    case "sunday":
        child_price_per_day = float(1.00)
        print(f"\n\tDrinks are free on Sundays!\n")
    case _:
        child_price_per_day = float(1.00)

# 4: Ask the user for their age and convert it to an integer.
diner_age = int(input(f"\n\tPlease tell us how old you are:\t"))

# 5: Use if/elif/else to calculate the price.
# Under 1: FREE ($0.00)
# Ages 1 to 12: age multiplied by child_price_per_year
# Ages 13 to 64: $16.95
# Age 65 and older: $12.95
if diner_age < 1:
    final_price = float(0.00)
elif diner_age < 13:
    final_price = child_price_per_day * diner_age
elif diner_age < 64:
    final_price = float(16.95)
else:
    final_price = float(12.95)


# 6: Print the final price formatted as currency.

print(f"\n\tToday, your drink will cost:\t${final_price:.2f}\n\n")
