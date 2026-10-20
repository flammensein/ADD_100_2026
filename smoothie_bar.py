"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)
def get_price(size):
    if size.lower() == "small":
        return 3.00
    elif  size.lower() == "medium":
        return 4.00
    elif size.lower() == "large":
        return 5.00
    else:
        # ⚠️ returns 0 as a result of an invalid size selection
        print("\n\tSorry, but that was not a valid size choice.")
        return 0

# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print(f"\n\tPreparing Smoothie:\n\t  Size: {size} \n\t  Base: {base} \n\t  Fruit: {fruit} \n\t  Scoops: {scoops}")
    

# TODO: Define main() to collect input and call your logic
def main():
    


main()