"""
fun with functions

"""

# 📌 A constant is a value we plan not to change while the program runs.
CONSTANT = "constant"
# 🌍 This list is outside the functions, so each function can use or change it.
people = ["Ben", "Jerry"]


# ➕ Add a name to the shared list, then show everyone currently on it.
def create(name):
    people.append(name)

    print(f"The people on our list are: ")
    for person in people:
        print(person)


# 📖 Read means display the names without changing the list.
def read():
    for person in people:
        print(person)


# 🛠️ These are placeholders: `pass` lets Python run an empty function for now.
def update():
    pass


def delete():
    pass


# 📋 Ask the user which menu action they want, and return the selected number.
def display_menu():
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    try:
        # input() gives us text, so int() converts it to a whole number.
        choice = int(input("Please enter the number of your selection:  "))
        if not 0 < choice < 5:
            print("Please select a number between 1 and 4")
            # Ask again when the number is outside the menu options.
            display_menu()
    except Exception as e:
        # This also handles input that cannot be converted to an integer.
        print(f"You have an error {e}, please type a number between 1 and 4")
        display_menu()
    return choice


# 🚦 main() coordinates the program: get a choice, then choose an action.
def main():
    selection = display_menu()
    print(selection)

    # match/case runs the block whose case matches the selected number.
    match selection:
        case 1:
            print("Create")
            new_name = input("Please enter your first name: ")
            create(new_name)
        case 2:
            print("Read")
            read()
        case 3:
            print("Update")
            update()
        case 4:
            print("Delete")
            delete()
        case _:
            # The underscore is the fallback case for any other value.
            print("Invalid choice.")
            selection = display_menu()


# ▶️ Start the program by calling its main function.
main()
