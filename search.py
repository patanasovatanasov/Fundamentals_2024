n = int(input())
word = input()
lst = []

for i in range(n):
    strings = input()
    lst.append(strings)
print(lst)
for i in range(len(lst) - 1, - 1, - 1):
    searched_word = lst[i]
    if word not in searched_word:
        lst.remove(searched_word)
print(lst)