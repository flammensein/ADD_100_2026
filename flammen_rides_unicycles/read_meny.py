def read_menu():
    menus = {}
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(";")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
        return menus
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")
    return coffee, prices, milks, flavors, shots


def print_menu(coffee, prices, milks, flavors, shots):
    """This section deliberately incomplete"""
    print("Coffee\n")
    coffee_item = coffee.split(",")
    for item in coffee_item:
        print(f"\t{item.strip()}")


def main():
    menu_items = read_menu()
    coffee, prices, milks, flavors, shots = split_into_variables(menu_items)
    print_menu(coffee, prices, milks, flavors, shots)


main()
