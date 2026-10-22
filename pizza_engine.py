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

# The Global Pantry
TOPPINGS = ("Pepperoni", "Mushrooms", "Italian Sausage", "Green Peppers", "Pineapple")

# Default Global Variables


def make_pizza(customer, size, toppings, is_delivery):
    is_delivery = False
    # return


def main():
    selected_toppings = []
    topping_selected = ""
    more_toppings = True
    # while more_toppings:
    try:
        print("\n")
        # ℹ️ Main menu for the user selection flow.
        for topping in TOPPINGS:
            print(f"\t{TOPPINGS.index(topping)+1} --- {topping}")
        while len(selected_toppings) <= len(TOPPINGS) and topping_selected != 0:
            topping_selected = int(
                input("\n\tEnter your toppings choice (1-4, enter 0 if finished): ")
            )
            print(f"\nBefore adding the selection to the list/order")
            print(f"Topping_Selected: {topping_selected}")
            if topping_selected >= len(TOPPINGS) or topping_selected < 0:
                print("\n\tINVALID SELECTION - Please try again.")
            else:
                selected_toppings.append(TOPPINGS[topping_selected - 1])
                print(f"\nAfter adding the selection to the list/order")
                print(f"Topping_Selected: {topping_selected}")
    except ValueError:
        print("\n\tINVALID SELECTION - Please try again.")
        # break
    # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
    except EOFError:
        print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
        # break
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")
        # break
        # return selected_toppings
    # print(f"\nLast Topping_Selected: {topping_selected}")
    print(f"Selected_Toppings: {selected_toppings}\n")
    pass


main()
