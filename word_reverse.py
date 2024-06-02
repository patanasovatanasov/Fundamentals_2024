word = str(input())
rev_word = ""

for letters in range(len(word) - 1, -1, -1):
    rev_word += word[letters]
print(rev_word)