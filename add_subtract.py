def sum_numbers(n1, n2):
    sum_result = n1 + n2
    return sum_result


def subtract(sum_res, n3):
    sub_result = sum_res - n3
    return sub_result


def add_and_subtract(n1, n2, n3):
    a = sum_numbers(n1, n2)
    b = subtract(a, n3)
    return b


num1 = int(input())
num2 = int(input())
num3 = int(input())


print(add_and_subtract(num1, num2, num3))