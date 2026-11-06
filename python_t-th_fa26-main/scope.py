"""
passing values, scope
"""

# ℹ️ This file demonstrates scope: global variables, function parameters, and nested functions.

# 📌 GLOBAL CONSTANTS (available everywhere in this file)
DOGS = ("Bouvier", "Shepherd", "Collie", "Border Collie")


def favorite_dogs(more=("Bouvier Des Flanders", "German Shepherd")):
    # ℹ️ `more` is a parameter with a default value (a tuple of extra dogs).
    # ⚠️ Beginner pitfall: avoid mutable defaults (like `[]`); tuples are safe here.
    for dog in DOGS:
        # 🖨️ Print each dog from the global constant tuple.
        print(dog)
    for dog in more:
        # 🖨️ Print each dog from the parameter tuple.
        print(dog)


def count(one, two, three):
    # 🖨️ Show the values we received via parameters (positional/keyword args).
    print(f"{one}  {two}  {three}")
    # ✅ Return: a tuple in reverse order (three, two, one)
    return three, two, one


def main():
    # ▶️ Entry point: define local values, call functions, and show nested scope.

    # ℹ️ Local variable: only `main()` can see `more_dogs` directly...
    more_dogs = ("Bulldog", "Great Dane", "Boxer")

    # 🧠 Plan: print global dogs → print default "more" dogs
    favorite_dogs()

    def nested_function():
        # ℹ️ ...but a nested function can "close over" variables from the outer scope.
        print("\n\n Nested function")
        for dog in more_dogs:
            # 🖨️ Print each dog from the `main()` scope (captured by the nested function).
            print(dog)

    # 🧠 Plan: run the nested function to prove it can access `more_dogs`.
    nested_function()

    # 🧪 Test: keyword arguments can be passed in any order.
    num1, num2, num3 = count(one=11, three=13, two=12)
    # ✅ Expected: values come back reversed (13 12 11)
    print(num1, num2, num3)


main()
