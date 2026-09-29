"""
A list by any other name?

Python flavors: list - mutable, tuple - immutable

Lists are similar to arrays in other languages, but Python lists can grow
or shrink as needed.
"""

# I owe, I owe, so off to work I go!
# ℹ️ info: Lists use square brackets. They are mutable, which means their contents can change.
# ℹ️ info: Tuples use parentheses. They are immutable, which means their contents cannot change.
dwarves = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]

# 💡tip: A list can contain strings, numbers, or other kinds of values.
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# The following example uses a list in a loop to process each month.
# It is commented out because it requires user input.
# total = 0

# for month in months:
#     try:
#         miles = float(input(f"How many miles did you drive in {month}? "))
#         total += miles
#     except Exception as e:
#         print("That was invalid. Please enter a number (0.0) ")
#         continue
# average = total / 12
# print(f"The average number of miles driven each month was:  {average:,.1f}")


# ℹ️ info: A for loop visits each item in a list in order.
for dwarf in dwarves:
    print(dwarf)

# ℹ️ info: List indexes start at 0, so index 2 refers to the third item.
print(dwarves[2])

# ⚠️ warning: Assignment does not copy a list. Both variables refer to the same list.
guest_list = dwarves

guest_list.append("Snarky")
print(dwarves)

# 💡tip: Use a slice to make a shallow copy of a list.
guest_list = dwarves[:]

# This change affects guest_list, but not dwarves.
guest_list.append("Sarcastic")
print(f"Guest list: {guest_list}")
print(f"dwarves: {dwarves}")

# ℹ️ info: The in operator checks whether a value is in a list.
if "Sleepy" in dwarves:
    print("Yaawwn!")

# ℹ️ info: sort changes the list. reverse=True sorts from largest to smallest.
guest_list.sort(reverse=True)
print(guest_list)

# 💡tip: Slicing returns a section of a list. The ending index is not included.
special_guest = guest_list[2:4]
print(special_guest)

# ℹ️ info: Negative indexes count from the end of a list.
print(guest_list[-1])

guest_list.insert(0, "Annoying")
print(guest_list)

# ℹ️ info: index returns the position of the first matching item.
print(dwarves.index("Sleepy"))

# ℹ️ info: remove deletes the first matching item by value.
guest_list.remove("Dopey")
print(guest_list)

# ℹ️ info: pop removes and returns an item by index. Here, it removes the first item.
guest_list.pop(0)
print(guest_list)

# ℹ️ info: len returns the number of items in a list.
print(len(guest_list))
