number = int(input())
numbers = str(number)
nums_int = []

for nums in range(len(numbers)):
    nums_int.append(numbers[nums])
nums_int.sort(reverse=True)
for n in nums_int:
    print(n, end='')
