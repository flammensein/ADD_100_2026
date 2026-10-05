"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[✅] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[✅] 4. Task 3: Validation (isdigit check) completed.
[✅] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
print(f"\n\t{instrument} is {len(instrument)} characters long.")
print("\n")
print(f"\n\tThe first letter of {instrument} is {instrument[:1]}")
print(f"\n\tThe last letter of {instrument} is {instrument[-1:]}")
print("\n")
print(f"\n\tThe lowest ASCII Character in {instrument} is '{min(instrument)}'.")
print(f"\n\tThe highest ASCII Character in {instrument} is '{max(instrument)}'.")
print("\n")


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
print(f"\n\tThe input, '{messy_input}' needs cleaned up.")
print(f"\t...processing typos...ziffing sockets...regretting nothing...")
print(
    f"\tThe input has been cleaned up, I hope you're proud of yourself (I am). \n\tHere it is: {messy_input.strip().upper().replace("_"," ")}"
)
print("\n")

# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
if serial_number.isdigit():
    the_truth_is_out_there = " Valid Serial"
else:
    the_truth_is_out_there = "n Invalid Serial"
print(f"\n\t{serial_number} is a{the_truth_is_out_there}.")
print("\n")


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
name_string = "DUCKY"
duck_letters = list(name_string)
quacks = 0

print("\n\t--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)
    print(f"\n\tThere was a teacher who had a duck,\n\t and Ducky was its Name-O!")
    print(f"\n\t{current_name}\n" * 3)
    print("\t...and Ducky was his Name-o!\n")
    duck_letters[int(quacks)] = "🦆"
    quacks += 1

# The FINAL DUCKY!!
current_name = " ".join(duck_letters)
print(f"\n\tThere was a teacher who had a duck,\n\t and Ducky was its Name-O!")
print(f"\n\t{current_name} \n" * 3)
print("\t...and Ducky was his Name-o!\n\n")
