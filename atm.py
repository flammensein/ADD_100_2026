"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

current_balance = 1000.00


# create a menu
is_running = True

while is_running:
    # will continue displaying the menu until the user selects exit
    print("\n")
    print("\t1...Check Balance")
    print("\t2...Make a Deposit")
    print("\t3...Withdrawal Cash")
    print("\t0...Exit Capitalism")

    try:
        choice = int(input("\nPlease select an action from the menu above:\t"))
    except ValueError:
        print("\n\tYou have made an invalid selection.")
        print("\tPlease enter the NUMBER of your selection from the menu.")
        continue

    match choice:
        case 1:
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            continue
        case 2:
            print(f"\n\tMake a Deposit:")
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            try:
                deposit = float(
                    input(f"\tPlease enter the amount you would like to deposit:\t$")
                )
                if deposit <= 0:
                    print("\n\tDeposit amounts must be greater than $0.00")
                else:
                    current_balance += deposit
                    print(f"\n\tYour deposit of ${deposit:.2f} was successful")
                    print(f"\n\tYour new balance is: ${current_balance:.2f}\n")
            except ValueError:
                print("\n\tInvalid input. Please try again.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue
        case 3:
            print(f"\n\tWithdrawal Cash:")
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            try:
                cash_out = float(
                    input(f"\tPlease enter the amount you would like to withdrawal:\t$")
                )
                if (cash_out <= 0) or ((cash_out % 5) != 0):
                    print(
                        "\n\tWithdrawal amounts must be greater than $5.00 and in $5 increments."
                    )
                elif cash_out > current_balance:
                    print(
                        f"Unfortunately ${cash_out:.2f} is greater than your balance of ${current_balance:.2f}"
                    )
                    continue
                else:
                    current_balance -= cash_out
                    print(f"\n\tYour withdrawal of ${cash_out:.2f} was successful")
                    print(f"\n\tYour new balance is: ${current_balance:.2f}\n")
                    continue
            except ValueError:
                print("\n\tInvalid input. Please try again.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue
        case 0:
            print("\n\tSo long, and thanks for all the fish!!")
            is_running = False
        case _:
            print("\n\tYou have made an invalid selection.")
            continue

print(f"\n\tThank you for participating in capitalism!!")
print(f"\n\t{'=' * 35}")
print(f"\t...POWERING DOWN...")
print(f"\t{'=' * 35}\n")
