import json
import random
import os


def load_dictionary(filepath):
    """Loads the Ave Maria dictionary from an external JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dictionary file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_decrypt_dict(trithemius_dict):
    """Builds a reverse-lookup dictionary for decryption."""
    decrypt_dict = {}
    for letter, words in trithemius_dict.items():
        for word in words:
            # Check prevents overwriting I/U with J/V/W during reverse mapping
            if word.lower() not in decrypt_dict:
                decrypt_dict[word.lower()] = letter
    return decrypt_dict


def encrypt_ave_maria(plaintext, trithemius_dict):
    """Encrypts a string by replacing letters with Latin words from the JSON."""
    plaintext = plaintext.lower()
    ciphertext = []

    for char in plaintext:
        if char in trithemius_dict:
            word = random.choice(trithemius_dict[char])
            ciphertext.append(word.capitalize())

    return " ".join(ciphertext)


def decrypt_ave_maria(ciphertext, decrypt_dict):
    """Decrypts a string by matching Latin words back to their source letters."""
    words = ciphertext.lower().split()
    plaintext = []

    for word in words:
        clean_word = "".join(c for c in word if c.isalpha())
        if clean_word in decrypt_dict:
            plaintext.append(decrypt_dict[clean_word])

    return "".join(plaintext)


if __name__ == "__main__":
    dict_file = "trithemius_dict.json"

    try:
        # Load external JSON
        trithemius_dict = load_dictionary(dict_file)
        decrypt_dict = build_decrypt_dict(trithemius_dict)

        # Test the implementation
        message = "secret"
        encrypted = encrypt_ave_maria(message, trithemius_dict)
        decrypted = decrypt_ave_maria(encrypted, decrypt_dict)

        print(f"Original: {message}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")

    except Exception as e:
        print(f"Execution Error: {e}")
