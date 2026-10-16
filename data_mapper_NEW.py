"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[✅] 1. Header Docstring included.
[✅] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[✅] 3. Program takes a word or phrase from the user.
[✅] 4. Program loops through characters and prints emojis.
[✅] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

# ℹ️ Core cipher map for character-to-emoji conversion.
#    Defines the full encryption/decryption key for letters, numbers, punctuation, and spaces.
# 📌 AI PROMPT used to generate list:
# Generate a list to use as a cipher. Below is provided an example for A, B, and C.
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

# ℹ️ Build the reverse cipher dictionary for decoding emojis back into text.
#    Why/How: Some emojis (like ☀️ or ☂️) include an invisible Unicode variation selector (\ufe0f),
#    making them 2 characters long in Python. Stripping "\ufe0f" with .replace() ensures every
#    emoji key is a single character so our character-by-character for-loop works cleanly.
#    Reference: https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)
REVERSE_EMOJI_CIPHER = {}
for character, emoji in EMOJI_CIPHER.items():
    emoji = emoji.replace("\ufe0f", "")
    REVERSE_EMOJI_CIPHER[emoji] = character

# ℹ️ Program loop stays active until the user chooses option 3 to exit.
program_running = True
while program_running:
    try:
        # ℹ️ Main menu for the user selection flow.
        print("\n\t1...Encode a message written with the Latin Alphabet")
        print("\t2...Decode a message written in Emojis into the Latin Alphabet")
        print("\t3...End your Cryptographic Joy Time")
        encrypt_decrypt = input("\n\tEnter your choice (1, 2, 3): ")

        # 📌 Case 1: Encode plain text into emoji text.
        if encrypt_decrypt == "1":
            # ℹ️ Input is uppercased so it matches the uppercase dictionary keys.
            user_secret = input(
                "\n\tTo encrypt, type your secret message below:\n\t"
            ).upper()
            encrypted_message_list = []

            # ℹ️ Perform character substitution across cipher mappings while preserving unsupported characters.
            for char in user_secret:
                try:
                    encrypted_message_list.append(EMOJI_CIPHER[char])
                except KeyError:
                    # Graceful recovery: keep unmapped symbols/characters unchanged.
                    encrypted_message_list.append(char)

            encrypted_message = "".join(encrypted_message_list)
            print(f"\n\t{encrypted_message}")

        # 📌 Case 2: Decode emojis back into normal characters.
        elif encrypt_decrypt == "2":
            # ℹ️ Strip invisible "\ufe0f" variation selectors from pasted emojis so each emoji is 1 character.
            user_secret = input(
                "\n\tTo decrypt, enter your encrypted message below:\n\t"
            ).replace("\ufe0f", "")
            decrypted_message_list = []

            # ℹ️ Perform character substitution across reverse cipher mappings while preserving unsupported characters.
            for char in user_secret:
                try:
                    decrypted_message_list.append(REVERSE_EMOJI_CIPHER[char])
                except KeyError:
                    # Graceful recovery: keep unmapped characters/emojis unchanged.
                    decrypted_message_list.append(char)

            decrypted_message = "".join(decrypted_message_list)
            print(f"\n\t{decrypted_message}")

        # 📌 Case 3: Clean exit path sets state flag to False to stop the loop.
        elif encrypt_decrypt == "3":
            print("\n\tExiting program...\n")
            program_running = False

        else:
            # ⚠️ Invalid menu options prompt the user to try again.
            print("\n\tInvalid entry. Please try again.")

    # ℹ️ Catches EOF Errors if the user presses keyboard exit shortcuts at the input prompt.
    except EOFError:
        print("\n\tInput cut short...Alas poor user, I barely knew thee...\n\n")
        break
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")
