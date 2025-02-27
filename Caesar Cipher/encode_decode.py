from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(original_text, shift_amount):
    encrypted_text = []
    for letter in original_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter_index += shift_amount
            if letter_index >= len(alphabet):
                letter_index -= len(alphabet)
            appendable = alphabet[letter_index]
        else:
            appendable = letter

        encrypted_text.append(appendable)

    print(''.join(encrypted_text))


def decrypt(encrypted_text, shift_amount):
    decrypted_text = []
    for letter in encrypted_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            letter_index -= shift_amount
            if letter_index >= len(alphabet):
                letter_index += len(alphabet)
            appendable = alphabet[letter_index]
        else:
            appendable = letter
        decrypted_text.append(appendable)
    print(''.join(decrypted_text))


if direction.lower() == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction.lower() == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("wrong entry")
