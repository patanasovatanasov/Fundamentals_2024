import math

prime_sum = 0
nonprime_sum = 0

while True:
    num = input()
    if num == "stop":
        print(f"Sum of all prime numbers is: {prime_sum}")
        print(f"Sum of all non prime numbers is: {nonprime_sum}")
        break

    num = int(num)

    if num < 0:
        print("Number is negative.")
        continue
    elif num <= 1:
        nonprime_sum += num
        continue
    elif num == 2:
        prime_sum += num
        continue
    elif num % 2 == 0:
        nonprime_sum += num
        continue

    is_prime = True
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            nonprime_sum += num
            is_prime = False
            break

    if is_prime:
        prime_sum += num
