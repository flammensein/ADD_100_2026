"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB ✨
-----------------------------------------------------------------------
[✅] 1. Header docstring included and styled for the assignment.
[✅] 2. Task 1: String basics — length, indexing, and ASCII patterns. 🎸
[✅] 3. Task 2: The Cleanup Crew — trim, normalize, and tidy messy text. 🧹
[✅] 4. Task 3: Validation check — confirm whether the serial number is numeric. 🔢
[✅] 5. Task 4: The Duck Loop — rebuild the name and reveal it with emoji flair. 🦆
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
# 📝 Annotation: This section introduces the core idea that strings are ordered collections of characters.
# We measure the total length, isolate the first and last characters, and compare values by ASCII order
# to find the smallest and largest character in the text. 🎯
instrument = "Acoustic Guitar"
print(f"\n\t{instrument} is {len(instrument)} characters long.")
print("\n")
print(f"\n\tThe first letter of {instrument} is {instrument[:1]}")
print(f"\n\tThe last letter of {instrument} is {instrument[-1:]}")
print("\n")
print(f"\n\tThe lowest ASCII Character in {instrument} is '{min(instrument)}'.")
print(f"\n\tThe highest ASCII Character in {instrument} is '{max(instrument)}'.")
print("\n")


# --- TASK 2: THE CLEANUP CREW 🧹 ---
# 📝 Annotation: This step shows how text can be cleaned and standardized before it is used.
# strip() removes stray spaces, upper() makes all letters consistent, and replace() converts formatting markers
# like underscores into readable spaces. 🧹✨
messy_input = "   vOLUME_knob_11   "
print(f"\n\tThe input, '{messy_input}' needs cleaned up.")
print(f"\t...processing typos...ziffing sockets...regretting nothing...")
print(
    f"\tThe input has been cleaned up, I hope you're proud of yourself (I am). \n\tHere it is: {messy_input.strip().upper().replace('_', ' ')}"
)
print("\n")

# --- TASK 3: THE VALIDATOR 🔍 ---
# 📝 Annotation: This validation step checks whether the value is made entirely of digits.
# The isdigit() method is useful when we only want numeric input, because letters or symbols should fail the check.
serial_number = "90210"
if serial_number.isdigit():
    the_truth_is_out_there = " Valid Serial"
else:
    the_truth_is_out_there = "n Invalid Serial"
print(f"\n\t{serial_number} is a{the_truth_is_out_there}.")
print("\n")


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# 📝 Annotation: This loop demonstrates that strings are immutable in Python.
# Instead of changing the original text directly, we convert the string into a list, update each character one at a time,
# and then rejoin the pieces to create the final duck-themed version. 🦆✨
name_string = "DUCKY"
duck_letters = list(name_string)
quacks = 0

print("\n\t--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)
    print(f"\n\tThere was a teacher who had a duck,\n\t and Ducky was its Name-O!")
    print(f"\n\t{current_name}\n" * 3)
    print("\t...and Ducky was his Name-o!\n")
    duck_letters[quacks] = "🦆"
    quacks += 1

# The FINAL DUCKY!! 🧩
# This final chorus prints the completed duck name after every letter has been swapped over.
# The code is intentionally repetitive to make the silly sing-along effect feel like a final encore.
current_name = " ".join(duck_letters)
print(f"\n\tThere was a teacher who had a duck,\n\t and Ducky was its Name-O!")
print(f"\n\t{current_name} \n" * 3)
print("\t...and Ducky was his Name-o!\n\n")
