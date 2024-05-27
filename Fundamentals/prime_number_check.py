number = int(input())

if number <= 1:
    print("False")
if number == 2:
    print("True")
if number % 2 == 0:
    print("False")
max_divisor = int(number ** 0.5) + 1
for d in range(3, max_divisor, 2):
    if number % d == 0:
        continue
print("False")
