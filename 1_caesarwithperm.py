# """

alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

def encrypt_decrypt(text, mode, key, key2):
    num_letters = len(alphabet)
    result = ''
    keyed_alphabet = new_alphabet(key2)

    key = key % num_letters
    if mode == 'd':
        key = -key # reverses the shift (forward = encryption, backward = decryption)

    for char in text:
        upper = char.upper()
        if upper in keyed_alphabet: #checking if it's Romanian character
            new_position = (keyed_alphabet.index(upper) + key) % num_letters # find letter position, move it by key, wrap around with modulus
            result += keyed_alphabet[new_position] # convert the position above to the new letter
        elif not char.isspace():
            # any other characters pass through, like punctuation, space...
            result += upper

    return result

def new_alphabet(key2):
    keyword = key2.upper()
    result = ''

    for char in keyword: # keeps only the first occurrence of each letter
        if char not in result:
            result += char

    for char in alphabet: # remaining alphabet
        if char not in result:
            result += char

    assert len(result) == len(alphabet) #safety check

    return result

def get_valid_keyword():
    while True:
            key2 = input("Enter a second key (must be at least 7 characters long): " )
            key2 = key2.replace('ş', 'ș').replace('ţ', 'ț').replace('Ş', 'Ș').replace('Ţ', 'Ț')

            invalid_charac = sorted({c for c in key2 if c.upper() not in alphabet})
            if invalid_charac:
                print(f"Input rejected. Invalid character(s): {' '.join(invalid_charac)}")
                print("Use only Romanian letters, with no spaces. Try again.")
            elif len(key2) < 7:
                print("Second key must be at least 7 characters long.")
            else:
                return key2.upper()

def get_valid_key():
    max_key = len(alphabet) - 1  # 31-1=30
    while True:
        try:
            key = int(input(f'Enter a key (1 through {max_key}): '))
            if 1 <= key <= max_key:
                return key # valid key is returned immediately
            else:
                print(f"Key must be between 1 and {max_key}. Please try again.")
        except ValueError: # non-numeric input
            print(f"Invalid input. Please enter a number between 1 and {max_key}.")

def find_invalid_chars(text):
    return sorted({c for c in text if c.upper() not in alphabet and not c.isspace()}) # return letters not part of RO alphabet

def get_valid_text(prompt):
    while True:
        text = input(prompt)
        text = text.replace('ş', 'ș').replace('ţ', 'ț').replace('Ş', 'Ș').replace('Ţ', 'Ț')
        invalid = find_invalid_chars(text)
        if invalid:
            print(f"Input rejected. Invalid character(s): {' '.join(invalid)}")
            print("Please use only Romanian letters. Try again.")
        else:
            return text


def main():
    while True:
        print("\n*** CAESAR CIPHER PROGRAM ***")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nENCRYPTION MODE")
            key = get_valid_key()
            key2 = get_valid_keyword()
            text = get_valid_text('Enter the text to encrypt: ')
            ciphertext = encrypt_decrypt(text, 'e', key, key2)
            print(f'CIPHERTEXT: {ciphertext}')

        elif choice == '2':
            print("\nDECRYPTION MODE")
            key = get_valid_key()
            key2 = get_valid_keyword()
            text = get_valid_text('Enter the text to decrypt: ')
            plaintext = encrypt_decrypt(text, 'd', key, key2)
            print(f'PLAINTEXT: {plaintext}')

        elif choice == '3':
            print("Thank you for using the Caesar Cipher program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
# """

