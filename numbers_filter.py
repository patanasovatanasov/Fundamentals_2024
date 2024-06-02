n = int(input())
lst = []
lst2 = []

for i in range(n):
    inputs = int(input())
    lst.append(inputs)
command = input()
if command == "even":
    for i in range(n):
        if lst[i] % 2 == 0:
            lst2.append(lst[i])
elif command == "odd":
    for i in range(n):
        if lst[i] % 2 != 0:
            lst2.append(lst[i])
elif command == "negative":
    for i in range(n):
        if lst[i] < 0:
            lst2.append(lst[i])
elif command == "positive":
    for i in range(n):
        if lst[i] >= 0:
            lst2.append(lst[i])
print(lst2)
