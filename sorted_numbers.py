def sorted_nums(nums_to_sort):
    nums_lst = [eval(x) for x in nums_to_sort]
    nums_lst.sort()
    return nums_lst


nums = input().split()
print(sorted_nums(nums))
