male = int(input())
female = int(input())
table_count = int(input())
counter = 0

for m in range(1, male + 1):
    if counter == table_count:
        break
    for f in range(1, female + 1):
        print(f"({m} <-> {f})", end=" ")
        counter += 1
        if counter == table_count:
            break
