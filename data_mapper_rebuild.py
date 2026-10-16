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

# Core cipher map for character-to-emoji conversion.
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

# Manually build the reverse cipher using a standard for loop to comply with course rules.
REVERSE_EMOJI_CIPHER = {}
for character, emoji in EMOJI_CIPHER.items():
    REVERSE_EMOJI_CIPHER[emoji] = character

# Program loop stays active until the user exits.
program_running = True
while program_running:
    try:
        print("\n\t1...Encode a message written with the Latin Alphabet")
        print("\t2...Decode a message written in Emojis into the Latin Alphabet")
        print("\t3...End your Cryptographic Joy Time")
        encrypt_decrypt = input("\n\tEnter your choice (1, 2, 3): ")

        if encrypt_decrypt == "1":
            user_secret = input(
                "\n\tTo encrypt, type your secret message below:\n\t"
            ).upper()
            encrypted_message_list = []

            # Iterate through characters and append to our new list
            for char in user_secret:
                try:
                    encrypted_message_list.append(EMOJI_CIPHER[char])
                except KeyError:
                    # Graceful recovery: append the unmapped character as-is
                    encrypted_message_list.append(char)

            encrypted_message = "".join(encrypted_message_list)
            print(f"\n\t{encrypted_message}")

        elif encrypt_decrypt == "2":
            user_secret = input(
                "\n\tTo decrypt, enter your encrypted message below:\n\t"
            )
            decrypted_message_list = []

            # Iterate through emojis and append mapped characters to our new list
            for char in user_secret:
                try:
                    decrypted_message_list.append(REVERSE_EMOJI_CIPHER[char])
                except KeyError:
                    # Graceful recovery: append the unmapped character as-is
                    decrypted_message_list.append(char)

            decrypted_message = "".join(decrypted_message_list)
            print(f"\n\t{decrypted_message}")

        elif encrypt_decrypt == "3":
            print("\n\tExiting program...\n")
            program_running = False

        else:
            print("\n\tInvalid entry. Please try again.")

    # Catches EOF Errors which are generated if user presses keyboard shortcuts while at the prompt.
    except EOFError:
        print(f"\n\tNo more input available. Exiting program...\n\n")
        break
    except Exception as e:
        print(f"\n\tAn unexpected error occurred: {e}")
