# Final Project: Coffee/Tea Order Menu

This folder contains a small, terminal-based ordering program that:

1. Collects employee information (who the drink is for).
2. Loads a menu from a text file.
3. Prompts the employee to pick a drink + options (size/milk/flavor/etc.).
4. Saves the results to simple text files for later reference.

## How To Run

From the **repo root** (`python_t-th_fa26/`), run:

```bash
python final_project/main.py
```

Running from the repo root matters because several modules open files using paths like `final_project\menu.txt`.

## Files And How They’re Related

**Program flow (high level):**

`main.py` → `employee.py` → `order.py` → `read_menu.py` → `menu.txt`

### Python files

- `main.py`
  - Entry point that starts the program and calls the major steps in order.
  - Imports and uses `employee.py` and `order.py`.

- `employee.py`
  - Handles employee input (ID, name, office, extension, allergies).
  - Appends employee info to `employee.txt`.

- `order.py`
  - Handles the drink-order prompts.
  - Calls `read_menu.read_menu()` to load menu data from `menu.txt`.
  - Writes orders to an `order_history` file (the file path is relative to the *current working directory*).

- `read_menu.py`
  - Reads `menu.txt` into a dictionary (category → comma-separated values).
  - Splits the dictionary values into variables for `order.py`.
  - Contains helper “print menu screen” functions (ex: printing drink types and sizes).

- `create_menu.py`
  - Helper script to *append* new menu categories/items into `menu.txt`.
  - Useful if you want to rebuild/extend the menu without editing the text file by hand.

### Data files

- `menu.txt`
  - The menu source of truth.
  - Format is one category per line, like:
    - `DRINK_TYPE : Americano, drip, latte, ...`
    - `SIZES : Extra Large, Large, medium, small`
    - `PRICES : 7.0, 6.0, 5.0, 4.0`

- `employee.txt`
  - Appends employee records in a simple `id:{...}` per-line format.

- `error_log.txt` (created at runtime if needed)
  - If `read_menu.py` hits an unexpected exception, it appends a timestamped line here.

## Notes

- There are multiple `coffee*.py` files in this folder; they appear to be earlier planning/iteration versions of the project and are not the primary entry point. The intended “run me” file is `main.py`.
- `create_menu.py` appends to `menu.txt` (it does not clear the file first). If you run it multiple times, you may end up with duplicate categories/lines.

