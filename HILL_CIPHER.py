def hill_encrypt(plaintext, key):
    import string
    alphabet = string.ascii_lowercase
    key_values = [alphabet.index(c) for c in key.lower() if c.isalpha()]
    size = int(len(key_values)**0.5)
    matrix = [key_values[i*size:(i+1)*size] for i in range(size)]
    while len(plaintext) % size != 0:
        plaintext += 'x'
    result = []
    for i in range(0, len(plaintext), size):
        block = [alphabet.index(c) for c in plaintext[i:i+size].lower()]
        enc = [(sum(block[k] * matrix[j][k] for k in range(size))) % 26 for j in range(size)]
        result.extend(enc)
    return ''.join(alphabet[i] for i in result).upper()

if __name__ == "__main__":
    text = "attackatdawn"
    key = "hill"
    encrypted = hill_encrypt(text, key)
    print(encrypted)
