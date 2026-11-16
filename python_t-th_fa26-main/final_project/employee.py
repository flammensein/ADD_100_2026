import os
import datetime


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def lookup_employee(id):
    employees = {}
    try:
        with open("final_project\\employee.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":{", 1)
                emp_id = parts_of_line[0].strip().strip("}")
                detail = parts_of_line[1].strip().strip("}")
                employees[emp_id] = detail
                if emp_id == id:
                    return True
                else:
                    continue

    except FileNotFoundError:
        print(f'File does not exist. I will create for you! It will be "employee.txt"')
        return False
    except IndexError:
        return False
    except Exception as e:
        right_now = datetime.datetime.now()
        error_log_path = os.path.join("final_project\\error_log.txt")
        with open(error_log_path, "a") as f:
            f.write(f"{right_now}, {e}\n")
        print(e)


def get_employee():
    id = input("Please enter your ID number:  ")
    found = lookup_employee(id)
    print(found)
    if found:
        return id
    else:
        f_name = input("Please enter your first name:  ")
        l_name = input("Please enter your last name:  ")
        office_nbr = input("Office to deliver to:  ")
        extension = input("Please enter extension:  ")
        known_allergies = input(
            "Please enter any known food allergies or sensitivities separated by commas:  "
        )

        employee_record = {
            "office": office_nbr,
            "extension": extension,
            "f_name": f_name,
            "l_name": l_name,
            "allergies": known_allergies,
        }

        with open("final_project\\employee.txt", "a") as f:
            f.write(f"{id}:{employee_record}\n")

        return id


def confirm_employee(id):

    # TODO  - read file into employee_record

    # while True:
    #     clear_screen()
    #     print(f"1.  Employee Number:  {employee_record['employee_nbr']}")
    #     print(f"2.  Office Number:  {employee_record['office']}")
    #     print(f"3.  Extension:  {employee_record['extension']}")
    #     print(f"4.  First Name:  {employee_record['f_name']}")
    #     print(f"5.  Last Name:  {employee_record['l_name']}")
    #     print(f"6.  Allergies: {employee_record['allergies']}")
    #     # 3) Ask: "Is this correct? (y/n)"
    # correct = input("Is this correct? (Y/N) ").strip().upper()
    # if correct == "Y":
    #     break
    # if correct != "N":
    #     input("Please enter Y or N. Press Enter to continue...")
    #     continue

    # try:
    #     change = int(input("What number would you like to change? ").strip())
    # except ValueError:
    #     input("Please enter a number (1-6). Press Enter to continue...")
    #     continue

    # # ⚠️ Important concept:
    # `employee_record` is the dictionary we want to update.
    # If you want the change to "stick", you must assign into the dict (example):
    # employee_record["office"] = input("New office number: ").strip()
    #     match change:
    #         case 1:
    #             while True:
    #                 try:
    #                     employee_nbr = int(input("New employee number: ").strip())
    #                     employee_record["employee_nbr"] = employee_nbr
    #                     break
    #                 except ValueError:
    #                     print("Employee number must be a whole number.")
    #         case 2:
    #             employee_record["office"] = input("New office number: ").strip()
    #         case 3:
    #             employee_record["extension"] = input("New extension: ").strip()
    #         case 4:
    #             employee_record["f_name"] = input("New first name: ").strip()
    #         case 5:
    #             employee_record["l_name"] = input("New last name: ").strip()
    #         case 6:
    #             employee_record["allergies"] = input("New allergies: ").strip()
    #         case _:
    #             input("Please choose a number 1-6. Press Enter to continue...")

    # # 4) If YES → go to print_label(order, employee).
    # # 5) If NO → allow changes, then save any updates.
    # #
    # 💾 Saving:
    # If anything changes, update the employee and/or order storage so it is available next time.

    return
