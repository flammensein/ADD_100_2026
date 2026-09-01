col_rent = 1500
col_utilities = 300
col_phone = 55

head_rent = "Rent"
head_utilities = "Utilities"
head_phone = "Phone"

expenses = col_phone + col_rent + col_utilities
phone_percent = col_phone / expenses

# print(f"{head_rent:^20}{head_utilities:^20}{head_phone:^20}")
# print(f"{col_rent:^20}{col_utilities:^20}{col_phone:^20}")

print(f"\n\nPhone percent of expenses is:   {phone_percent:.2%}")
