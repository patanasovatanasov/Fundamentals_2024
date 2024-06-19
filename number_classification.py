numbers = list(map(int, input().split(", ")))

POSITIVE = [str(x) for x in numbers if x >= 0]
NEGATIVE = [str(x) for x in numbers if x < 0]
EVEN = [str(x) for x in numbers if x % 2 == 0]
ODD = [str(x) for x in numbers if x % 2 != 0]

print(f"Positive: {", ".join(POSITIVE)}")
print(f"Negative: {", ".join(NEGATIVE)}")
print(f"Even: {", ".join(EVEN)}")
print(f"Odd: {", ".join(ODD)}")