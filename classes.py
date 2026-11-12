"""

classes and object

"""


class Drink:
    def __init__(self, drink_type, size, milk, flavor, pumps):
        # private attributes __ double underscore makes them private
        self.__drink_type
        self.__size
        self.__milk
        self.__flavor
        self.__pumps

        # getters
        def get_drink(self):
            return self.__drink_type

        def get_size(self):
            return self.__size

        def get_milk(self):
            return self.__milk

        def get_flavor(self):
            return self.__flavor

        def get_pump(self):
            return self.__pumps

        # setters
        def set_drink(self, drink_type):
            self.__drink_type = drink_type

        def set_milk(self, milk):
            self._milk = milk

        def set_size(self, size):
            self.__size = size

        def set_flavor(self, flavor):
            self.__flavor = flavor

        def set_pumps(self, pumps):
            self.__pumps = pumps


def main():

    latte = Drink("Latte", "Extra Large", "Whole", "Caramel", "5")
    matcha = Drink("Matcha", "Large", "2%", "none", 0)

    latte.summary()
    matcha.summary()


main()
