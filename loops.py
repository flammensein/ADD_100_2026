"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# 📌 Task 1: Continue prompting until the response matches the sentinel value.
# 💡 Called .lower() to make the comparison case-insensitive, so "YES" and "yes"
#    follow the same path without requiring the user to enter a specific case.
# ℹ️ I've used "exit" in various languages in the past so I assumed it existed in
#    python as well and it seems to work well here for me.
parental_response = "no"
print(f"\n\tA child has decided to test your last nerve! Begin encounter...\n")
while parental_response.lower() != "yes":
    print(f"\n\t\tThe child asks: Are we there yet?")
    parental_response = input(f"\n\t\tHow do you respond?\t")

print(
    f"\n\n\tYou have acquiesced to the child's nagging or arrived at your destination. Good day.\n\n"
)

# 📌 Task 2: range starts at 99, stops before 0, and decrements by 1 so each
#    verse is processed from 99 down through 1.
for bottle_count in range(99, 0, -1):
    # 💡 Keep the plural and singular wording separate so the output remains
    #    grammatically correct as the count changes.
    if bottle_count > 1:
        print(
            f"\n\t{bottle_count} bottles of beer on the wall! {bottle_count} bottles of beer!!"
        )
        if (bottle_count - 1) == 1:
            print(
                f"\n\tTake one down! Pass it around! {bottle_count - 1} bottle of beer on the wall!!"
            )
        elif (bottle_count - 1) > 1:
            print(
                f"\n\tTake one down! Pass it around! {bottle_count - 1} bottles of beer on the wall!!"
            )
        else:
            print(f"\n\tThere's something wrong with your wall...where's da beers?\n\n")
            exit()
    elif bottle_count == 1:
        print(
            f"\n\t{bottle_count} bottle of beer on the wall! {bottle_count} bottle of beer!!"
        )
        print(
            f"\n\tTake it down! Pass it around!! There're no bottles of beer on the wall!!!\n\n"
        )
        exit()
