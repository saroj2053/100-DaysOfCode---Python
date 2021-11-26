# Refactoring code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type decode to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "decode":
        shift *= -1


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        print(f"The {cipher_direction}d text is {end_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go on again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
