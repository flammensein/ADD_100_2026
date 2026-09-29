"""
validation demos
"""

# psychology definition from Dictionary.com:
# the act of affirming a person, or their ideas, feelings, or actions, as acceptable and worthy.


# print("You are a great programmer!")
# print("You are as funny as you think you are!!🤣😂😅")
# print("And gosh darn it, people like you!")


# programming definition also from Dictionary.com:
# the act of confirming something as true or correct.
# translation: "please don't make the program explode."


# validate input good, bad, ugly!!!

# ℹ️ info: A while loop is a repeating structure. It keeps running as long as a condition is true.
# ⚠️ warning: In this example, the loop continues until the user enters a name that is not empty.
# 💡tip: This is input validation. We are checking whether the input is acceptable before moving on.
name = ""
while not name:
    name = input("Please enter your name:  ").strip()
    # ℹ️ info: Input is cleaned with .strip() before validation so extra spaces do not count as a value.
    # 💡tip: We can also format the first letter of the name with .capitalize() to make it look cleaner.
    name = name.capitalize()
print(f"Hello, {name}")

# ℹ️ info: A try/except block helps us catch errors without crashing the whole program.
# ⚠️ warning: If the user enters a non-number, Python raises a ValueError when we try to convert it to an int.
# 💡tip: The except block is basically a polite "please try that again" for the program.
try:
    age = -1
    # ℹ️ info: This while loop validates the age range. We keep asking until the age is between 0 and 100.
    # ⚠️ warning: If the user enters an invalid value, the condition is still true and the loop repeats.
    while age < 0 or age > 100:
        age = int(input("How old are you?  "))

        if age > 100:
            print("Wow, you look awesome.")
            print("I think there might be a typo, you can't really be")
            print("That old! 😲")
        elif age > 16:
            print("We will generate a parking permit.")
except ValueError:
    print("I'm sorry, that was not a valid integer")
except Exception as e:
    print(e)
