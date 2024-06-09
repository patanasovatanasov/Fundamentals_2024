def min_max_sum(some_nums):
    to_int = [eval(x) for x in some_nums]
    min_num = min(to_int)
    max_num = max(to_int)
    sum_num = sum(to_int)
    return f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_num}"


nums = input().split()
print(min_max_sum(nums))