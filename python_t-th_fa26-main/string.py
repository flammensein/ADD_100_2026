"""
String mastery: working with text, string methods, and built-in functions.
"""

greeting = "Hello"

print(greeting)

# ℹ️ info: The + operator concatenates (joins) strings. Strings are immutable,
# so this expression creates a new string and assigns it back to greeting.
greeting = greeting + " World"

print(greeting)

# ℹ️ info: Escape sequences start with a backslash: \n makes a new line and
# 	 inserts a tab. The double quote here is ordinary text inside single quotes.
print('\n\n new lines, \t tab " ')
# 💡tip: Multiplying a string repeats its contents; this prints 100 asterisks.
print("*" * 100)


# 🔤 Converting values to strings

ten = 10

# ⚠️ warning: Python cannot concatenate a string and an integer directly.
# print("Ten: " + ten)
# ℹ️ info: str() is a built-in conversion function; it returns the number as text.
print("Ten: " + str(ten))
# 💡tip: An f-string inserts the value into the text without explicitly calling str().
print(f"Ten:  {ten}")


name = "meri kasprak   "
# ℹ️ info: strip() returns a string with whitespace removed from both ends.
# title() returns a title-cased string, capitalizing the start of each word.
# String methods return results; they do not change the original string in place.
print(name.strip().title())

string_list = "John Jacob Jingleheimer Schmidt"
# ℹ️ info: split(" ") separates this string wherever there is a space and returns a list.
list_of_string = string_list.split(" ")
print(list_of_string)
# ℹ️ info: A for loop can visit each string in the list one at a time.
for item in list_of_string:
    print(item)


# 🐶 Bingo: replacing letters one at a time
# ℹ️ info: Strings cannot be changed in place, so list() (a built-in function)
# makes a list of individual characters that we can update.
name_string = "BINGO"
dog_letters = list(name_string)
count = 0

# 2. THE LOOP: This runs once for each character in "BINGO".
for char in name_string:
    # ℹ️ info: join() is a string method. The string before the dot is the
    # separator placed between each item from the iterable (here, a list).
    current_name = " ".join(dog_letters)

    print("There was a farmer who had a dog and Bingo was his Name-o")
    # 💡tip: The f-string inserts current_name; multiplying the result repeats it 3 times.
    print(f"({current_name}) \n" * 3)
    print("and Bingo was his Name-o!\n")

    # Replace the character at this position; count tracks the matching list index.
    dog_letters[count] = "🐶"
    count += 1

# 3. THE FINALE: join() combines the updated list of characters into one string.
final_name = " ".join(dog_letters)
print(f"({final_name}) \n" * 3)
print("and Bingo was his Name-o!")
