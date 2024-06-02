single_string = input()
list = []

for letters_index in range(len(single_string)):
    if 65 <= ord(single_string[letters_index]) <= 90:
        list.append(letters_index)
print(list)