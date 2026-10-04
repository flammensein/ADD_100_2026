"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. RESPONSES is a tuple containing at least 8 string options.
[✅] 3. Program uses a 'while True' loop to keep the game running.
[✅] 4. random.choice() selects the answer from the tuple.
[✅] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# Create a tuple of possible responses for the 'Oracle' to give.
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

print(f"\n\t{'~' * 43}")
print(
    "\t\u2014\u2014\u2014 Welcome \u2014 to the Desert of the Real \u2014\u2014\u2014"
)
print(f"\t{'~' * 43}")

print(f"\n\tCAUTION!!! The future is mysterious! For clarity, ask yes/no questions.")

# Loops until the user enters "quit" as their query
while True:
    try:
        print(f'\n\n\tEnter "Quit" to let the Oracle rest.\n')
        the_ultimate_question = input(f"\n\tWhat is it you wish to know?   ").lower()
    except ValueError:
        print("\n\tInvalid entry. Please try again.")
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")

    # If user types "quit", break the loop
    if the_ultimate_question == "quit":
        break
    else:
        # Use random.choice(RESPONSES) to answer
        the_perfect_answer = random.choice(THE_ORACLE_SAYS)
        print(f"\n\t{the_perfect_answer}\n")
        continue

print(f"\n\tThe Oracle fades into the mists until called upon once again...")
input(f"\n\tPress 'ENTER' to exit the mists before you, too, fade away...\n")
