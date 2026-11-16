"""
Classes & objects (beginner-friendly example)

ℹ️ A *class* is a blueprint for making objects.
ℹ️ An *object* (also called an *instance*) is one specific thing made from that blueprint.

This file demonstrates:
- Creating a class with attributes (data)
- Writing methods (functions that belong to a class)
- Using "private" attributes with double underscores (encapsulation)

⚠️ Note: In real projects, we usually run the program using the
`if __name__ == "__main__":` pattern so the file doesn't auto-run when imported.
"""


class Drink:
    def __init__(self, drink_type, size, milk, flavor, pumps):
        # ℹ️ The constructor runs automatically when you create a new Drink(...).
        # ✅ Goal: store the starting values for this drink object.
        #
        # ⚠️ "Private" attributes:
        # - A name starting with `__` is *name-mangled* by Python.
        # - This discourages direct access like `latte.__size` from outside the class.
        # - We access/update them using methods (getters/setters) instead.
        self.__drink_type = drink_type
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__pumps = pumps

    # 📌 Getters (accessor methods)
    # ✅ Goal: safely read a value from the object.
    # ℹ️ Naming note: Many codebases use `property` instead of explicit get_/set_ methods,
    # but getters/setters are a clear first-semester way to practice encapsulation.
    def get_drink(self):
        return self.__drink_type

    def get_size(self):
        return self.__size

    def get_milk(self):
        return self.__milk

    def get_flavor(self):
        return self.__flavor

    def get_pumps(self):
        return self.__pumps

    # 📌 Setters (mutator methods)
    # ✅ Goal: safely change a value stored in the object.
    # ⚠️ Common beginner mistake: forgetting to assign to `self.__...`.
    # You must update the attribute on *this object* (self), not a local variable.

    def set_drink(self, drink_type):
        self.__drink_type = drink_type

    def set_size(self, size):
        self.__size = size

    def set_milk(self, milk):
        self.__milk = milk

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def set_pumps(self, pumps):
        self.__pumps = pumps

    def summary(self):
        # 🖨️ Display a quick "receipt-style" description of this object.
        # ⚠️ Consistency tip: try to keep `pumps` the same type everywhere (int is typical).
        print(
            f"{self.__drink_type}, {self.__size}, {self.__milk},{self.__flavor}, {self.__pumps}"
        )


def main():
    # ▶️ Entry point for this lesson/demo file.
    # 🧪 Create a couple of Drink objects, then call their methods.

    latte = Drink("Latte", "Extra Large", "Whole", "Caramel", "5")
    matcha = Drink("Matcha", "Large", "2%", "none", 0)

    latte.summary()
    matcha.summary()


if __name__ == "__main__":
    main()
