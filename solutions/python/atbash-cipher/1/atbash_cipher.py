cipher = "zyxwvutsrqponmlkjihgfedcba"
plain = "abcdefghijklmnopqrstuvwxyz"


def encode(plain_text):
    ciphred_text = ""
    for char in plain_text:
        if char.isalpha():
            pos = plain.index(char.lower())
            ciphred_text += cipher[pos]
        elif char.isdigit():
            ciphred_text += char
    blocs = []
    for i in range(0, len(ciphred_text), 5):
        bloc = ciphred_text[i:i+5]
        blocs.append(bloc)
    return " ".join(blocs)


def decode(ciphered_text):
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            pos = cipher.index(char.lower())
            plain_text += plain[pos]
        elif char.isdigit():
            plain_text += char
    return plain_text


print(encode("Testing,1 2 3, testing."))
