def frequency(text2):
    Qall = len(text2)
    print(Qall)
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ALPHABET = list(ALPHABET)
    alphabet = list(alphabet)
    start_freques = []
    for elem in alphabet:
        if elem in text2:
            start_freques.append(text2.count(elem))
        elif elem not in text2:
            start_freques.append(0)
    for elem in ALPHABET:
        if elem in text2:
            i = ALPHABET.index(elem)
            start_freques[i] += 1
    for i in range(len(start_freques)):
        start_freques[i] = start_freques[i] / Qall
    print(*start_freques)


def frequency_decode(text2):
    new_text = ""
    alphabet = "вгдеиклморсуфшхпжныйбзтаьячюцёщэъВГДЕИКЛМОРСУФШХПЖНЫЙБЗТАЬЯЧЮЦЁЩЭЪ"
    alphabet = list(alphabet)
    enc_alphabet = "ормщгчясцжштпеванюзыьйбэхилфёдъкуОРМЩГЧЯСЦЖШТПЕВАНЮЗЫЬЙБЭХИЛФЁДЪКУ"
    enc_alphabet = list(enc_alphabet)
    for i in range(len(text2)):
        if text2[i] in enc_alphabet:
            new_text += alphabet[enc_alphabet.index(text2[i])]
        else:
            new_text += text2[i]
    return new_text


print(frequency_decode(input()))
