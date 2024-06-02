n = int(input())

for numbers in range(n):
    number = int(input())
    if number % 2 == 0:
        continue
    else:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")