names = input().split(", ")
sorted_lst = sorted(names, key=lambda x: (-len(x), x))
print(sorted_lst)