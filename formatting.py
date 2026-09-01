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

# Get input for calculations ----
gross_income = float(6686.20)
monthly_rent = float(1220.50)
monthly_utilities = float(200.00)
monthly_bills = float(400)
monthly_debt = float(2000)
# gross_income = float(input("\n\n\tPlease enter your monthly GROSS income:\t$   "))
# monthly_rent = float(input("\n\tPlease enter your monthly rent cost:\t$   "))
# monthly_utilities = float(input("\n\tPlease enter your monthly utilities:\t$   "))
# monthly_bills = float(input("\n\tPlease enter your monthly bills:\t$   "))
# monthly_debt = float(input("\n\tPlease enter your monthly debt payment:\t$   "))
# print("\n" + "=" * 90)
print(f"{'=' * 90:^90}")
print(f"{'Thank you! Your expense report/calculations are as follows:':^90}")
print(f"{'=' * 90:^90}")

# Perform budget calculations
net_income = gross_income * 0.8
tot_expenses = monthly_bills + monthly_debt + monthly_rent + monthly_utilities
income_remaining = net_income - tot_expenses


# Print the formatted report
print(f"\n\n{'BASIC PERSONAL BUDGET (A SUMMARY)':^40}")
print(
    f"{'Gross Income':>15}{'Net Income':>15}{'Rent':>15}{'Utilities':>15}{'Other Bills':>15}{'Other Debt':>15}"
)


print(
    f"{gross_income:>15,.2f}{net_income:>15,.2f}{monthly_rent:>15,.2f}{monthly_utilities:>15,.2f}{monthly_bills:>15,.2f}{monthly_debt:>15,.2f}\n"
)
