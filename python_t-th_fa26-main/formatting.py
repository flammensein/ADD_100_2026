# 🧾 FORMATTING EXAMPLES
# Python can format output neatly using f-strings.
# An f-string lets us insert variables directly into text.

# 💡 Tip: use f"{variable}" to print data with text.
name = "Meri"
age = 55

print(name + " is " + str(age) + " years old")
print(f"{name} is {age} years old.")

# 🧮 These variables represent monthly expenses.
col_rent = 1500
col_utilities = 300
col_phone = 55

head_rent = "Rent"
head_utilities = "Utilities"
head_phone = "Phone"

expenses = col_rent + col_utilities + col_phone
phone_percent = col_phone / expenses

# 📐 The :^20 format centers text in a space of 20 characters.
print(f"{head_rent:^20}{head_utilities:^20}{head_phone:^20}")
# 💡 The :>20 format right-aligns numbers.
print(f"{col_rent:>20}{col_utilities:>20}{col_phone:>20}")

# 📊 The :.2% format turns a decimal into a percent with 2 digits after the decimal.
print(f"\n\nPhone percent of expenses is:  {phone_percent:.2%}")

days_in_month = 365 / 12
average_daily_rent = col_rent / days_in_month

# 💵 The :, and .2f formatting makes currency display neatly.
print(f"The average daily rent is: $ {average_daily_rent:20,.2f}")

# ⚠️ Warning: if you try to add a number and a string, Python will fail.
# ✅ Use str() when combining text and numbers in older-style concatenation.
