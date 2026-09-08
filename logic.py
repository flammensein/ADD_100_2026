"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Get number 1
number_1 = int(input(f"\n\tPlease enter an integer for comparison: \t"))

# Get number 2
number_2 = int(input(f"\n\tPlease enter another integer for comparison: \t"))

# Logic Check 1
if number_1 > 0 and number_2 > 0:
    print(f"\n\tBoth are positive.")
# Logic Check 2
if number_1 > 100 and number_2 > 100:
    print(f"\n\tBoth greater than 100.")
# Logic Check 3
if (number_1 % 2 == 0) or (number_2 % 2 == 0):
    print(f"\n\tOne of these is even.")
# Logic Check 4
if (number_1 < 100) or (number_2 < 100):
    print(f"\n\tOne of these is less than 100")
# Logic Check 5
if not (number_1 == number_2):
    print(f"\n\tThese numbers are NOT the same.")
# Logic Check 6
if not (number_1 == 0 and number_2 == 0):
    print(f"\n\tThese numbers are NOT 0!")


# TODO if/elif/else categorize first num (item 4 above)


print("\n\n")
