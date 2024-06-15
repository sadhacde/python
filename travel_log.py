# caesar cipher, shifts left to encode
# right to decode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(cipher_type, start_text, shift_amount):
    new_text = ""
    if shift_amount > 26:
        shift_amount %= 26
    for char in start_text:
        if char in alphabet:
            old = alphabet.index(char)
            if cipher_type == "encode":
                new = old + shift_amount
            elif cipher_type == "decode":
                new = old - shift_amount
            new_text += alphabet[new]
        else:
            new_text += char
    print(f"The {cipher_type}d text is {new_text}")

repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(cipher_type=direction, start_text=text, shift_amount=shift)

    repeat = input("Would you like to cipher another message? Type 'yes' or 'no'").lower()

if repeat == 'no':
    print("Goodbye!")