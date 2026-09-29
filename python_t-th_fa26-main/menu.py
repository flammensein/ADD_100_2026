"""
using menus and validation
practice for crud:
🏗️  Create
📖  Read
🔃  Update
🗑️  Delete

"""

# 🧠 This file shows a simple menu program.
# A menu is a way to let the user choose what the program should do.
# We will use a loop so the menu keeps appearing until the user exits.

# 🔁 while True means: keep repeating forever until we decide to stop.
while True:
    # 🧭 The menu is displayed each time the loop runs.
    print("1.  Create contact")
    print("2.  Find and display contact")
    print("3.  Update contact")
    print("4.  Delete contact")
    print("5.  Exit")

    # 🛡️ try/except is used to catch errors before the program crashes.
    # The program tries to convert the user's input into an integer.
    # If the user enters something like "hello", Python raises a ValueError.
    try:
        choice = int(input("Please enter the NUMBER of your choice:  "))

    # ⚠️ except ValueError handles the specific error for non-numeric input.
    # This is a beginner-friendly way to say: "please try again instead of crashing."
    except ValueError:
        print("Enter a numeric value, please!   🔢 ")
        # 🔄 continue sends the program back to the top of the loop.
        continue

    # 🧭 match/case is a cleaner version of if/elif/else for multiple choices.
    # It checks the value in choice and runs the matching case.
    match choice:
        case 1:
            print("Create Contact 🏗️")
            # ✅ continue makes the loop start over and show the menu again.
            continue
        case 2:
            print("Find and display contact 📖")
            continue
        case 3:
            print("Update contact 🔃")
            continue
        case 4:
            print("Delete contact 🗑️")
            continue
        case 5:
            # 🏁 break stops the while loop.
            print("Goodbye! 👋")
            break
        case _:
            # 🧩 case _ acts like the default option in an if/else chain.
            # It handles any choice that is not one of the menu options.
            print("That is not a valid menu choice. Please try again. ⚠️")
            continue

# ✅ This message prints when the loop ends.
print("Logic done ✅")
