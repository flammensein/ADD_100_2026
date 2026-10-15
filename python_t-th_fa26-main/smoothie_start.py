"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, price) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# 🥤 These tuples are the menu of choices. A tuple is an ordered collection
# that this program should treat as fixed (not add to or remove from).
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# 💰 TODO: Complete the price function described in the assignment checklist.
# `size` is the user's chosen size; compare it without worrying about letter case.
def price(size):
    if size.lower() == "small":
        return 3.00
    elif size.lower() == "medium":
        return 5.00
    elif size.lower() == "large":
        return 7.00
    else:
        # ⚠️ An unknown size is not a valid order, so report it and return 0.
        print("Sorry, that was not a valid choice")
        return 0


# 🧪 TODO: Define blend(size, base, fruit, price).
# It should use the order details and price to print a description of the smoothie.


# 🧭 TODO: Finish main() so it asks for the customer's choices, then calls
# the functions above. Local variables such as size and base must be set first.
def main():
    # These calls are a starting outline; define the values and functions first.
    price = get_price(size)
    blend(size, base, fruit, price)


# ▶️ Run the program by calling main().
main()
