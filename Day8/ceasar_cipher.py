print("CEASAR CIPHER")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encoder(message, number_shifts):
    cipher_text = ""
    for x in message:
        position = alphabet.index(x)
        new_position = position + number_shifts
        if new_position>25:
            new_position-=25
            print("**Please Avoid Shifting Greater then 25**")
        text = alphabet[new_position]
        cipher_text += text

    print(f"The Original text is {message}")
    print(f"The encoded text is {cipher_text}")

def decoder(message,number_shifts):
    decrypted_text =""
    for x in message:
        position = alphabet.index(x)
        new_position = position-number_shifts
        if new_position<0:
            new_position+=25
            print("**Please Avoid Shifting Less then 0**")
        text = alphabet[new_position]
        decrypted_text +=text
    print(f"The Original text is {message}")
    print(f"The dencoded text is {decrypted_text}")

while True:
    choice = input("Type 'encode' to encrpt 'decode' to decrypt: ")
    if choice== "encode":
        message = input("Message to Encode: ").lower()
        number_shifts  =int(input("Number of Shifts: "))
        encoder(message,number_shifts)
    elif choice== "decode":
        text_to_decode = input("Message to Decode:").lower()
        number_shifts  =int(input("Number of Shifts: "))
        decoder(text_to_decode,number_shifts)

    re_run = input("Type Yes or No to continue game: ").lower()
    if re_run == "yes":
        pass
    else:
        break