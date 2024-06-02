from math import inf

min_number = inf

while True:
    usr_input = input()
    if usr_input != "Stop":
        usr_input = int(usr_input)
        if usr_input < min_number:
            min_number = usr_input
        else:
            continue
    else:
        break
print(min_number)