"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Global Constants BASES and FRUITS defined as Tuples.
[✅] 3. Professional function get_price(size) returns a float.
[✅] 4. Professional function blend(size, base, fruit, price) for output.
[🚧] 5. main() function handles try/except for price (int).
[🚧] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    if size.lower() == "small":
        return 3.00
    elif size.lower() == "medium":
        return 4.00
    elif size.lower() == "large":
        return 5.00
    else:
        # ⚠️ returns 0 as a result of an invalid size selection
        print("\n\tSorry, but that was not a valid size choice.")
        return 0


# TODO: Define blend(size, base, fruit, price)
def blend(size, base, fruit, price):
    print(
        f"\n\tPreparing Smoothie:\n\t  Size: {size} \n\t  Base: {base} \n\t  Fruit: {fruit} \n\t  Price: ${price:.2f}"
    )


def base_selection():
    while True:
        try:
            # ℹ️ Main menu for the user selection flow.
            print("\n\t1. Water")
            print("\t2. Apple Juice")
            print("\t3. Orange Juice")
            print("\t4. Milk")
            base_selected = int(input("\n\tEnter your base choice (1-4): "))
            if base_selected < 1 or base_selected > 4:
                print("\n\tINVALID SELECTION - Please try again.")
                continue
            return BASES[base_selected - 1]
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            return ""


def fruit_selection():
    selected_fruits = []
    more_fruit = True
    while more_fruit:
        try:
            # ℹ️ Main menu for the user selection flow.
            print("\n\t1. Strawberry")
            print("\t2. Banana")
            print("\t3. Mango")
            print("\t4. Blueberry")
            fruit_selected = int(
                input("\n\tEnter your fruit choice (1-4, enter 0 if finished): ")
            )
            if fruit_selected == 0:
                # User has indicated all desired fruit has been selected. Return to main()
                break
            elif fruit_selected > 4 or fruit_selected < 1:
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_fruits.append(FRUITS[fruit_selected - 1])
        except ValueError:
            print("\n\tINVALID SELECTION - Please try again.")
        # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
        except EOFError:
            print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
            break
        except Exception as e:
            print(f"\n\tAn unexpected error occurred: {e}")
    return selected_fruits


# TODO: Define main() to collect input and call your logic
# 🚧 Work in progress
def main():
    size = 0
    while size == 0:
        size = input(
            f"\n\tPlease enter your desired smoothie size (Small, Medium, Large):   "
        )
        price = get_price(size)

    base = base_selection()
    fruit = fruit_selection()

    blend(size, base, fruit, price)


main()
