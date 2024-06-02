from math import inf

max_number = -inf

while True:
    usr_input = input()
    if usr_input != "Stop":
        usr_input = int(usr_input)
        if usr_input > max_number:
            max_number = usr_input
        else:
            continue
    else:
        break
print(max_number)