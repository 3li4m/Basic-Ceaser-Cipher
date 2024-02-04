import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceaser(cipher_txt, cipher_shift, cipher_dir):
    cipher = ""
    if cipher_dir == "decode":
        cipher_shift *= -1

    for i in range(0, len(text)):
        if text[i] in alphabet:
            if (alphabet.index(text[i]) + cipher_shift) >= (len(alphabet)):
                cipher += alphabet[alphabet.index(text[i]) + cipher_shift -
                                   (len(alphabet))]
            else:
                cipher += alphabet[alphabet.index(text[i]) + cipher_shift]
        else:
            cipher += text[i]

    print(f"The decoded text is: {cipher}")


print(art.logo)

while (True):
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if (shift > 26):
        shift = shift % 26

    ceaser(cipher_txt=text, cipher_shift=shift, cipher_dir=direction)
    re_cipher = input(
        "[*****] Type 'Y' if you want to go again, otherwise type 'N' to exit: \n"
    )

    if (re_cipher.lower() == "n" or re_cipher.lower() == "no"):
        break

# def encrypt(encode_txt, encode_shift):
#     cipher = ""
#     for i in range(0, len(text)):
#         if text[i] in alphabet:
#             if (alphabet.index(text[i]) + shift) > (len(alphabet)):
#                 cipher += alphabet[alphabet.index(text[i]) + shift -
#                                    (len(alphabet))]
#             else:
#                 cipher += alphabet[alphabet.index(text[i]) + shift]

#     print(f"The decoded text is {cipher}")

# def decrypt(decode_txt, decode_shift):
#     decoded_cipher = ""
#     for i in range(0, len(text)):
#         if text[i] in alphabet:
#             if (alphabet.index(text[i]) - shift) < (0):
#                 decoded_cipher += alphabet[alphabet.index(text[i]) - shift +
#                                            (len(alphabet))]
#             else:
#                 decoded_cipher += alphabet[alphabet.index(text[i]) - shift]

#     print(f"The decoded text is {decoded_cipher}")

# if direction == "encode":
#     encrypt(encode_txt=text, encode_shift=shift)
# elif direction == "decode":
#     decrypt(decode_txt=text, decode_shift=shift)
# else:
#     print("No direction inputted")
