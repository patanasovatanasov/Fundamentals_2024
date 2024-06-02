n = int(input())

for number in range(1111, 10000):
    for digit in str(number):
        if digit == "0":
            break
        if n % int(digit) != 0:
            break
    else:
        print(number, end=" ")