first_line = input().split(", ")
second_line = input().split(", ")
new_list = []


def subtracted(f, s):
    new_list = [x for x in f if any(x in y for y in s)]
    return new_list


print(subtracted(first_line, second_line))