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

# NOTE: We haven't (as far as I can recall) Covered exiting the script/loop/logic intentionally, but
# it's existed in every language I've ever used so I figured I'd try it and it seems to have worked...


# parental_response = "no"
# print(f"\n\tA child has decided to test your last nerve! Begin encounter...\n")
# while parental_response.lower() != "yes":
#     print(f"\n\t\tThe child asks: Are we there yet?")
#     parental_response = input(f"\n\t\tHow do you respond?\t")

# print(
#     f"\n\n\tYou have acquiesced to the child's nagging or arrived at your destination. Good day.\n\n"
# )


for bottle_count in range(99, 0, -1):
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
            exit
    elif bottle_count == 1:
        print(
            f"\n\t{bottle_count} bottle of beer on the wall! {bottle_count} bottle of beer!!"
        )
        print(
            f"\n\tTake it down! Pass it around!! There're no bottles of beer on the wall!!!\n\n"
        )
        exit
