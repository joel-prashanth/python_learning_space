alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt and 'decode' to decrypt your message: ").lower().strip()

text = input("Type your message: ").lower().strip()

shift = int(input("Type shift number: "))


def encrypt(original_text, shift_key):

    encoded_word = ""

    for char in original_text:

        if (char in alphabet):
            alpha_index = alphabet.index(char)
            shifted_index = alpha_index + shift_key
            encoded_alphabet = alphabet[shifted_index]
            encoded_word += encoded_alphabet
        else:
             encoded_word += char

    return encoded_word

encrypted_word = encrypt(text, shift)
print(encrypted_word)

if (direction == 'encode'):
    encrypt
