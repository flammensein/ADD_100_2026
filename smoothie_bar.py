"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Global Constants BASES and FRUITS defined as Tuples.
[✅] 3. Professional function get_price(size) returns a float.
[✅] 4. Professional function blend(size, base, fruit, scoops) for output.
[✅] 5. main() function handles try/except for scoops (int) with fallback.
[✅] 6. main() calls both functions correctly and prints the final bill.
-----------------------------------------------------------------------
"""

# ℹ️ These standard-library modules support the platform-specific screen clear.
# I got this idea from researching how to make the "deprecated" warning go away:
#       sources:
#               - PROMPT:Pylance is giving me a soft deprecation notice about os.system() in my clear screen function. Show me sources for the recommended way to do this instead.
#               - https://docs.python.org/3/library/subprocess.html
#               - https://docs.python.org/3/library/os.html#os.system
import os
import subprocess

# 📌 Fixed menu options; tuples keep the available choices in a stable order.
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# 📌 Map the selected size to its fixed price.
def get_price(size):
    """Evaluates size string and returns price as a float, or 0.0 if invalid."""
    # 💡 Lowercasing allows size names in any letter case.
    if size.lower() == "small":
        return 3.00
    elif size.lower() == "medium":
        return 4.00
    elif size.lower() == "large":
        return 5.00
    else:
        # ⚠️ main() treats 0.0 as invalid and prompts for another size.
        print("\n\tSorry, but that was not a valid size choice.")
        return 0.0


# 📌 Present the completed order in a customer-friendly format.
def blend(size, base, fruit, scoops):
    clear_screen()
    """Prints a formatted summary showing size, base, customer-friendly fruit, and scoops."""
    # 💡 Join fruit names into readable text instead of displaying the raw list.
    #    The join processes each selected name once: O(n) time and output space.
    fruit_display = ", ".join(fruit) if fruit else "None (Base Only)"

    print(
        f"\n\tPreparing Smoothie:\n"
        f"\t  Size:   {size.title()}\n"
        f"\t  Base:   {base}\n"
        f"\t  Fruit:  {fruit_display}\n"
        f"\t  Scoops: {scoops}"
    )


def base_selection():
    """Prompts user to select a smoothie base or cancel."""
    # 📌 Repeat until a valid menu choice is made, the user cancels, or input ends.
    while True:
        clear_screen()
        try:
            print("\n\t1. Water")
            print("\t2. Apple Juice")
            print("\t3. Orange Juice")
            print("\t4. Milk")
            print("\t5. Exit Base Selection")
            base_selected = int(
                input("\n\tEnter your base choice (1-4, 5 to cancel): ")
            )
            if base_selected == 5:
                print("\n\tYou have canceled base selection. Exiting the base menu.")
                return ""
            elif 1 <= base_selected <= 4:
                # 💡 Menu choices start at 1, while tuple indexes start at 0.
                return BASES[base_selected - 1]
            else:
                print("\n\tINVALID SELECTION - Please try again.")
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            return ""


def fruit_selection():
    """Collect up to four distinct fruits, or finish early with choice 5."""
    selected_fruits = []
    more_fruit = True
    # 📌 Collect unique choices until the user finishes or selects all four fruits.
    # 💡 Duplicate checks scan at most four items (constant bounded work per choice).
    while more_fruit:
        clear_screen()
        try:
            if selected_fruits:
                print(f"\n\tCurrently selected: {', '.join(selected_fruits)}")
            print("\n\t1. Strawberry")
            print("\t2. Banana")
            print("\t3. Mango")
            print("\t4. Blueberry")
            print("\t5. done with fruit selection(s)")
            fruit_selected = int(
                input(
                    "\n\tEnter your fruit choice (1-4 above; max of 4 choices allowed): "
                )
            )
            if fruit_selected == 5:
                # ⚠️ The user must choose a fruit before finishing this menu.
                if not selected_fruits:
                    print(
                        "\n\tPlease select at least one fruit before finishing your smoothie."
                    )
                    continue
                break
            elif 1 <= fruit_selected and fruit_selected <= 4:
                # 💡 Convert the one-based menu number to a zero-based tuple index.
                fruit = FRUITS[fruit_selected - 1]
                if fruit in selected_fruits:
                    input(
                        f"\t{fruit} has already been selected. Press ENTER to try again."
                    )
                    continue
                selected_fruits.append(fruit)
                if len(selected_fruits) == 4:
                    break
            else:
                input("\n\tINVALID SELECTION - PRESS ENTER TO RETRY")
        except ValueError:
            input("\n\tINVALID SELECTION - PRESS ENTER TO RETRY")
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            # ⚠️ None signals interrupted input to main(), which cancels the order.
            return None
    return selected_fruits


def clear_screen():
    # ℹ️ Select the terminal command based on the operating system.
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True, check=True)
    blender_banner()


def blender_banner():
    # 💡 Use the border width to center the shop name consistently.
    banner_border = "=" * 38
    shop_name = "THE DAILY BLEND-der SMOOTHIE BAR"
    print(
        f"\n\t{banner_border}\n"
        f"\t{shop_name.center(len(banner_border))}\n"
        f"\t{banner_border}\n"
    )


# 📌 Coordinate input, order validation, summary display, and billing.
def main():
    clear_screen()
    total_cost = 0.0
    size = ""

    # 📌 A zero price indicates an invalid size, so keep prompting.
    while total_cost == 0.0:
        try:
            size = input(
                "\n\tPlease enter your desired smoothie size (Small, Medium, Large):   "
            ).strip()
            if size:
                total_cost = get_price(size)
            else:
                print("\tYou must select a valid size.")
                continue
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            return

    # 📌 An empty string from base_selection() means the order was canceled.
    base = base_selection()
    if not base:
        print("\n\tSmoothie order canceled.")
        return

    # 📌 None from fruit_selection() means input ended before selection completed.
    fruit = fruit_selection()
    if fruit is None:
        print("\n\tSmoothie order canceled.")
        return

    # ⚠️ Invalid, negative, or interrupted scoop input falls back to zero.
    try:
        scoops = int(input("\n\tHow many protein/booster scoops would you like?: "))
        if scoops < 0:
            print("\tNegative scoops not allowed. Defaulting to 0 scoops.")
            scoops = 0
    except ValueError:
        print("\n\tInvalid number of scoops entered. Defaulting to 0 scoops.")
        scoops = 0
    except EOFError:
        print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
        scoops = 0

    # 📌 Scoops appear in the summary; the assignment prices by size only.
    blend(size, base, fruit, scoops)

    # 🖨️ Display the size-based total with two digits after the decimal point.
    print(f"\n\t-----------------------------")
    print(f"\tTOTAL DUE: ${total_cost:.2f}")
    print(f"\t-----------------------------\n")


# ▶️ Start the interactive program.
main()
