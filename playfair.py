def generate_key_table(key):
    key = key.lower().replace("j", "i")
    table = []
    for c in key:
        if c not in table and c.isalpha():
            table.append(c)
    for c in range(ord('a'), ord('z') + 1):
        ch = chr(c)
        if ch == 'j':
            continue
        if ch not in table:
            table.append(ch)
    return [table[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.lower().replace("j", "i")
    text = "".join([c for c in text if c.isalpha()])
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        b = ''
        if i+1 < len(text):
            b = text[i+1]
        if a == b:
            pairs.append(a + 'x')
            i += 1
        else:
            if i+1 < len(text):
                pairs.append(a + b)
                i += 2
            else:
                pairs.append(a + 'x')
                i += 1
    return pairs

def find_position(c, table):
    for row_i, row in enumerate(table):
        if c in row:
            return row_i, row.index(c)

def playfair_encrypt(message, key):
    table = generate_key_table(key)
    pairs = preprocess_text(message)
    encrypted = []
    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(a, table)
        r2, c2 = find_position(b, table)
        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            c1, c2 = c2, c1
        encrypted.append(table[r1][c1])
        encrypted.append(table[r2][c2])
    return "".join(encrypted).upper()

if __name__ == "__main__":
    key_input = "playfair example"
    message_input = "hide the gold in the tree stump"
    result = playfair_encrypt(message_input, key_input)
    print(result)
