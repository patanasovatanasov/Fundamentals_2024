first = int(input())
second = int(input())
third = int(input())

for f in range(2, first + 1, 2):
    for s in range(2, second + 1):
        is_prime = True
        for i in range(2, s):
            if s % i == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        for t in range(2, third + 1, 2):
            print(f"{f} {s} {t}")