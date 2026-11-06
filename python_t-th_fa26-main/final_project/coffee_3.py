"""
☕ Final Project Menus

"""

# 📌 Week 10 note (design decision):
# We decided to pass around the employee's ID (employee_id), not the whole employee record.
# Next week, when we learn file I/O, we will use employee_id to look up the full employee info from the file.

# 📌 CONSTANTS
# A constant is a value we do not plan to change while the program runs.
# We use ALL CAPS for constants so they are easy to spot.
# 📌 CONSTANTS: these are our "menu options" (fixed choices) for the user to pick from.
MILKS = ("Whole", "2%", "Skim", "Oat", "Soy", "Coconut", "None")
DRINK_TYPE = ("Americano", "Drip", "Latte", "Caffe au Lait", "Matcha", "Tea")
SIZES = ("Large", "Medium", "Small")
FLAVORS = (
    "Caramel",
    "Vanilla",
    "Chocolate",
    "Seasonal",
    "Sugar Free Caramel",
    "Sugar Free Vanilla",
    "None"
)

# ℹ️ info: Tuples are a fixed menu of choices (we do not add/remove options while running).


# ℹ️ info: Python collections (tuples/lists) use 0-based indexes (first item is index 0).
import os

# TODO next class add date time stamp


def clear_screen():
    # 🧠 Job: clear the terminal so the next "screen" looks clean for the user.
    # ℹ️ info: os.system(...) runs a command in your operating system (Windows uses "cls").
    # Assigning to _ silences the system return code (0) in interactive shells
    # this code I looked up on the internet and was answered by AI (gemini)
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_employee():
    # 🧠 STEP 1: Identify the employee
    # Plan:
    # 1) Ask for the employee number.
    # 2) Look up that employee in storage (ex: a text file).
    # 3) If the employee does not exist, collect info and create a new record.
    #
    # 📁 Data idea (text file):
    # EmployeeNumber, Name, OfficeNumber, Extension
    # ⚠️ pitfall: naming a variable `id` hides Python's built-in id() function.
    id = int(input("Please enter your ID number:  "))
    # TODO lookup employee
    f_name = input("Please enter your first name:  ")
    l_name = input("Please enter your last name:  ")
    office_nbr = input("Office to deliver to:  ")
    extension = input("Please enter extension:  ")
    known_allergies = input(
        "Please enter any known food allergies or sensitivities separated by commas:  "
    )
    #
    # ✅ Return value:

    # ✅ Return: a dictionary (dict) so we can keep employee info with NAMEs (keys).
    # 💡 tip: you can access a value by key, like employee_record["office"].
    employee_record = {
        "employee_nbr": id,
        "office": office_nbr,
        "extension": extension,
        "f_name": f_name,
        "l_name": l_name,
        "allergies": known_allergies,
    }

    return employee_record


def get_order(emp_id):
    # 🧠 STEP 2: Collect a drink order
    # Inputs:
    # - emp_id: the employee's ID number (so we can connect the order to a person)
    # ✅ Return: an order (right now we store it as a list)
    # 🧠 STEP 2: Get an order for this employee
    # Plan:
    # 1) Check if this employee has prior orders saved.
    # 2) If yes, list the 5 most recent orders (number them 1–5).
    # 3) Ask if they want to repeat an order number.
    # 4) If not repeating, display the menu and collect new choices (milk, roast, size, etc.).
    #
    clear_screen()
    while True:
        # 🖨️ Display the menu with numbers starting at 1 (friendlier for humans)
        count = 1
        for drink in DRINK_TYPE:
            print(f"{count}.   {drink}")
            count += 1
        try:
            # ⚠️ pitfall: `type` is also the name of a built-in Python function.
            # Using it as a variable works, but can be confusing. (A clearer name: drink_choice)
            type = int(
                input(
                    "Please enter the number for the type of drink you want:  "
                ).strip()
            )
        except ValueError:
            # 🛡️ Error handling: if they type letters instead of a number, int(...) fails.
            # ⚠️ Common bug: use len(DRINK_TYPE), not DRINK_TYPE.len()
            input(
                f"Please enter a number (1-{len(DRINK_TYPE)}). Press Enter to continue..."
            )
            continue
        if type < 1 or type > len(DRINK_TYPE):
            input(
                f"Please enter a number (1-{len(DRINK_TYPE)}). Press Enter to continue..."
            )
            continue
        # ℹ️ info: We subtract 1 because users choose 1..N, but Python indexes are 0..N-1.
        drink = DRINK_TYPE[type - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the size menu
        count = 1
        for size in SIZES:
            print(f"{count}.   {size}")
            count += 1
        try:
            my_size = int(
                input(
                    "Please enter the number for the size of drink you want:  "
                ).strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(SIZES), not SIZES.len()
            input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
            continue
        if my_size < 1 or my_size > len(SIZES):
            input(f"Please enter a number (1-{len(SIZES)}). Press Enter to continue...")
            continue
        size = SIZES[my_size - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the milk menu
        count = 1
        for milk in MILKS:
            print(f"{count}.   {milk}")
            count += 1
        try:
            my_milk = int(
                input("Please enter the number for the milk you want:  ").strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(MILKS), not MILKS.len()
            input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
            continue
        if my_milk < 1 or my_milk > len(MILKS):
            input(f"Please enter a number (1-{len(MILKS)}). Press Enter to continue...")
            continue
        milk = MILKS[my_milk - 1]
        break

    clear_screen()
    while True:
        # 🖨️ Display the flavor menu
        count = 1
        for flavor in FLAVORS:
            print(f"{count}.   {flavor}")
            count += 1
        try:
            my_flavor = int(
                input("Please enter the number for the flavor you want:  ").strip()
            )
        except ValueError:
            # ⚠️ Common bug: use len(FLAVORS), not FLAVORS.len()
            input(
                f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
            )
            continue
        if my_flavor < 1 or my_flavor > len(FLAVORS):
            input(
                f"Please enter a number (1-{len(FLAVORS)}). Press Enter to continue..."
            )
            continue
        flavor = FLAVORS[my_flavor - 1]
        break

    while True:
        try:
            # 🧠 Ask for the number of flavor pumps (extra flavor shots)
            pumps = int(
                input(
                    "Please enter the number of pumps you want (ten cents each):  "
                ).strip()
            )
            if pumps < 0:
                print("Pumps cannot be negative. ")
                continue
            if pumps > 10:
                print("Ten is the maximum number of pumps. ")
                continue
        except ValueError:
            # 🛡️ If they type something that is not a number, don't crash—ask again.
            input(f"Please enter a number (0-10). Press Enter to continue...")
            continue
        break

    # ℹ️ info: This order is stored as a list. Each position has a meaning:
    # order[0]=emp_id, order[1]=drink, order[2]=size, order[3]=milk, order[4]=flavor, order[5]=pumps
    order = [emp_id, drink, size, milk, flavor, pumps]

    return order


def confirm_order(order):
    # 🧠 STEP 3: Confirm an order (show it back to the user and allow edits)
    # ✅ Return: the updated order list
    while True:
        clear_screen()
        count = 1
        # 🖨️ Display the order with numbers starting at 1 (easier for people to choose a line to edit)
        for item in order:
            print(f"{count}.  {item}")
            count += 1
        try:
            correct = input("Is everything correct (Y/N)").strip().upper()
            if correct == "Y":
                return order
            if correct != "N":
                input("Please enter Y or N. Press Enter to continue...")
                continue

            change = int(input("Please enter the number you want to change:  ").strip())
        except ValueError:
            # ⚠️ Common bug: lists don't have .length(); the Python way is len(order)
            input(f"Please enter a number (1-{len(order)}). Press Enter to continue...")
            continue

        try:
            if change < 1 or change > len(order):
                input(
                    f"Please enter a number (1-{len(order)}). Press Enter to continue..."
                )
                continue
            # ℹ️ info: change is 1-based for the user, so we use change-1 for the list index.
            new_value = input(f"Please enter the new value for {order[change-1]}")
            order[change - 1] = new_value
            # 💡 tip: We use `continue` (loop again) instead of calling confirm_order(order) again.
            # That keeps the logic in one loop and avoids recursion.
            continue
        except Exception as e:
            print(f"{e}\nThat was not a valid entry. Try again")
            input("Press Enter to continue...")
            continue


def confirm_employee(employee_record):
    # 🧠 STEP 1b: Confirm employee info (print the record, let the user fix mistakes)
    # ✅ Return: the (possibly updated) employee_record dictionary
    while True:
        clear_screen()
        # confirm employee record
        # NOTE: This is an f-string. The string itself uses double quotes: f"..."
        # Inside the { ... } part we also need quotes for dict keys. If we used double quotes
        # again (employee_record["office"]), Python would think the f-string ended early.
        # Using single quotes for the dict keys avoids that quote-conflict.
        print(f"1.  Employee Number:  {employee_record['employee_nbr']}")
        print(f"2.  Office Number:  {employee_record['office']}")
        print(f"3.  Extension:  {employee_record['extension']}")
        print(f"4.  First Name:  {employee_record['f_name']}")
        print(f"5.  Last Name:  {employee_record['l_name']}")
        print(f"6.  Allergies: {employee_record['allergies']}")
        # 3) Ask: "Is this correct? (y/n)"
        correct = input("Is this correct? (Y/N) ").strip().upper()
        if correct == "Y":
            break
        if correct != "N":
            input("Please enter Y or N. Press Enter to continue...")
            continue

        try:
            change = int(input("What number would you like to change? ").strip())
        except ValueError:
            input("Please enter a number (1-6). Press Enter to continue...")
            continue

        # ⚠️ Important concept:
        # `employee_record` is the dictionary we want to update.
        # If you want the change to "stick", you must assign into the dict (example):
        # employee_record["office"] = input("New office number: ").strip()
        match change:
            case 1:
                while True:
                    try:
                        employee_nbr = int(input("New employee number: ").strip())
                        employee_record["employee_nbr"] = employee_nbr
                        break
                    except ValueError:
                        print("Employee number must be a whole number.")
            case 2:
                employee_record["office"] = input("New office number: ").strip()
            case 3:
                employee_record["extension"] = input("New extension: ").strip()
            case 4:
                employee_record["f_name"] = input("New first name: ").strip()
            case 5:
                employee_record["l_name"] = input("New last name: ").strip()
            case 6:
                employee_record["allergies"] = input("New allergies: ").strip()
            case _:
                input("Please choose a number 1-6. Press Enter to continue...")

    # 4) If YES → go to print_label(order, employee).
    # 5) If NO → allow changes, then save any updates.
    #
    # 💾 Saving:
    # If anything changes, update the employee and/or order storage so it is available next time.

    return employee_record


def print_label(order, employee):
    # 🧠 STEP 4: Output a label / receipt for the order
    # 🖨️ Output: this function is where you format what prints to the screen.
    # 🧠 STEP 4: Output (label / receipt)
    # Plan:
    # 1) Create the label text (employee + order details).
    # 2) Print the label to the screen (or to a printer later).
    # ℹ️ If `employee` is a dictionary, looping over it gives you the KEYS.
    # We use each key to print both the key and the value.
    for key in employee:
        print(f"{key}: {employee[key]}")
    for item in order:
        print(item)
    # 3) Ask if they also want a receipt.
    # 4) Print the receipt if requested.
    pass


def main():
    # ▶️ Entry point: main() runs the program "top to bottom" in order.
    # ▶️ main() is the "boss" function that runs the steps in order.
    # It collects results from one function and passes them into the next.
    clear_screen()
    # 🧠 Get the employee record first
    # emp_record is a dictionary
    emp_record = get_employee()
    # ℹ️ Grab the employee number out of the dictionary using its key
    emp_id = emp_record["employee_nbr"]
    # NOTE on scope/mutability:
    # When we pass a dictionary into a function, the function can see and edit the SAME dictionary object.
    # Returning it and re-assigning (emp_record = confirm_employee(emp_record)) is not required for scope;
    # we do it here to make the logic/readability clear ("this function may update the record").
    emp_record = confirm_employee(emp_record)
    # ✅ We pass the employee ID (an int) into get_order so the order can be tied to a person.
    order = get_order(emp_id)
    order = confirm_order(order)


# ▶️ Start the program by calling main().
main()
