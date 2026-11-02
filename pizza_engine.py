"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[✅] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[✅] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

import os
import subprocess
import random

# The Global Pantry
TOPPINGS = ("Mushrooms", "Italian Sausage", "Green Peppers", "Pineapple")

# Default Global Variables
# 💡 Use the border width to center the shop name consistently.
banner_border = "=" * 38
shop_name = "Flammen Hot Pizzeria"
SIZE_OPTIONS = ["s", "m", "l"]


def clear_screen():
    # ℹ️ Select the terminal command based on the operating system.
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True, check=True)
    pizza_pie_banner()


def pizza_pie_banner():
    print(
        f"\n\t{banner_border}\n"
        f"\t{shop_name.center(len(banner_border))}\n"
        f"\t{banner_border}\n"
    )


# def pizza_pie_size(size):
#     pass


def make_pizza(customer, size, toppings, is_delivery=False):

    if size[0].lower() == "s":
        cost_of_a_meal = 9.00
    elif size[0].lower() == "m":
        cost_of_a_meal = 13.00
    elif size[0].lower() == "l":
        cost_of_a_meal = 17.00
    else:
        # ⚠️ main() treats 0.0 as invalid and prompts for another size.
        print("\n\tSorry, but that was not a valid size choice.")

    toppings_display = ", ".join(toppings) if toppings else "Cheese Only (No Toppings)"

    order_id = f"PZ-{random.randint(9000, 9999)}"
    print(f"\n\tOrder #: {order_id}")
    print(f"\tCustomer: {customer}")
    print(f"\tDine-In: {is_delivery}")
    print(f"\tSize: {size}")
    print(f"\tTotal:  ${cost_of_a_meal:.2f}")
    print(f"\tToppings: {toppings_display}")

    return


def customer_info(is_delivery=False):
    """Prompts user for customer contact and delivery address details.
    :return: dict, structured collection of customer contact and address data
    """
    address = "CARRYOUT"
    banner_border = "=" * 38
    banner_title = "CUSTOMER INFORMATION"
    print(
        f"\n\t{banner_border}\n"
        f"\t{banner_title.center(len(banner_border))}\n"
        f"\t{banner_border}\n"
    )

    try:
        # ℹ️ Collect first name and ensure it is not left empty
        first_name = ""
        while not first_name:
            first_name = input("\tPlease enter your first name: ").strip().capitalize()
            if not first_name:
                print("\tFirst name cannot be blank. Please try again.\n")

        # ℹ️ Collect last name and normalize capitalization
        last_name = ""
        while not last_name:
            last_name = input("\tPlease enter your last name: ").strip().capitalize()
            if not last_name:
                print("\tLast name cannot be blank. Please try again.\n")

        # 💡 Validate 10-digit phone number using digit-checking and length bounds
        phone = ""
        while not phone:
            phone_input = input("\tPlease enter your 10-digit phone number: ").strip()
            # 🛡️ Strip formatting characters like hyphens or parentheses if entered
            cleaned_phone = (
                phone_input.replace("-", "")
                .replace("(", "")
                .replace(")", "")
                .replace(" ", "")
            )

            if len(cleaned_phone) == 10 and cleaned_phone.isdigit():
                phone = cleaned_phone
            else:
                print("\tInvalid phone number. Must be exactly 10 numeric digits.\n")

        # ℹ️ Collect street address for delivery handoff
        if is_delivery == True:
            address = ""
            while not address:
                address = input("\tPlease enter your delivery street address: ").strip()
                if not address:
                    print("\tAddress cannot be blank. Please try again.\n")

        # ✅ Package user details into a dictionary structure
        full_name = f"{first_name} {last_name}"
        return {
            "customer": full_name,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "address": address,
        }

    # ⚠️ Catch keyboard exit signal gracefully to prevent crash loops
    except EOFError:
        print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
        return None


def main():
    selected_toppings = []
    topping_selected = ""
    pie_size = ""
    is_delivery = ""

    clear_screen()
    # TO-DO add a welcoming statement to start the ordering process
    while is_delivery == "":
        its_not_digiorno = (
            input(f"\n\tIs this order for delivery? (y/n): ").strip().lower()
        )
        if its_not_digiorno == "":
            is_delivery = ""
            input(f"\n\tYou have entered an invalid option. PRESS ENTER TO RETRY.")
            continue
        elif its_not_digiorno[0] == "y":
            is_delivery = True
        elif its_not_digiorno[0] == "n":
            is_delivery = False
        else:
            is_delivery = ""
            input(f"\n\tYou have entered an invalid option. PRESS ENTER TO RETRY.")
            continue

    info = customer_info(is_delivery)

    while not pie_size:
        try:
            selected_size = (
                input(
                    "\n\tWhat size pizza would you like to order? (Small, Medium, Large):   "
                )
                .strip()
                .lower()
            )
            if selected_size == "":
                input("\tYou must select a size. PRESS ENTER TO RETRY")
                continue
            elif selected_size[0] not in SIZE_OPTIONS:
                input("\tYou must select a valid size. PRESS ENTER TO RETRY")
                continue
            else:
                pie_size = selected_size.capitalize()
        except Exception as e:
            print(f"\n\tAn unexpected error occurred: {e}")
            input("\n\tPRESS ENTER TO MOVE ON")
            continue

    try:
        print("\n")
        # ℹ️ Main menu for the user selection flow.
        for topping in TOPPINGS:
            print(f"\t{TOPPINGS.index(topping)+1} --- {topping}")
        while len(selected_toppings) < len(TOPPINGS) and topping_selected != 0:
            topping_selected = int(
                input("\n\tEnter your toppings choice (1-4, enter 0 if finished): ")
            )
            if topping_selected == 0:
                break
            elif topping_selected > len(TOPPINGS) or topping_selected < 0:
                input("\n\tINVALID SELECTION - PRESS ENTER TO RETRY")
            else:
                selected_toppings.append(TOPPINGS[topping_selected - 1])
                print(f"\tCurrently Selected Toppings: {selected_toppings}")
    except ValueError:
        input("\n\tINVALID SELECTION - PRESS ENTER TO RETRY")
    # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
    except EOFError:
        print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
        # break
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")
        input("\n\tPRESS ENTER TO MOVE ON")

    print(f"\n\tSelected_Toppings: {selected_toppings}\n")
    make_pizza(
        customer=info["customer"],
        size=pie_size,
        toppings=selected_toppings,
        is_delivery=is_delivery,
    )


main()
