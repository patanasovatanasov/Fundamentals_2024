first = input()
second = input()
third = input()
counter = 0

askii_begin = ord(first)
askii_end = ord(second)
askii_excl = ord(third)

for f in range(askii_begin, askii_end + 1):
    if f == askii_excl:
        continue
    for s in range(askii_begin, askii_end + 1):
        if s == askii_excl:
            continue
        for t in range(askii_begin, askii_end + 1):
            if t == askii_excl:
                continue
            counter += 1
            print(f"{chr(f)}{chr(s)}{chr(t)}", end=" ")
print(counter)