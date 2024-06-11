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

#DECRYPTION

def decrypt(message, key):
    message = message.lower()
    decrypted_message = ""
    for char in message:
        if char.islower():
            decrypted_message += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

print(decrypt("xpviojn xvmmjn xcjxj kvixcj kviozmv?", 21))