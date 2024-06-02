number = int(input())

for _ in range(1, number, 1):
    print(f"*" * _)
for __ in range(number, 0, -1):
    print(f"*" * __)