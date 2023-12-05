def atbash(text):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet = list(alphabet)
    new_text = ""
    for i in range(len(text)):
        if text[i] in alphabet:
            new_text += alphabet[-1 - alphabet.index(text[i])]
        elif text[i] in ALPHABET:
            new_text += ALPHABET[-1 - ALPHABET.index(text[i])]
        else:
            new_text += text[i]
    return new_text


print(atbash(input()))
