"""
imported into main.py

"""

import datetime
import os


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def read_menu():
    menus = {}
    try:
        with open("final_project\\menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":", 1)
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
        print(f"Menus: {menus}")
        return menus
    except FileNotFoundError:
        print(f'Please create the file or check the file name. It should be "menu.txt"')
        return menus
    except IndexError:
        return menus
    except Exception as e:
        right_now = datetime.datetime.now()
        error_log_path = os.path.join("final_project\\error_log.txt")
        with open(error_log_path, "a") as f:
            f.write(f"{right_now}, {e}\n")
        print(e)


def split_into_variables(menu_items):
    print("I'm in split into variables")
    coffee = menu_items.get("DRINK_TYPE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILKS")
    flavors = menu_items.get("FLAVORS")
    sizes = menu_items.get("SIZES")
    print(f"split into variables: {coffee}, {prices}, {milks}, {flavors}, {sizes}")
    return coffee, prices, milks, flavors, sizes


def print_coffee(coffee):

    clear_screen()
    print("Coffee\n")
    count = 1
    coffee_item = coffee.split(",")
    for item in coffee_item:
        print(f"{count}.  \t{item.strip()}")
        count += 1
    return len(coffee)


def print_sizes(sizes, prices):
    clear_screen()
    print("Sizes\n")
    count = 1
    sizes_item = sizes.split(",")
    prices_item = prices.split(",")
    for item in range(0, len(sizes_item)):
        print(f"{count}. {sizes_item[item]}       $ {float(prices_item[item]):.2f}")
        count += 1
