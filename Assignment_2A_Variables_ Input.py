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

# ℹ️ Gather information from the user
pet_type = input("\nEnter the species of a pet: ")
the_word_ultra = input("\nType the word 'ultra': ")
sports_team = input("\nEnter the name of a sports team: ")
fav_sport = input("\nWhat is your favorite sport?: ")
score_num_one = input("\nPick a number: ")
fish_descriptor = input("\nEnter an adjective: ")

# ℹ️ Build a story using the aforementioned information provided by the user
print(
    f"\n\n\n\tThere once was a {pet_type} from Nantucket eating {fish_descriptor} fish from some buckets."
)
print(f"\n\tDown on the field, {sports_team} refused to yield.")
print(f"\n\tThe {fav_sport} crowd cheered, what a-ruckus!")
print(f"\n\tAt the end of the game, won by {score_num_one}, that's not lame.")
print(f"\n\tA distraction the {the_word_ultra} rich gave us.\n\n\n")
