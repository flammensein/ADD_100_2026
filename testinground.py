DEPT_IN = [
    "exit function",
    "Book Store",
    "Finance",
    "Help Desk",
    "Book Store",
    "Administration",
    "Human Resources",
    "Student Services",
    "Facilities",
    "Academic Affairs",
]

print(f"\n\tYou must be a member of a department authorized to reset user passwords.")
print(f"\n")
for dept_name in DEPT_IN:
    print(f"\t{DEPT_IN.index(dept_name)}: {dept_name}")
what_your_dept = input(
    f"\n\tPlease select your department from the list above (1-9):\t"
)
