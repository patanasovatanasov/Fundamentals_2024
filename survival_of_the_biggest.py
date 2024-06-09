nums = input().split()
nums_int = [eval(i) for i in nums]
n = int(input())
for _ in range(n):
    smallest = min(nums_int)
    nums_int.remove(smallest)
print(", ".join(str(_) for _ in nums_int))
