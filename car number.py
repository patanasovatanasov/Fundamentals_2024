begin = int(input())
end = int(input())

for n in range(begin, end + 1):
    for n1 in range(begin, end + 1):
        for n2 in range(begin, end + 1):
            for n3 in range(begin, end + 1):
                if (n % 2 == 0 and n3 % 2 == 1) or (n % 2 == 1 and n3 % 2 == 0):
                    if n > n3:
                        if (n1 + n2) % 2 == 0:
                            print(f"{n}{n1}{n2}{n3}", end=" ")
