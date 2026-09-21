"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------

Part 1: The Code
Create a registration form (registration.py) in which each input is validated using a while loop.  Registration for a dance:
Requirements:

 ✅   First Name & Last Name: Cannot be blank.
 ✅   Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
 ✅   Phone Number: Cannot be blank.
    Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
    Additional Tickets? (Y/N) (Extra credit - 5 points- start the whole process over if they say yes!)


Part 2: The Screenshot
While your program is running in Debug Mode, take a screenshot of your VS Code window. I must be able to see:

    A red breakpoint on one of your lines.
    The Watch window on the left shows at least one of your variables.

Submission Items:

    The GitHub Link to your registration.py file.
    The Image File (.png or .jpg) of your Debug/Watch screenshot.


"""

# Putting these outside the main look to avoid resetting it after each loop.
ticket_count = 0
more_tickets = True
of_age_tickets = 0

while more_tickets == True:
    first_name = ""
    while (
        not first_name
    ):  # loops until the user enters a value that meets our bare minimal requirements of a first name
        try:
            first_name = input(f"\n\tPlease enter the dancer's first name:\t").strip()
            first_name = first_name.capitalize()
            print(f"\n\tThank you! ")
        except ValueError:
            print("\n\tInvalid entry. Please try again.")
            continue
        except Exception as e:
            # Handles unexpected errors without stopping the program.
            print(f"\n\tAn unexpected error occurred: {e}")
            continue

    last_name = ""
    while (
        not last_name
    ):  # loops until the user enters a value that meets our bare minimal requirements of a last name
        try:
            last_name = input(f"\n\tPlease enter the dancer's last name:\t").strip()
            last_name = last_name.capitalize()
            print(
                f"\n\tThank you! We have a couple more questions about {first_name} {last_name}.\n"
            )
        except ValueError:
            print("\n\tInvalid entry. Please try again.")
            continue
        except Exception as e:
            # Handles unexpected errors without stopping the program.
            print(f"\n\tAn unexpected error occurred: {e}")
            continue

    valid_entry = False
    while not valid_entry:  # loops until the user enters a valid entry
        try:
            dancer_age = int(input(f"\n\tPlease tell us the dancer's age:\t"))
            if dancer_age <= 0:
                print(f"\n\tPlease enter a valid number for their age.")
            elif dancer_age > 117:
                print(
                    f"\n\tAs of the creation of this program, the oldest person alive is 117. And it is doubtful they are here. Please enter their real age.\n\n"
                )
            elif dancer_age > 20:
                # accepts an 'of age' valid entry, ends the loop, and moves on.
                print(
                    f"\n\tThis dancer is age appropriate for a drink ticket with their dance ticket. Please drink responsibly and have fun!\n\n"
                )
                of_age_tickets += 1
                valid_entry = True
            else:
                # accepts an 'under age' valid entry, ends the loop, and moves on.
                print(f"\n\tThank you!\n\n")
                valid_entry = True
                print(
                    f"\n\tYou must enter an integer for their age (e.g. 42 not Forty-Two).\n\n"
                )
        except ValueError:
            print("\n\tInvalid entry. Please try again.")
            continue
        except Exception as e:
            # Handles unexpected errors without stopping the program.
            print(f"\n\tAn unexpected error occurred: {e}")
            continue

    phone_num = ""
    # Loops until a value is entered.
    # ⚠️ Accepts any non-null value, but if I were to deploy this for real I would learn how to make it detect
    # the number of characters input, ensure they were all numbers, and that there were 10 numerical digits.
    while not phone_num:
        phone_num = input(
            f"\n\tPlease enter the dancer's 10-digit phone number:\t"
        ).strip()

    try:
        if ticket_count <= 0:
            ticket_count = int(
                input(f"\n\tHow many tickets would {first_name} {last_name} like?:\t")
            )
            # print(f"Ticket Count:\t{ticket_count}")
            # break
        elif ticket_count > 0:
            added_tickets = int(input(f"\n\tHow many tickets would this dancer?:\t"))
            # print(f"Ticket Count:\t{ticket_count}")
            # print(f"Added Tickets:\t{added_tickets}")
            ticket_count += added_tickets
            # print(f"Ticket Count:\t{ticket_count}")
            # break
    except ValueError:
        print("\n\tInvalid entry. Please try again.")
        continue
    except Exception as e:
        # Handles unexpected errors without stopping the program.
        print(f"\n\tAn unexpected error occurred: {e}")
        continue

    print(f"\n\tYou are set to order {ticket_count} ticket(s). \n")

    # yes_no = "y"
    # while yes_no == "y":
    # try:
    yes_no = input(
        f"\n\tWould you like to add tickets for other dancers to your purchase? (Y/N):\t"
    ).lower()
    # print(f"yes_no:\t{yes_no}")
    if yes_no == "n":
        # print(f"yes_no:\t{yes_no}")
        more_tickets = False
        # break
    elif yes_no == "y":
        # print(f"yes_no:\t{yes_no}")
        more_tickets = True
        # break
    else:
        # print(f"yes_no:\t{yes_no}")
        print(f"\n\tInvalid Input, please enter 'Y' for Yes or 'N' for No.")
        # continue
        # except Exception as e:
        # print(f"\n\tAn unexpected error occurred:  {e}")


print(f"\n\n")
print(
    f"\n\tYour final order will include {ticket_count} dance ticket(s) and {of_age_tickets} drink tickets. \n"
)
print(
    f"\n\tEnjoy the dance and have fun! Always drink responsibly and designate a driver if using private transportation. Someone love you."
)
