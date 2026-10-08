"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[✅] 3. Program takes a word or phrase from the user.
[ ] 4. Program loops through characters and prints emojis.
[ ] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

# import random

# # AI PROMPT:
# # Generate a list to use as a cipher. Below is  provided an example for A, B, and C.
# # Finish the alphabet and punctuation, including " ", following this example I provided.
# EMOJI_CIPHER = {
#     "A": "🍎",
#     "B": "🍌",
#     "C": "🐱",
#     "D": "🐶",
#     "E": "🐘",
#     "F": "🐸",
#     "G": "🦒",
#     "H": "🏠",
#     "I": "🍦",
#     "J": "🪼",
#     "K": "🔑",
#     "L": "🦁",
#     "M": "🌙",
#     "N": "🌃",
#     "O": "🐙",
#     "P": "🐧",
#     "Q": "👑",
#     "R": "🌈",
#     "S": "☀️",
#     "T": "🌳",
#     "U": "☂️",
#     "V": "🎻",
#     "W": "🐳",
#     "X": "❌",
#     "Y": "🪀",
#     "Z": "🦓",
#     "0": "🥚",
#     "1": "☝️",
#     "2": "✌️",
#     "3": "🍀",
#     "4": "🐈",
#     "5": "⭐",
#     "6": "🐝",
#     "7": "🌈",
#     "8": "🕷️",
#     "9": "🪐",
#     ".": "🔴",
#     ",": "🟠",
#     "!": "❗",
#     "?": "❓",
#     "'": "📝",
#     '"': "💬",
#     "-": "➖",
#     ":": "🕒",
#     ";": "🤔",
#     "(": "⬅️",
#     ")": "➡️",
#     "&": "🤝",
#     " ": " ",
# }

un_message = input(
    "\n\tEnter your secret message below (valid characters: A-Z 0-9 punctuation(.,!?'\"-:;()&) and [space]):\n\t   "
).upper()


# # TODO: Loop through each character
# # TODO: try to print the emoji, except if it's a space or symbol
