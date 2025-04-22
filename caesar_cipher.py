alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Caesar Cipher!")

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


def decrypt(encrypted_word, key):

    decoded_word = ""
    for char in encrypted_word:
        if (char in alphabet):
            encoded_index = alphabet.index(char)
            decode_index = encoded_index - key
            decoded_word += alphabet[decode_index]
        else:
            decoded_word += char

    print(f"The original message was: {decoded_word}")


if (direction == 'encode'):
    encrypted_word = encrypt(text, shift)
    print(f"Message encoded to: {encrypted_word}")

elif (direction == 'decode'):
    decrypted_word = decrypt(text, shift)

else:
    print("Enter correct option.")
