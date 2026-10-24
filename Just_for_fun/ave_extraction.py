import sqlite3
import csv
import re
import os

# Trithemius's 24-letter alphabet, matching the Polygraphia tables
ALPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "x",
    "y",
    "z",
    "w",
]


def clean_raw_text(filepath):
    """Reads a text file and returns a list of lowercase alphabetic words."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw text file not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Extract only alphabetic characters, stripping numbers and punctuation
    words = re.findall(r"[a-zA-Z]+", raw_text.lower())
    return words


def parse_to_structured_data(words):
    """Chunks a list of words into 24-letter columns."""
    structured_data = []
    column_index = 1

    # Iterate through the word list in chunks of 24
    for i in range(0, len(words), 24):
        chunk = words[i : i + 24]

        # Flag incomplete columns at the end of the file
        if len(chunk) < 24:
            print(
                f"Warning: Column {column_index} is incomplete. Expected 24 words, got {len(chunk)}."
            )

        for j, word in enumerate(chunk):
            if j < len(ALPHABET):
                letter = ALPHABET[j]
                structured_data.append((column_index, letter, word))

        column_index += 1

    return structured_data


def export_to_sqlite(data, db_path="ave_maria.db"):
    """Exports structured data to a SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vocabulary (
            Column_Index INTEGER,
            Plaintext_Letter TEXT,
            Cipher_Word TEXT
        )
    """)

    # Clear existing data to prevent appending duplicates on rerun
    cursor.execute("DELETE FROM Vocabulary")

    cursor.executemany(
        """
        INSERT INTO Vocabulary (Column_Index, Plaintext_Letter, Cipher_Word)
        VALUES (?, ?, ?)
    """,
        data,
    )

    conn.commit()
    conn.close()


def export_to_csv(data, csv_path="ave_maria.csv"):
    """Exports structured data to a CSV file."""
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Column_Index", "Plaintext_Letter", "Cipher_Word"])
        writer.writerows(data)


if __name__ == "__main__":
    # Point this variable to your raw OCR text file once you have it
    raw_text_file = "raw_polygraphia_dump.txt"

    try:
        # Create a dummy file for testing purposes if it doesn't exist
        if not os.path.exists(raw_text_file):
            with open(raw_text_file, "w") as f:
                f.write("test " * 48)  # Creates exactly 2 columns worth of dummy data

        words = clean_raw_text(raw_text_file)
        parsed_data = parse_to_structured_data(words)

        export_to_sqlite(parsed_data)
        export_to_csv(parsed_data)

        total_columns = len(parsed_data) // 24
        print(f"Successfully parsed {len(words)} words into {total_columns} columns.")

    except Exception as e:
        print(f"Execution Error: {e}")
