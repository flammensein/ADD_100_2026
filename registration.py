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

    First Name & Last Name: Cannot be blank.
 ✅   Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
    Phone Number: Cannot be blank.
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

first_name = input(f"")
while first_name == "":
    print(f"")
    first_name = input(f"")


# last_name = input(f"")
# while last_name == "":
#     print(f"")
#     last_name = input(f"")


# dancer_age = 0
# while True:
#     try:
#         dancer_age = int(input(f"\n\tPlease tell us the dancer's age:\t"))
#         if dancer_age <= 0:
#             print(f"\n\tPlease enter a valid number for your age.")
#         elif dancer_age > 117:
#             print(
#                 f"\n\tAs of the creation of this program, the oldest person alive is 117. And I doubt you are that person. Please enter a valid number for your age.\n\n"
#             )
#         elif dancer_age > 20:
#             print(
#                 f"\n\tYou are age appropriate to receive a drink ticket with your dance ticket. Please drink responsibly and have fun!\n\n"
#             )
#         else:
#             print(f"\n\tThank you!\n\n")
#     except ValueError:
#         print(
#             f"\n\tYou must enter an integer as a number for your age (e.g. 42 not Forty-Two).\n\n"
#         )

# phone_num = input(f"")


# ticket_count = input(f"")


# more_tickets = input(f"")
