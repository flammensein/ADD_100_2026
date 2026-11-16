"""
☕ Final Project Menus

"""

import employee
import order
import datetime
import os

# 📌 Week 11 note (design decision):
# split into multiple files


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


# will read in
def print_label(emp_order, employee_id):

    right_now = datetime.datetime.now()
    # formatted by ai
    formatted_now = (
        right_now.strftime("%B ")
        + str(right_now.day)
        + right_now.strftime(", %Y ")
        + right_now.strftime("%I").lstrip("0")
        + right_now.strftime("%p").lower()
    )
    print(formatted_now)
    for key in employee_id:
        print(f"{key}: {employee_id[key]}")
    for item in emp_order:
        print(item)
    # 3) Ask if they also want a receipt.
    # 4) Print the receipt if requested.


def main():

    clear_screen()
    id = employee.get_employee()
    employee.confirm_employee(id)
    order.get_order(id)
    order.confirm_order()


# ▶️ Start the program by calling main().
main()
