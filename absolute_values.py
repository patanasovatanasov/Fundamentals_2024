numbers = input().split(" ")
nums = []
for _ in range(len(numbers)):
    nums.append(abs(eval(numbers[_])))
    nums = [float(_) for _ in nums]
print(nums)