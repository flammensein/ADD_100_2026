"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# ✅TODO: Create a tuple of at least 8 responses
THE_ORACLE_SAYS = (
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
)

mystical_query = ""

print(f"\n\t{'~' * 43}")
print(
    "\t\u2014\u2014\u2014 Welcome \u2014 to the Desert of the Real \u2014\u2014\u2014"
)
print(f"\t{'~' * 43}")

# ✅TODO: Create a while loop that keeps asking questions
# Loops until the user enters "quit" as their query
while True:
    print(f'\tEnter "Quit" to let the Oracle rest.')
    the_ultimate_question = input(f"\n\tWhat is it you wish to know?   ")

    # ✅TODO: Use random.choice(RESPONSES) to answer
    the_perfect_answer = random.choice(THE_ORACLE_SAYS)
    print(f"\n\t{the_perfect_answer}")

    # TODO: If user types "quit", break the loop
    if str(the_ultimate_question).lower == "quit":
        break

print(f"\n\tThe Oracle fades into the mists until called upon once again...")
input(f"\n\tPress 'ENTER' to exit the mists before you, too, fade away...")
