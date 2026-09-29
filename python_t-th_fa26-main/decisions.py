# 🧠 DECISION MAKING IN PYTHON
# Use if and else statements to make choices in a program.
# Comparisons help Python decide what to do next.

age = 18

if age >= 18:
    print("✅ You are an adult.")
else:
    print("🧒 You are under 18.")

# 💡 Tip: == checks if two values are equal.
# 💡 Tip: != means "not equal".
# 💡 Tip: >, <, >=, and <= are comparison operators.
# ⚠️ Warning: do not confuse = with ==.
# = assigns a value, while == compares two values.

# Example with user input
name = input("Enter your name: ")
if name == "Sam":
    print(f"Hello, {name}! You are the instructor!")
else:
    print(f"Hello, {name}! Welcome to Python.")
