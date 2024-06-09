first_char = input()
end_char = input()
chars = []
for char in range(ord(first_char) + 1, ord(end_char)):
    chars.append(chr(char))
print(" ".join(chars))