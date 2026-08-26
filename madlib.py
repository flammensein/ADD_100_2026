"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️ Gather information from the user
pet_type = input("\nPlease enter the species of a pet: ")
the_word_ultra = input('\nPlease type the word "ultra": ')
sports_team = input("\nPlease enter the name of a sports team: ")
fav_sport = input("\nWhat is your favorite sport?: ")
score_num_one = input("\nPlease pick a number: ")
an_adjective = input("\nPlease enter an adjective: ")


# ℹ️ Title of this new literary masterpiece
print(f"\n\n\t\tHey, look! A {an_adjective} Misdirection!!")

# ℹ️ Output a story using the remaining information provided by the user
print(f"\n\n\tThere once was a {pet_type} from Nantucket.")
print(f"\n\tIt was eating some fish from a bucket.")
print(f"\n\tDown on the field, {sports_team} refused to yield.")
print(f"\n\tThe {fav_sport} crowd cheered, what a-ruckus!")
print(f"\n\tAt the end of the game, won by {score_num_one}, that's not lame.")
print(f"\n\tMisdirection the {the_word_ultra} rich gave us.\n\n\n")
