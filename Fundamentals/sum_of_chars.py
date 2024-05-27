number_of_chars = int(input())
sum_of_chars = 0
for char in range(number_of_chars):
    new_char = input()
    sum_of_chars += ord(new_char)

print(f"The sum equals: {sum_of_chars}")