"""
Dictionaries
"""

# ℹ️ info: A dictionary stores matching key-value pairs.
# Here, the number is the key and the Japanese word is its value.
import random  # Used below to shuffle the quiz questions.

number_names_japanese = {
    1: "ichi",
    2: "nee",
    3: "son",
    4: "shi",
    5: "go",
    6: "roku",
    7: "shichi",
    8: "hachi",
    9: "ku",
    10: "ju",
}

# 💡 tip: .items() gives each key and value as a pair.
# list() makes those pairs into a list that can be shuffled.
questions = list(number_names_japanese.items())
# ℹ️ info: shuffle changes the order of the list in place.
random.shuffle(questions)

# Keep track of how many answers are right and wrong.
right = 0
wrong = 0

# ℹ️ info: This loop visits each shuffled number-word pair.
for key, value in questions:
    # 💡 tip: key is the number; value is the Japanese word.
    try:
        # input() gives text, so int() converts the response to a number.
        answer = int(input(f"Please enter the numeric value for {value}:"))
    except Exception as e:
        # If the response cannot be converted to an integer, show the error
        # and move on to the next question.
        print(e)
        continue

    # Compare the student's answer with the correct number (the key).
    if answer == key:
        right += 1
    else:
        wrong += 1

# ℹ️ info: An f-string puts variable values inside the message.
print(f"You got {right} right and {wrong} wrong")

# Divide correct answers by the number of questions to get the score.
score = right / 10
print(f"Your score is {score:,.1f}")

# ℹ️ info: Use a key to look up its value in the dictionary.
print(f"{number_names_japanese.get(1)}")

# ℹ️ info: To look up a key from a value, visit the pairs and compare values.
for key, value in number_names_japanese.items():
    if value == "ichi":
        print(key)
