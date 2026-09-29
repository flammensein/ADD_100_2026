"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(0, 21))
option_pick = 1

print(f"\n\tWelcome to Flammen's Micro Cinema!")

while option_pick != 0:
    if len(seats) == 1:
        print(f"\n\tThere are no more seats available!")
        print(f"\n\tPlease visit us another day!")

    print(f"\n\tHere are the seats currently available:")
    print(f"\n")
    for chair in seats:
        if chair == 0:
            print(f"\tEnter '0' to QUIT")
        else:
            print(f"\t\t{chair}")

    print(f"\n")
    option_pick = int(
        input(f"\n\tPlease pick an available seat from the list above:   ")
    )
    if option_pick == 0:
        break
    elif option_pick in seats:
        print(f"\n\tYou are reserving seat {option_pick}, enjoy the show!")
        seats.remove(option_pick)
    else:
        print(f"\n\tThat seat is either unavailable or invalid.")
        print(f"\tPLEASE MAKE A VALID SELECTION.\n")

print(f"\n\tThank you for visiting Flammen's Micro Cinema!")
print(f"\n\tEnjoy the show...if that's your thing...we're not the boss of you...")
