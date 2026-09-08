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

# Get two numbers from the user for comparative analysis
number_1 = int(input(f"\n\tPlease enter an integer for comparison: \t"))
number_2 = int(input(f"\n\tPlease enter another integer for comparison: \t"))

# Perform 6 logic checks on the two numbers:
if number_1 > 0 and number_2 > 0:  # Are they both positive?
    print(f"\n\tBoth are positive.")
else:
    print(f"\n\tAt least one of your numbers is negative.")

if number_1 > 100 and number_2 > 100:  # Are they both greater than 100?
    print(f"\n\tBoth greater than 100.")
else:
    print(f"\n\tAt least one of your numbers is less than 100.")

if (number_1 % 2 == 0) or (number_2 % 2 == 0):  # Is EITHER of them an even number?
    print(f"\n\tOne of these is even.")
else:
    print(f"\n\tNeither of your numbers is an even number.")

if (number_1 < 100) or (number_2 < 100):  # Is EITHER of them less than 100?
    print(f"\n\tOne of these is less than 100")
else:
    print(f"\n\tNeither of your numbers is less than 100.")

if number_1 != number_2:  # Are they the SAME/Equal number?
    print(f"\n\tThese numbers are NOT the same.")
else:
    print(f"\n\tThese numbers are the same.")

if not (number_1 == 0 or number_2 == 0):  # Are neither of them zeros?
    print(f"\n\tThese numbers are NOT 0!")
else:
    print(f"\n\tAt least one of these numbers is 0!")


# Categorize first number provided above as Positive, Negative, Zero
if number_1 > 0:
    print(f"\n\n\tYour first number, {number_1}, is a positive number!")
elif number_1 < 0:
    print(f"\n\n\tYour first number, {number_1}, is an negative number!")
else:
    print(f"\n\n\tYour first number was a 0 (zero)!")


print(f"\n\n\tThanks for your time!")
print("\n\n")
