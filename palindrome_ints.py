def is_palindrome(some_nums):
    if some_nums == some_nums[::-1]:
        return True
    else:
        return False


nums = input().split(", ")
for num in nums:
    print(is_palindrome(num))