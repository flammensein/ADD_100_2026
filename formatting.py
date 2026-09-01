# col_rent = 1500
# col_utilities = 300
# col_phone = 55

# head_rent = "Rent"
# head_utilities = "Utilities"
# head_phone = "Phone"

# expenses = col_phone + col_rent + col_utilities
# phone_percent = col_phone / expenses

# # print(f"{head_rent:^20}{head_utilities:^20}{head_phone:^20}")
# # print(f"{col_rent:^20}{col_utilities:^20}{col_phone:^20}")

# print(f"\n\nPhone percent of expenses is:   {phone_percent:.2%}")
"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

monthly_income = float(input("\n\n\tPlease enter your monthly GROSS income:\t$   "))
monthly_rent = float(input("\n\tPlease enter your monthly rent cost:\t$   "))
monthly_utilities = float(input("\n\tPlease enter your monthly utilities:\t$   "))
monthly_bills = float(input("\n\tPlease enter your monthly bills:\t$   "))
monthly_debt = float(input("\n\tPlease enter your monthly debt payment:\t$   "))
