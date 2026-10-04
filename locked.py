"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[✅ ] 1. Header Docstring included.
[✅ ] 2. Department constant defined in ALL_CAPS.
[✅ ] 3. Username tuple and password list defined.
[✅ ] 4. While loop runs interactively.
[✅ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------

    📌 I used the chatbot to incorporate the "List of Requirements" into the
    annotations. I felt it did a decent job, though I'm not sure if that's what
    I really think or if it's my desire to move on to the next task.

"""

### ℹ️ System constant defined in ALL_CAPS
DEPARTMENT = "SECURITY & IT ADMINISTRATION"

### ℹ️ Department list from initial assignment template
DEPT_IN = [
    "exit function",
    "Book Store",
    "Finance",
    "Help Desk",
    "Book Store",
    "IT Administration",
    "Human Resources",
    "Student Services",
    "Facilities",
    "Academic Affairs",
]

### ℹ️ USER_NAMES defined as a constant tuple (immutable)
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

### ℹ️ Parallel mutable list for passwords
passwords = [
    "Pass123!",
    "Secr3t!",
    "P@ssword1",
    "Admin2026",
    "SafePass99",
    "GrantPass!1",
    "Harper#2026",
    "Jackson$99",
    "Kennedy!123",
    "LeePass2026",
    "Morgan#88",
    "Nelson$77",
    "Parker!100",
    "Quinn#2026",
    "Reid$321",
    "Roberts!55",
    "Stone#2026",
    "Turner$44",
    "Underwood!9",
    "Walker#11",
    "Wang$2026",
    "Young!22",
    "Zimmerman#33",
    "Martin$2026",
    "Thompson!44",
    "Wilson#55",
    "Wright$66",
    "Vargas!77",
    "Patel#88",
    "Kim$2026",
]


# 📌 This is the Outer Loop, not to be confused with any iterations of "The Outer Limits"
# 📌 Extra Credit: Category Selection
print(f"\n\tWelcome to the {DEPARTMENT} Terminal!")

program_running = True

while program_running:
    print("\n\t--- EMPLOYEE CATEGORY MENU ---")
    print("\t1...Sales")
    print("\t2...Admin")
    print("\t3...IT")
    print("\t4...Production")
    print("\t5...Exit")

    category_choice = input("\n\tSelect an employee category (1-5):\t").strip().lower()

    if category_choice == "5":
        print(f"\n\tExiting {DEPARTMENT} Terminal.\n")
        program_running = False
        continue

    if category_choice not in ("1", "2", "3", "4"):
        print("\n\tInvalid category selection. Please try again.\n")
        continue

    is_it_user = category_choice == "3"

    if is_it_user:
        print("\n\tIT Category selected. Advanced options unlocked.\n")
    else:
        print("\n\tStandard Employee access granted.\n")

    terminal_running = True
    while terminal_running:
        # 📌 Displays the interactive menu options.
        print(f"\n\t{'-' * 55}")
        print(f"\t         {DEPARTMENT} TERMINAL")
        print(f"\n\t{'-' * 55}")
        print("\t0...Return to Category Menu")
        print("\t1...Lookup Username")
        print("\t2...Change Password")
        print("\t3...Request Username Change")
        if is_it_user:
            print("\t4...Add New Employee/Password (IT Only)")
        print(f"\n\t{'-' * 55}")

        try:
            choice = input("\n\tPlease select an action from the menu above:\t").strip()

            if choice == "1":
                # 📌 Option 1: Looking up Username
                search_user = (
                    input("\n\tPlease enter username to lookup:\t").strip().lower()
                )
                if search_user in USER_NAMES:
                    idx_loc = USER_NAMES.index(search_user)
                    print(
                        f"\n\t[INFO] User '{USER_NAMES[idx_loc]}' IS an active employee in {DEPARTMENT}.\n"
                    )
                else:
                    print(
                        f"\n\t[INFO] User '{search_user}' is NOT an employee in {DEPARTMENT}.\n"
                    )

            elif choice == "2":
                # 📌 Option 2: Changing Password
                search_user = (
                    input("\n\tPlease enter username to change password for:\t")
                    .strip()
                    .lower()
                )
                if search_user in USER_NAMES:
                    idx_loc = USER_NAMES.index(search_user)
                    new_pass = input(
                        f"\tPlease enter new password for '{USER_NAMES[idx_loc]}':\t"
                    ).strip()
                    if not new_pass:
                        raise ValueError("Password cannot be blank.")

                    # 💡 Update password in parallel mutable list
                    passwords[idx_loc] = new_pass
                    print(
                        f"\n\t[SUCCESS] Password updated successfully for user '{USER_NAMES[idx_loc]}'.\n"
                    )
                else:
                    print(
                        f"\n\t[ERROR] Username '{search_user}' does not exist in the system.\n"
                    )

            elif choice == "3":
                # 📌 Option 3: Request Username Change
                old_user = (
                    input("\n\tPlease enter current username to request change:\t")
                    .strip()
                    .lower()
                )
                if old_user in USER_NAMES:
                    print(
                        f"\n\t[NOTICE] Request to change username '{old_user}' has been submitted to IT."
                    )
                    print(
                        "\n\tNote: Usernames cannot be modified directly due to tuple immutability."
                    )

                    # 💡 Demonstration option for tuple immutability (triggers TypeError if "y" is chosen in the next line)
                    try_direct = (
                        input(
                            "\n\tWould you like to attempt direct username modification? (y/n):\t"
                        )
                        .strip()
                        .lower()
                    )
                    if try_direct == "y":
                        idx_loc = USER_NAMES.index(old_user)
                        USER_NAMES[idx_loc] = (
                            "new_username"  # 📌 Triggers TypeError Below!
                        )
                else:
                    print(
                        f"\n\t[ERROR] Username '{old_user}' does not exist in the system.\n"
                    )

            elif choice == "4" and is_it_user:
                # 📌 Extra Credit (+10 pts): Add New Employee/Password (IT Only)
                new_user = (
                    input("\n\tPlease enter new employee username to add:\t")
                    .strip()
                    .lower()
                )
                if not new_user:
                    raise ValueError("Username cannot be blank.")

                if new_user in USER_NAMES:
                    print(
                        f"\n\t[ERROR] Username '{new_user}' already exists in the system.\n"
                    )
                else:
                    new_pass = input(
                        f"\tPlease enter password for new user '{new_user}':\t"
                    ).strip()
                    if not new_pass:
                        raise ValueError("Password cannot be blank.")

                    # 💡 Data Structure Conversion: Tuple -> List -> Append -> Tuple
                    temp_user_list = list(USER_NAMES)
                    temp_user_list.append(new_user)
                    USER_NAMES = tuple(temp_user_list)

                    # 💡 Update parallel mutable passwords list
                    passwords.append(new_pass)
                    print(
                        f"\n\t[SUCCESS] Added new employee '{new_user}' and credential record!\n"
                    )

            elif choice == "0":
                # 📌 Option 0: Returning to Category Selection
                print(
                    f"\n\tExiting {DEPARTMENT} Terminal. Returning to Category selection.\n"
                )
                terminal_running = False

            else:
                print("\n\tYou have made an invalid selection. Please try again.\n")

        except TypeError as e:
            # ⚠️ Gracefully catches TypeError when attempting to modify the immutable tuple
            print(f"\n\t[TYPE ERROR DETECTED] {e}")
            print(
                "\tSystem Immutability Violation: Tuples cannot be modified in-place."
            )
            print(
                "\tPlease email the Help Desk at helpdesk@fakeSchool.edu for credential assistance.\n"
            )

        except ValueError as e:
            # ⚠️ Gracefully catches ValueError for invalid data inputs
            print(f"\n\t[VALUE ERROR DETECTED] {e}")
            print(
                "\tPlease email the Help Desk at helpdesk@fakeSchool.edu for assistance.\n"
            )

        except Exception as e:
            # ⚠️ Handles unexpected errors safely
            print(f"\n\tAn unexpected error occurred: {e}")
            print(
                "\tPlease email the Help Desk at helpdesk@fakeSchool.edu for assistance.\n"
            )
