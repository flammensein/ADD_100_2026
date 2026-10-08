"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

"""
Prompt used to generate the NATO_ALPHABET:
    Finish this list for the variable "NATO_ALPHABET" including all of the letters, 
    numbers, and punctuation as listed on the wiki page here: 
    https://en.wikipedia.org/wiki/NATO_phonetic_alphabet#Letters
    Use the "Code Word" columns for the translated values of all 3 types. Be sure 
    to include an entry for " " that is just " " on both sides.
"""
NATO_ALPHABET = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    ".": "stop",
    ",": "comma",
    "-": "hyphen",
    "/": "slant",
    "(": "brackets on",
    ")": "brackets off",
    ":": "colon",
    ";": "semi-colon",
    "!": "exclamation mark",
    "?": "question mark",
    "'": "apostrophe",
    '"': "quote",
    " ": " ",
}

word = input("Enter word to spell: ").upper()

# TODO: Loop through each character
# TODO: try to print the NATO code, except if character is missing
