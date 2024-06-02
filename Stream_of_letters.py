word = ""
sentence = ""
count_n, count_o, count_c = 0, 0, 0

while True:
    letter = input()
    if letter == "End":
        if count_c == 1 and count_n == 1 and count_o == 1:
            sentence += word + " "
            print(sentence)
            break
        else:
            print(sentence)
            break

    if 64 < ord(letter) < 91 or 96 < ord(letter) < 123:
        if count_c == 1 and count_n == 1 and count_o == 1:
            sentence += word + " "
            word = ""
            count_n, count_o, count_c = 0, 0, 0
        if letter == "n" and count_n == 0:
            count_n += 1
            continue
        if letter == "o" and count_o == 0:
            count_o += 1
            continue
        if letter == "c" and count_c == 0:
            count_c += 1
            continue
        word += letter
    else:
        continue