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
gross_income = float(input("\n\n\tPlease enter your monthly GROSS income:\t$   "))
monthly_rent = float(input("\n\tPlease enter your monthly rent cost:\t$   "))
monthly_utilities = float(input("\n\tPlease enter your monthly utilities:\t$   "))
monthly_bills = float(input("\n\tPlease enter your monthly bills:\t$   "))
monthly_debt = float(input("\n\tPlease enter your monthly debt payment:\t$   "))


# Perform budget calculations
net_income = gross_income * 0.8
tot_expenses = monthly_bills + monthly_debt + monthly_rent + monthly_utilities
income_remaining = net_income - tot_expenses
percent_income = float((tot_expenses / net_income))
discretionary_income = float((income_remaining / net_income))

# Print the formatted report
print(f"\n\n")
print(f"\t{'=' * 35:^35}")
print(f"\t{'BASIC PERSONAL BUDGET':^35}")
print(f"\t{'=' * 35:^35}")
print(f"\t{'Gross Income:':<20}\t${gross_income:>10.2f}\n")
print(f"\t{'Net Income:'  :<20}\t${net_income:>10.2f}\n")
print(f"\t{'Total Expenses:'  :<20}\t${tot_expenses:>10.2f}\n")
print(f"\t{'Discretionary Income:':<20}\t${income_remaining:>10.2f}\n")
print(f"\t{'Expensed Income:':<20}\t{percent_income:>10.2%}\n")
print(f"\t{'Discretionary Income:':<20}\t{discretionary_income:>10.2%}\n")
print(f"\n\n")
