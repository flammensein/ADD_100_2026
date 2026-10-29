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

# needed for the clear_screen() function
import os
import subprocess

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# ✅ 1. Define get_price(size)
def get_price(size):
    """Evaluates size string and returns price as a float, or 0.0 if invalid."""
    if size.lower() == "small":
        return 3.00
    elif size.lower() == "medium":
        return 4.00
    elif size.lower() == "large":
        return 5.00
    else:
        # ⚠️ Returns 0.0 as a result of an invalid size selection
        print("\n\tSorry, but that was not a valid size choice.")
        return 0.0


# ✅ 2. Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    clear_screen()
    """Prints a formatted summary showing size, base, customer-friendly fruit, and scoops."""
    # Issue 2 Fix: Customer-friendly string rather than raw Python list representation
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
    # Loops until user selects a valid base (1-4), cancels (5), or triggers EOF
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
    while more_fruit:
        clear_screen()
        try:
            print("\n\t1. Strawberry")
            print("\t2. Banana")
            print("\t3. Mango")
            print("\t4. Blueberry")
            print("\t5. done with fruit selection(s)")
            fruit_selected = int(
                input(
                    "\n\tEnter your fruit choice (1-4, 5 to finish; auto-finishes at 4): "
                )
            )
            if fruit_selected == 5:
                # Issue 4 Fix: Enforce at least one fruit selection
                if not selected_fruits:
                    print(
                        "\n\tPlease select at least one fruit before finishing your smoothie."
                    )
                    continue
                break
            elif 1 <= fruit_selected <= 4:
                fruit = FRUITS[fruit_selected - 1]
                if fruit in selected_fruits:
                    print(f"\t{fruit} has already been selected.")
                    continue
                selected_fruits.append(fruit)
                print(f"\tSelected: {selected_fruits}")
                if len(selected_fruits) == 4:
                    break
            else:
                print("\n\tINVALID SELECTION - Please try again.")
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        # Issue 1 Fix: Signal cancellation on EOF
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            return None
        # Issue 5 Fix: Removed broad 'except Exception' to avoid masking logic bugs
    return selected_fruits


def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True, check=True)
    blender_banner()


def blender_banner():
    banner_border = "=" * 38
    shop_name = "THE DAILY BLEND-der SMOOTHIE BAR"
    print(
        f"\n\t{banner_border}\n"
        f"\t{shop_name.center(len(banner_border))}\n"
        f"\t{banner_border}\n"
    )


# ✅ 3. Define main() to collect inputs, validate scoops, and call functions
def main():
    clear_screen()
    total_cost = 0.0
    size = ""

    # Size selection loop
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

    # Base selection
    base = base_selection()
    if not base:
        print("\n\tSmoothie order canceled.")
        return

    # Fruit selection
    fruit = fruit_selection()
    # Issue 1 Fix: Order canceled if fruit selection hit EOF
    if fruit is None:
        print("\n\tSmoothie order canceled.")
        return

    # Scoop selection with try/except integer resilience & fallback
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

    # Issue 3: Scoops passed to blend; total_cost is size-based per assignment specs
    blend(size, base, fruit, scoops)

    # Final bill
    print(f"\n\t-----------------------------")
    print(f"\tTOTAL DUE: ${total_cost:.2f}")
    print(f"\t-----------------------------\n")


main()
