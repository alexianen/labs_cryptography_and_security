import re

alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = len(alphabet)

# -----------   Vigenere algorithm -----------

def encrypt_decrypt(text, key, decrypt=False):
    sign = -1 if decrypt else 1
    result = []
    for i, char in enumerate(text):
        shift = alphabet.index(key[i % len(key)])
        result.append(alphabet[(alphabet.index(char) + sign * shift) % N])
    return "".join(result)
# --------------------------------------------

# -----------   Validation -----------

CEDILLA_FIX = str.maketrans('şţŞŢ', 'șțȘȚ')   # cedilla becomes diacritic
PUNCTUATION = re.compile(r'[\s\-,.!?–—]')


def find_invalid_chars(text):
    return sorted({c for c in text if c.upper() not in alphabet})


def get_valid_input(prompt, min_length=0, strip_punctuation=False):
    while True:
        text = input(prompt).translate(CEDILLA_FIX)
        if strip_punctuation:
            text = PUNCTUATION.sub('', text)

        invalid = find_invalid_chars(text)
        if invalid:
            print(f"Input rejected. Invalid character(s): {' '.join(invalid)}")
            print("Use only Romanian letters. Try again.")
        elif len(text) < min_length:
            print(f"Input must be at least {min_length} characters long.")
        else:
            return text.upper()


def main():
    while True:
        print("\n*** VIGENÈRE CIPHER PROGRAM ***")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nENCRYPTION MODE")
            key = get_valid_input("Enter the key (at least 7 letters, no spaces): ", min_length=7)
            text = get_valid_input("Enter the text to encrypt: ", strip_punctuation=True, min_length=1)
            print(f'CIPHERTEXT: {encrypt_decrypt(text, key)}')
        elif choice == '2':
            print("\nDECRYPTION MODE")
            key = get_valid_input("Enter the key (at least 7 letters, no spaces): ", min_length=7)
            text = get_valid_input("Enter the text to decrypt: ", strip_punctuation=True, min_length=1)
            print(f'PLAINTEXT: {encrypt_decrypt(text, key, decrypt=True)}')

        elif choice == '3':
            print("Thank you for using the Vigenère Cipher program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
