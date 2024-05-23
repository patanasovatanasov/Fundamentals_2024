n = int(input())

for strings in range(1, n + 1):
    string_given = input()
    if "," not in string_given and "." not in string_given and "_" not in string_given:
        print(f"{string_given} is pure.")
    else:
        print(f"{string_given} is not pure!")