def smallest_number(a, b, c):
    nums = [int(a), int(b), int(c)]
    sm = min(nums)
    return sm

a, b, c = int(input()), int(input()), int(input())
print(smallest_number(a, b, c))