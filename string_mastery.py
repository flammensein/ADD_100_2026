"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
# TODO: Print the length of 'instrument'
# TODO: Print the first and last letter of 'instrument'
# TODO: Use min() and max() to find and print the lowest and highest ASCII characters


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
# TODO: Use .strip() to remove spaces
# TODO: Use .upper() to capitalize everything
# TODO: Use .replace() to swap the underscores "_" for spaces " "


# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
# TODO: Use .isdigit() to check validity.
# Print "Valid Serial" if it is numeric, or "Invalid Serial" if it isn't.


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")

# TODO: Create a loop that iterates through name_string (for char in name_string)
# TODO: Inside the loop:
#       1. Use " ".join(duck_letters) to create a variable named 'current_name'
#       2. Print: "There was a teacher who had a duck and Ducky was his Name-o"
#       3. Print the line f"({current_name}) \n" multiplied by 3
#       4. Print "and Ducky was his Name-o!\n"
#       5. Replace the letter in duck_letters at index [count] with "🦆"
#       6. Increment count by 1

# TODO: After the loop, print the "Finale" (the final version with all 🦆 emojis)
# Hint: You'll need one more .join() and one more print block here!
