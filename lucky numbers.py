num = int(input())

for _ in range(1000, 10000):
    index = str(_)
    sum_first = int(index[0]) + int(index[1])
    sum_second = int(index[2]) + int(index[3])
    if sum_first == sum_second and sum_first != 0 and "0" not in index[0:4]:
        if num % sum_first == 0:
            print(_, end=" ")
