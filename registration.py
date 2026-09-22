"""
-----------------------------------------------------------------------
ASSIGNMENT: DANCE TICKET REGISTRATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All inputs are validated.
[ ] 3. The program runs in a loop until the user chooses to stop.
[ ] 4. A try/except block is used to handle invalid input.
[ ] 5. A generic exception is included for unexpected errors.
-----------------------------------------------------------------------
"""

# ℹ️ Wrap the entire program in an outer try/except to catch any unexpected failure.
try:
    # ℹ️ Initialize values outside the main loop so they persist across dancer entries.
    ticket_count = 0
    more_tickets = True
    of_age_tickets = 0

    # 📌 Continue processing while the user wants to add more dancers.
    while more_tickets:
        # ℹ️ Ask for the first name and keep prompting until it is not blank.
        first_name = ""
        while not first_name:
            try:
                first_name = input(
                    "\n\tPlease enter the dancer's first name:\t"
                ).strip()
                first_name = first_name.capitalize()
            except ValueError:
                print("\n\tInvalid entry. Please try again.")
            except Exception as e:
                print(f"\n\tAn unexpected error occurred: {e}")

        # ✅ A valid first name was entered.
        print("\n\tThank you!")

        # ℹ️ Ask for the last name and validate it in the same way.
        last_name = ""
        while not last_name:
            try:
                last_name = input("\n\tPlease enter the dancer's last name:\t").strip()
                last_name = last_name.capitalize()
            except ValueError:
                print("\n\tInvalid entry. Please try again.")
            except Exception as e:
                print(f"\n\tAn unexpected error occurred: {e}")

        # 💡 This keeps the output personal and clear for the current dancer.
        print(
            f"\n\tThank you! We have a couple more questions about {first_name} {last_name}.\n"
        )

        # ℹ️ Validate the dancer's age and allow only realistic values.
        valid_entry = False
        while not valid_entry:
            try:
                dancer_age = int(input("\n\tPlease tell us the dancer's age:\t"))

                if dancer_age <= 0:
                    print("\n\tPlease enter a valid number for their age.")
                elif dancer_age > 117:
                    print(
                        "\n\tAs of the creation of this program, the oldest person alive is 117. "
                        "Please enter their real age.\n"
                    )
                elif dancer_age >= 21:
                    # ✅ Age 21 or older qualifies for a drink ticket.
                    print(
                        "\n\tThis dancer is age appropriate for a drink ticket with their dance ticket. "
                        "Please drink responsibly and have fun!\n"
                    )
                    of_age_tickets += 1
                    valid_entry = True
                elif dancer_age <= 20:
                    # ✅ Valid underage dancer entry.
                    print("\n\tThank you!\n")
                    valid_entry = True
                else:
                    print(
                        "\n\tYou must enter an integer for their age (e.g. 42 not Forty-Two).\n"
                    )
            except ValueError:
                print("\n\tInvalid entry. Please try again.")
            except Exception as e:
                print(f"\n\tAn unexpected error occurred: {e}")

        # ⚠️ Phone number is checked for a value, but could be validated further for digits and length.
        phone_num = ""
        while not phone_num:
            try:
                phone_num = input(
                    "\n\tPlease enter the dancer's 10-digit phone number:\t"
                ).strip()
            except ValueError:
                print("\n\tInvalid entry. Please try again.")
            except Exception as e:
                print(f"\n\tAn unexpected error occurred: {e}")

        # ℹ️ Ask how many tickets they want and validate the number.
        try:
            if ticket_count <= 0:
                ticket_count = int(
                    input(
                        f"\n\tHow many tickets would {first_name} {last_name} like?:\t"
                    )
                )
            else:
                added_tickets = int(
                    input("\n\tHow many additional tickets would this dancer like?:\t")
                )
                ticket_count += added_tickets
        except ValueError:
            print("\n\tInvalid entry. Please try again.")
            continue
        except Exception as e:
            print(f"\n\tAn unexpected error occurred: {e}")
            continue

        # ✅ Display the current ticket total for this dancer.
        print(f"\n\tYou are set to order {ticket_count} ticket(s).\n")

        # 📌 Ask if the user wants to add more dancers and normalize the response with .upper().
        yes_no = (
            input(
                "\n\tWould you like to add tickets for other dancers to your purchase? (Y/N):\t"
            )
            .strip()
            .upper()
        )

        # 💡 Boolean logic is clearer when we set the flag directly.
        if yes_no == "N":
            more_tickets = False
        elif yes_no == "Y":
            more_tickets = True
        else:
            print("\n\tInvalid Input, please enter 'Y' for Yes or 'N' for No.")
            # Keep the loop going until the answer is valid.
            more_tickets = True

    # ✅ Final summary after all dancers have been processed.
    print("\n\n")
    print(
        f"\n\tYour final order will include {ticket_count} dance ticket(s) and {of_age_tickets} drink tickets.\n"
    )
    print(
        "\n\tEnjoy the dance and have fun! \n\tDrink responsibly and designate a sober driver in advance. \n\tSomeone loves you."
    )
    print("\n\n")

except ValueError:
    print("\n\tA value error occurred. Please check your inputs and try again.")

except Exception as e:
    print(f"\n\tAn unexpected error occurred: {e}")
    print("\n\tThe program is shutting down. Please try again later.")
