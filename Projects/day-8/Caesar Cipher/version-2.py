alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type decode to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        position = position % 25  # what if the text entered contains z
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The cipher text is: {cipher_text}")


encrypt(plain_text=text, shift_amount=shift)

txt = input("Enter encoded message: \n")
decrypt_shift = int(input("Enter shift amount: \n"))


def decrypt(cipher_text, shift_amt):
    plaintext = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amt
        new_letter = alphabet[new_position]
        plaintext += new_letter
    print(f"The plaintext is: {plaintext}")


decrypt(cipher_text=txt, shift_amt=decrypt_shift)