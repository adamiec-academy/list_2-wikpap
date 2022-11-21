def cipher(text, shift):
    result = ""

    for char in text:
        if char == " ":
            result += " "
        elif (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decipher(text, shift):
    return cipher(text, -shift)
