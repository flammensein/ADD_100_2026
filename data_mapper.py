"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[✅] 3. Program takes a word or phrase from the user.
[✅] 4. Program loops through characters and prints emojis.
[ ] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

# AI PROMPT:
# Generate a list to use as a cipher. Below is  provided an example for A, B, and C.
# Finish the alphabet and punctuation, including " ", following this example I provided.
EMOJI_CIPHER = {
    "A": "🍎",
    "B": "🍌",
    "C": "🐱",
    "D": "🐶",
    "E": "🐘",
    "F": "🐸",
    "G": "🦒",
    "H": "🏠",
    "I": "🍦",
    "J": "🪼",
    "K": "🔑",
    "L": "🦁",
    "M": "🌙",
    "N": "🌃",
    "O": "🐙",
    "P": "🐧",
    "Q": "👑",
    "R": "🌹",
    "S": "☀️",
    "T": "🌳",
    "U": "☂️",
    "V": "🎻",
    "W": "🐳",
    "X": "❌",
    "Y": "🪀",
    "Z": "🦓",
    "0": "🥚",
    "1": "☝️",
    "2": "✌️",
    "3": "🍀",
    "4": "🐈",
    "5": "⭐",
    "6": "🐝",
    "7": "🌈",
    "8": "🕷️",
    "9": "🪐",
    ".": "🔴",
    ",": "🟠",
    "!": "❗",
    "?": "❓",
    "'": "📝",
    '"': "💬",
    "-": "➖",
    ":": "🕒",
    ";": "🤔",
    "(": "⬅️",
    ")": "➡️",
    "&": "🤝",
    " ": " ",
}


program_running = True
# Keeps the program running until a choice by the user sets program_running to False
while program_running:
    try:
        print(
            "\n\t1...Encode a message written with the Latin Alphabet(E.G. the one this text is typed with)"
        )
        print("\t2...Decode a message written in Emojis into the Latin Alphabet. ")
        print("\t3...End your Cryptographic Joy Time")
        encrypt_decrypt = input(
            f"\n\tEnter your choice from above (1,2,3) to have fun with encryption and decryption:   "
        )
    except ValueError:
        print("\n\tInvalid entry. Please try again.")
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")

    if encrypt_decrypt == "1":
        user_secret = input(
            "\n\tTo encrypt, type your secret message below. \n\t(valid characters: A-Z 0-9 punctuation(.,!?'\"-:;()&) and [space]):   "
        ).upper()
        print()
        encrypted_message = user_secret
        for character, emoji in EMOJI_CIPHER.items():
            encrypted_message = encrypted_message.replace(character, emoji)
        print(f"\n\t{encrypted_message}")
        continue

    elif encrypt_decrypt == "2":
        user_secret = input(
            "\n\tTo decrypt, enter your encrypted message below. \n\t(characters outside the scope will be left unchanged):   "
        )
        print()
        decoded_message = user_secret
        for character, emoji in EMOJI_CIPHER.items():
            decoded_message = decoded_message.replace(emoji, character)
        print(f"\n\t{decoded_message}")
        continue

    elif encrypt_decrypt == "3":
        print()
        program_running = False
        break

    else:
        print("\n\tInvalid entry. Please try again.")
