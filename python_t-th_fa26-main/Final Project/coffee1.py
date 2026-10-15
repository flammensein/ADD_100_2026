"""
☕ Final Project Planning File (STUBS)

This file is intentionally *not finished yet*.
We are using stubs (`pass`) plus comments to plan the program first.

✅ Goal: write the plan in English, then turn each step into Python code later.

"""

# 📌 CONSTANTS
# A constant is a value we do not plan to change while the program runs.
# We use ALL CAPS for constants so they are easy to spot.
MILK = ("Whole", "2%", "Skim", "Oat", "Soy", "Coconut", "None")
ROAST = ("Dark", "Light", "DeCaff")
# ℹ️ info: Tuples are a fixed menu of choices (we do not add/remove options while running).


def get_employee():
    # 🧠 STEP 1: Identify the employee
    # Plan:
    # 1) Ask for the employee number.
    # 2) Look up that employee in storage (ex: a text file).
    # 3) If the employee does not exist, collect info and create a new record.
    #
    # 📁 Data idea (text file):
    # EmployeeNumber, Name, OfficeNumber, Extension
    #
    # ✅ Return value:
    # Return an employee identifier (or an employee record) so the rest of the program
    # knows who is placing the order.
    pass


def get_order(employee_id):
    # 🧠 STEP 2: Get an order for this employee
    # Plan:
    # 1) Check if this employee has prior orders saved.
    # 2) If yes, list the 5 most recent orders (number them 1–5).
    # 3) Ask if they want to repeat an order number.
    # 4) If not repeating, display the menu and collect new choices (milk, roast, size, etc.).
    #
    # ✅ Return value:
    # Return an "order" object (for beginners, this could be a string, tuple, list, or dict).
    pass


def confirm(order, employee):
    # 🧠 STEP 3: Confirm the order details
    # Plan:
    # 1) Display the employee info and order info on screen.
    # 2) Show line numbers so the user can choose what to edit (ex: "1) milk", "2) roast").
    # 3) Ask: "Is this correct? (y/n)"
    # 4) If YES → go to print_label(order, employee).
    # 5) If NO → allow changes, then save any updates.
    #
    # 💾 Saving:
    # If anything changes, update the employee and/or order storage so it is available next time.
    pass


def print_label(order, employee):
    # 🧠 STEP 4: Output (label / receipt)
    # Plan:
    # 1) Create the label text (employee + order details).
    # 2) Print the label to the screen (or to a printer later).
    # 3) Ask if they also want a receipt.
    # 4) Print the receipt if requested.
    pass


def main():
    # ▶️ main() is the "boss" function that runs the steps in order.
    # It collects results from one function and passes them into the next.
    employee = get_employee()
    order = get_order(employee)
    confirm(order, employee)


main()
