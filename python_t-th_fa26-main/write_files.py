"""
writing to files

"""

# 📝 This script creates a simple "menu" text file that lists sandwich specials by day.
# 💡 When you "write to a file", Python saves text to a file on your computer (like Notepad).

# 🛠 Setup: we import `datetime` so we can stamp the file with today's date.
import datetime

# 📝 We capture the current date/time one time when the program starts.
# 💡 That way, every line in the file uses the same timestamp (instead of changing mid-run).
right_now = datetime.datetime.now()


def header():
    # 👣 Step 1: Open (or create) `menu.txt` in "write" mode.
    # 📌 Important: mode `"w"` OVERWRITES the file each time you run the program.
    # 🧠 Why it works: `with open(...) as f:` creates a "file handle" named `f`,
    # and Python automatically closes the file when the `with` block ends.
    with open("menu.txt", "w") as f:
        # 👣 Step 2: Write the first lines of the file.
        # 📝 `\n` means "new line" (pressing Enter).
        f.write("-----------Specials----------\n")
        # 💡 Tip: `strftime` formatting can be used inside an f-string.
        # This prints like: "October 27, 2026"
        f.write(f"Current as of {right_now:%B %#d, %Y}\n\n")  # Windows


def main():
    header()

    # 🧾 Data "table": a dictionary maps each day (key) to a sandwich special (value).
    # 💡 Tip: Dictionaries are great when you want "look up this thing by name".
    sandwich_specials = {
        "Monday": "Turkey Club",
        "Tuesday": "Tuna Melt",
        "Wednesday": "Italian Sub",
        "Thursday": "BBQ Chicken Sandwich",
        "Friday": "Philly Cheesesteak",
        "Saturday": "BLT",
        "Sunday": "Grilled Cheese",
    }

    # 👣 Step 3: Re-open the same file in "append" mode to add more lines.
    # 📌 Important: mode `"a"` ADDS to the end of the file (it does not erase it).
    with open("menu.txt", "a") as f:
        # 👣 Step 4: Loop through the dictionary and write one line per day.
        # 🧠 Why it works: `.items()` gives us both the key and value each time.
        for day, sandwich in sandwich_specials.items():
            f.write(f"{day}:       {sandwich}\n")

    # 📝 This is just a message in the terminal so you know where to look.
    print("your file is saved in menu.txt")


main()
