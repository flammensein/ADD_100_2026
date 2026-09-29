"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# 🎉 Madlibs program
# This project lets the user enter words and then creates a silly sentence.

# 📝 Step 1: get input from the user and save it in variables.
print("\t\t\t\tMadlibs - Mary had a Little Lamb\n\n")
name = input("Enter a person's name: ")
animal = input("Enter a kind of animal: ")
color = input("Enter a color: ")

# 💡 Tip: input() always returns a string, even if the user types numbers.
# ⚠️ Warning: if you want math, convert with int() or float().

# 🖨️ Step 2: display the story using f-strings.
print(f"\n\n{name} had a little {animal}")
print(f"Whose fleece was {color} as snow")
print(f"And everywhere that {name} went")
print(f"The {animal} was sure to go")

# ✅ This is a good example of combining user input and formatted output.
# 💡 The \n escape creates a new line, and \t adds a tab space.
