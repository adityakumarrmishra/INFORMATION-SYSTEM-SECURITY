def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return "".join(result)

plaintext = "Hello, World!"
key = 3
encrypted = caesar_cipher(plaintext, key)
decrypted = caesar_cipher(encrypted, -key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
