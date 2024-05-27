number = int(input())

for nums in range(1, number + 1):
    sum_of_digits = 0
    digits = nums
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if  (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{nums} -> True")
    else:
        print(f"{nums} -> False")