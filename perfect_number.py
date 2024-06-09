def is_perfect(number):
    div_sum = 0
    for x in range(1, number):
        if number % x == 0:
            div_sum += x
    if div_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect(num))