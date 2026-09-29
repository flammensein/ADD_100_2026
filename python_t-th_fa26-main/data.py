"""
Data Types in Python

ℹ️ info: In Python, a data type defines the category of value a variable holds, determining what operations can be performed on it.
"""

# 🧵 Strings
# ℹ️ info: Strings (type `str`) represent a sequence of text characters. They are always enclosed in quotes: single ('Hello') or double ("Hello").
string_1 = "1"
string_2 = "2"

# ⚠️ warning: Adding two strings together performs string "concatenation" (joining them together), not mathematical addition!
# 💡tip: Here, string_1 + string_2 outputs "12", not 3.
print(string_1 + string_2)


# 🔢numbers
# ℹ️ info: Python has two main numeric types: integers (`int`) for whole numbers, and floating-point numbers (`float`) for decimals.
integer = 40

# ⚠️ warning: Avoid naming your variables using Python's built-in function/type names.
# Here, naming the variable `float` is valid Python but overrides the built-in function `float()`. This is called "shadowing" and is a very common source of bugs!
float = 0.2

# ℹ️ info: Mathematical operations between variables of the same physical type (`int` + `int`) yield that type.
print(integer + integer)

# 💡tip: If you perform arithmetic between an `int` and a `float`, Python automatically converts (coerces) the final result to a `float`.
print(integer + float)

# 💡tip: You can use "type casting" (conversion functions) to convert one type to another.
# Here, `int(string_1)` converts the string "1" into the integer 1, enabling mathematical addition with `integer` (Result: 41).
print(int(string_1) + integer)

# 👻 BOOlean
# ℹ️ info: Booleans (type `bool`) store logical truth values: either `True` or `False`.
# ⚠️ warning: Python is strictly case-sensitive! You must capitalize `True` and `False`. Using lowercase `true` or `false` will produce a `NameError`.
tired = True
have_coffee = False

print(have_coffee)

# 💡tip: Booleans are most frequently used in combination with control flow (like `if` statements) to run code conditionally.
if tired:
    print("Drink Coffee")
