# 🔁 LOOP EXAMPLES
# A loop repeats code over and over until a condition is met.

# 🧠 while loop: keep going while the condition remains true.
print("While")
count = 10
while count > 0:
    print(count)
    count -= 1  # 💡 Decrease the value so the loop eventually stops.

# 🔁 for loop: repeat a known number of times.
print("\n\nfor")
for m in range(10, 0, -1):
    print(m)

print("\n\nrecursion")


# 🧠 Recursion is when a function calls itself.
# ⚠️ Be careful: if the condition never changes, it can loop forever and crash.
def count(m):
    print(m)
    if m > 1:
        m = m - 1
        count(m)


count(10)

# 🧠 while loop with a condition change
# This loop keeps asking until the user says yes.
answer = "no"

while answer != "yes":
    answer = input("Can I watch tv? (yes/no)").lower()

# 🩺 Example using a condition with temperature.
temperature = 98.4

while temperature < 99:
    print("You have to go to school.")
    print("but I'm sick!")
    temperature = float(input("Enter temperature:  "))

print("Ok. You can stay home. No video games. ")

# 📅 A for loop can also iterate through a list of items.
days_of_week = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
for day in days_of_week:
    print(day)

# 💡 Tip: while loops are useful when you do not know ahead of time how many times you need to repeat.
# 💡 Tip: for loops are useful when you are looping through a fixed list or range.
# ⚠️ Warning: infinite loops happen when the condition never becomes false.
