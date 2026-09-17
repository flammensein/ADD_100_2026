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

# ℹ️ Starting balance for the ATM account.
current_balance = 1000.00

# ℹ️ Keeps the ATM running until the user exits.
is_running = True

while is_running:
    # 📌 Displays the main menu.
    print("\n")
    print("\t1...Check Balance")
    print("\t2...Make a Deposit")
    print("\t3...Withdrawal Cash")
    print("\t0...Exit Capitalism")

    # ℹ️ Reads user input and validates it as a number.
    try:
        choice = int(input("\nPlease select an action from the menu above:\t"))
    except ValueError:
        # Invalid menu input is rejected to prevent crashes.
        print("\n\tYou have made an invalid selection.")
        print("\tPlease enter the NUMBER of your selection from the menu.")
        continue

    # 📌 Uses match-case to handle menu selections.
    match choice:
        case 1:
            # Displays the current balance in currency format.
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            continue

        case 2:
            # 📌 Deposit section updates the account balance.
            print(f"\n\tMake a Deposit:")
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            try:
                deposit = float(
                    input(f"\tPlease enter the amount you would like to deposit:\t$")
                )
                # Prevents negative or zero deposits.
                if deposit <= 0:
                    print("\n\tDeposit amounts must be greater than $0.00")
                else:
                    current_balance += deposit
                    print(f"\n\tYour deposit of ${deposit:.2f} was successful")
                    print(f"\n\tYour new balance is: ${current_balance:.2f}\n")
            except ValueError:
                # Rejects non-numeric deposit values.
                print("\n\tInvalid input. Please try again.")
                continue
            except Exception as e:
                # Handles unexpected errors without stopping the program.
                print(f"An unexpected error occurred: {e}")
                continue

        case 3:
            # 📌 Withdrawal section checks amount and available funds.
            print(f"\n\tWithdrawal Cash:")
            print(f"\n\tYour current Account Balance is: ${current_balance:.2f}\n")
            try:
                cash_out = float(
                    input(f"\tPlease enter the amount you would like to withdrawal:\t$")
                )
                # Prevents invalid withdrawals and overdrafts.
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
                # Rejects non-numeric withdrawal values.
                print("\n\tInvalid input. Please try again.")
                continue
            except Exception as e:
                # Handles unexpected errors safely.
                print(f"An unexpected error occurred: {e}")
                continue

        case 0:
            # Exits the loop and ends the ATM session.
            print("\n\tSo long, and thanks for all the fish!!")
            is_running = False

        case _:
            # Handles invalid menu selections.
            print("\n\tYou have made an invalid selection.")
            continue

# ℹ️ Shutdown message shown after the program ends.
print(f"\n\tThank you for participating in capitalism!!")
print(f"\n\t{'=' * 35}")
print(f"\t...POWERING DOWN...")
print(f"\t{'=' * 35}\n")
