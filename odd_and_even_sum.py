def sums(nums):
    odd_sum = 0
    even_sum = 0
    for _ in nums:
        if _ % 2 == 0:
            even_sum += _
        else:
            odd_sum += _
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
numbers_as_integer = [eval(x) for x in number]

print((sums(numbers_as_integer)))