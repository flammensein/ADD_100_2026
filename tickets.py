"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[✅] 1. Create a list of 20 seats (numbered 1-20).
[✅] 2. Display the list of available seats.
[✅] 3. Ask user for a seat number (0 to quit).
[✅] 4. Remove the selected seat from the list.
[✅] 5. Handle invalid inputs (seat taken or doesn't exist).
[✅] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# ℹ️ Build the list of available seats using only valid seat numbers 1 through 20.
# 💡 Starting with 1 keeps 0 outside the seat list so it can act as the quit option.
seats = list(range(1, 21))
option_pick = 1

# ✅ Print the welcome banner for the cinema.
print(f"\n\tWelcome to Flammen's Micro Cinema!")

# 🔁 Keep running until the user quits or every seat is sold out.
while option_pick != 0:
    # ⚠️ If there are no seats left, end the program gracefully.
    if len(seats) == 0:
        print(f"\n\tThere are no more seats available!")
        print(f"\n\tPlease visit us another day!")
        break

    # 📌 Display the remaining available seats.
    print(f"\n\tHere are the seats currently available:")
    print(f"\n")

    for chair in seats:
        print(f"\t\t{chair}")

    print(f"\n\tEnter '0' to QUIT")
    print(f"\n")

    # ℹ️ Ask the user to choose a seat number.
    try:
        option_pick = int(
            input(f"\n\tPlease pick an available seat from the list above:   ")
        )
    except ValueError:
        # ⚠️ Handle non-numeric input cleanly.
        print(f"\n\tThat seat is either unavailable or invalid.")
        print(f"\tPLEASE MAKE A VALID SELECTION.\n")
        continue
    except Exception as e:
        # ⚠️ Catch unexpected errors and keep the program running safely.
        print(f"\n\tAn unexpected error occurred: {e}")
        continue

    # ⚠️ Exit the loop immediately when the user enters 0.
    if option_pick == 0:
        break

    # ✅ Reserve the selected seat if it is still available.
    elif option_pick in seats:
        print(f"\n\tYou are reserving seat {option_pick}, enjoy the show!")
        seats.remove(option_pick)

    else:
        # ⚠️ Tell the user the seat is invalid or already taken.
        print(f"\n\tThat seat is either unavailable or invalid.")
        print(f"\tPLEASE MAKE A VALID SELECTION.\n")

# ✅ Final exit message after the user quits or all seats are sold.
print(f"\n\tThank you for visiting Flammen's Micro Cinema!")
print(f"\n\tEnjoy the show...if that's your thing...we're not the boss of you...")
