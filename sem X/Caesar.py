def caesar(text1):
    key = 19
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
    ALPHABET = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"
    new_alphabet = ""
    NEW_ALPHABET = ""
    new_text = ""
    for i in range(key, 33):
        new_alphabet += alphabet[i]
    for i in range(key):
        new_alphabet += alphabet[i]
    NEW_ALPHABET = ""
    for i in range(key, 33):
        NEW_ALPHABET += ALPHABET[i]
    for i in range(key):
        NEW_ALPHABET += ALPHABET[i]
    print(new_alphabet, len(new_alphabet))
    print(NEW_ALPHABET, len(NEW_ALPHABET))
    for i in range(len(text1)):
        if text1[i] in alphabet:
            new_text += new_alphabet[alphabet.index(text1[i])]
        elif text1[i] in ALPHABET:
            new_text += NEW_ALPHABET[ALPHABET.index(text1[i])]
        else:
            new_text += text1[i]
    return new_text


print(caesar(input()))
