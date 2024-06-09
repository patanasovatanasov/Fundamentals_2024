def even_nums(d):
    if d % 2 == 0:
        return True
    else:
        return False


numbers = input().split(" ")

int_nums = [eval(n) for n in numbers]

filtered = filter(even_nums, int_nums)
filtered = list(filtered)
print(filtered)
