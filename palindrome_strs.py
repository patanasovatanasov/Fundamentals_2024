words = input().split(" ")
searched_word = input()
palindromes = []

for w in words:
    if w == "".join(reversed(w)):
        palindromes.append(w)

print(f"{palindromes}")
print(f"Found palindrome {words.count(searched_word)} times")