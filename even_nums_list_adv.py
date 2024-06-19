numbers = list(map(int, input().split(", ")))
found_inds = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
even_numbers = list(filter(lambda x: x != "no", found_inds))
print(even_numbers)
