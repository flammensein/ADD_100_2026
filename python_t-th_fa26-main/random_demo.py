"""
random and string verification
"""

# 📦 import: brings in the random module so we can generate random numbers.
# ℹ️ info: Python's standard library has lots of these built-in modules, we just need to import them to use them.
import random

# 🎲 random.randint(a, b) picks a random whole number, including both a and b.
number = random.randint(0, 100)
while True:
    # ℹ️ info: A while True loop repeats forever until we hit a break statement.
    try:
        # 🧼 cleaning string data: .strip() removes extra spaces, .lower() makes the text lowercase.
        # 💡 tip: input() always returns a string, so we wrap it with int() to convert it to a number.
        # ⚠️ warning: if the user types letters instead of a number, int() will raise a ValueError.
        guess = int(input("Guess a number between 0 and 100:  ").lower().strip())
        if guess == number:
            print("You win!")
            break
        else:
            # 🔥 distance tells us how close the guess was to the secret number.
            distance = abs(number - guess)
            if distance < 10:
                print("Hot")
            elif distance < 20:
                print("Warm")
            else:
                print("Cold")
    except Exception as e:
        # ✅ catching the error here keeps the program from crashing on bad input.
        print(e)
