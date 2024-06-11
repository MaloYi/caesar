#ENCRYPTION

def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

print(encrypt("Cuantos carros choco pancho pantera?", 21))
#output will be "xpviojn xvmmjn xcjxj kvixcj kviozmv?"

#DECRYPTION

def decrypt(message, shift):
    message = message.lower()
    decrypted_message = ""
    for char in message:
        if char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

print(decrypt("xpviojn xvmmjn xcjxj kvixcj kviozmv?", 21))
#output will be "Cuantos carros choco pancho pantera?"