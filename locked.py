"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

DEPT_IN = [
    "Book Store",
    "Finance",
    "Help Desk",
    "Book Store",
    "Administration",
    "Human Resources",
    "Student Services",
    "Facilities",
    "Academic Affairs",
]

USER_NAMES = (
    "abaker",
    "bcarter",
    "cday",
    "dellis",
    "efoster",
    "ggrant",
    "hharper",
    "ijackson",
    "jkennedy",
    "klee",
    "lmorgan",
    "nnelson",
    "oparker",
    "pquinn",
    "rreid",
    "sroberts",
    "tstone",
    "uturner",
    "vunderwood",
    "wwalker",
    "xwang",
    "yyoung",
    "zzimmerman",
    "amartin",
    "bthompson",
    "cwilson",
    "dwright",
    "evargas",
    "gpatel",
    "hkim",
)

passwords = [
    "6ba11a0bafccb9c7",
    "5b723b4cbe258108",
    "a00b7a06add04cb5",
    "9163d29e54692537",
    "b695d5887806beee",
    "1bdf5ef664d56fea",
    "bcf3b7026363fcc6",
    "052689cfe4378156",
    "999918bfa3e9f209",
    "fca2cf45541c6312",
    "a7c20bf7e6695d1e",
    "b3cf30c358005477",
    "5d5cea35f84f7247",
    "3202ccf675ab335e",
    "a579b68ca36ea785",
    "7096b3cd49708aad",
    "0102af5683b97e15",
    "9192fc22ccf1f99d",
    "8d04f5bdd1cac1a0",
    "a47ea8027f25ce03",
    "20638195a1348fd2",
    "642dcef62980fcc3",
    "18afbb9823e8ffb5",
    "31539c15e64d1adc",
    "5fd476c8d2a7d795",
    "25795a66d2a3e8ba",
    "10f1d9afff3362fe",
    "aa8e4ae4fd6b1074",
    "547dcc297f2d2898",
    "81a06e94c2c12286",
]

"""
List of Requirements:

Extra credit: Ask for employee category from a menu; only let IT or ADMIN change the username! +5

✅    Header Docstring: Include the complete checklist docstring at the top of your file. (Note: Do not include student names per grading policy).
✅    Department Constant: Define a system constant in ALL_CAPS representing your department name.
✅    Parallel Structures: Define a constant tuple for usernames (`USER_NAMES`) and a parallel mutable list for passwords (`passwords`).
ℹ️    Interactive `while` Loop: Use a persistent while loop to keep the terminal running so users can look up users, update passwords, attempt to add a user. Provide a menu of options - lookup username (if statement, yes that is an employee, no that is not an employee), change username, change password, quit - change username will break
ℹ️    The Tamper Trap (`try/except`): Allow the user to attempt changing a username inside the tuple. Catch the resulting TypeError and print a message telling the user to email the help desk because usernames cannot be changed.
ℹ️    Password Updates: Allow the user to update a password inside the mutable list using a valid index. (Get the index of the username, use to update the password)
ℹ️    Error Handling: Gracefully catch ValueError and IndexError when handling index lookups or numerical input.
"""

keep_running = "y"

while keep_running != "n":
    try:
        print(f"\n\tPlease choose an action from the following list:\n")
        print(f"\n\t0. Quit Program")
        print(f"\n\t1. Lookup UserName")
        print(f"\n\t2. Change a User's UserName")
        print(f"\n\t3. Change a User's Password")
        selected_option = input(f"\n\tEnter Option Here:\t")

        match selected_option:
            case "0":
                keep_running = "n"
                break
            case "1":
                username_query = input(f"\n\tEnter the username to search for:\t")
                if username_query in USER_NAMES:
                    print(f"\n\fThe user {username_query} is a valid username.")
                continue
            case "2":
                print(f"\n\tSorry, only a member of IT can change a user's username.")
                print(
                    f"\n\tPlease contact the Help Desk to create a Name Change Request."
                )
                continue
            case "3":
                print(
                    f"\n\tYou must be a member of a department authorized to reset user passwords."
                )
                print(f"\n\t1. Book Store")
                print(f"\t2. Finance")
                print(f"\t3. Help Desk")
                print(f"\t4. Book Store")
                print(f"\t5. Administration")
                print(f"\t6. Human Resources")
                print(f"\t7. Student Services")
                print(f"\t8. Facilities")
                print(f"\t9. Academic Affairs")
                what_your_dept = input(
                    f"\n\tPlease select your department from the list above (1-9):\t"
                )

                continue
            case _:
                print("\n\tInvalid entry. Please try again.")
                keep_running = "y"
                continue
    except ValueError:
        print("\n\tInvalid entry. Please try again.")
        keep_running = "y"
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")
        keep_running = "y"
