"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[✅] 3. Program takes a word or phrase from the user.
[✅] 4. Program loops through characters and prints emojis.
[☣️] 5. A 'try/except' block handles spaces or punctuation. ☣️ I intentionally left this out as the way I felt the code should work would be to handle at least a basic level of punctuation and spaces to be encrypted/decrypted. Doing otherwise to me would be disingenuous and detract from the end fun of having a script that can encode/decode in a fun way and do it smoothly.
-----------------------------------------------------------------------
"""

# ℹ️ Core cipher map for character-to-emoji conversion.
#    Defines the full encryption/decryption key for letters, numbers, punctuation, and spaces.
# 📌 AI PROMPT used to generate list:
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

# ℹ️ Program loop stays active until the user exits.
program_running = True
while program_running:
    try:
        # ℹ️ Main menu for the user selection flow.
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

    # 📌 Case 1: encode plain text into emoji text.
    if encrypt_decrypt == "1":
        # ℹ️ Input is uppercased so it matches the dictionary keys.
        user_secret = input(
            "\n\tTo encrypt, type your secret message below. \n\t(valid characters: A-Z 0-9 punctuation(.,!?'\"-:;()&) and [space]):   "
        ).upper()
        print()
        # ℹ️ Each character is replaced using the mapping in EMOJI_CIPHER.
        encrypted_message = user_secret
        for character, emoji in EMOJI_CIPHER.items():
            encrypted_message = encrypted_message.replace(character, emoji)
        # ℹ️ Encoded output is printed to the console.
        print(f"\n\t{encrypted_message}")
        continue

    # 📌 Case 2: decode emoji text back into normal characters.
    elif encrypt_decrypt == "2":
        # ℹ️ Input here will be read as emoji text to be converted back to readable characters.
        user_secret = input(
            "\n\tTo decrypt, enter your encrypted message below. \n\t(characters outside the scope will be left unchanged):   "
        )
        print()
        # ℹ️ Reversing the mapping to decrypt back to the human readable character set.
        decoded_message = user_secret
        for character, emoji in EMOJI_CIPHER.items():
            decoded_message = decoded_message.replace(emoji, character)
        # ℹ️ Decoded output is printed to the console.
        print(f"\n\t{decoded_message}")
        continue

    # 📌 Case 3: Clean exit path ends the loop and stops the program.
    elif encrypt_decrypt == "3":
        print()
        program_running = False
        break

    else:
        # ⚠️ Invalid options fall through to the input prompt again.
        print("\n\tInvalid entry. Please try again.")
