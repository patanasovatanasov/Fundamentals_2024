n = int(input())
count = 0
suma = 0

for _ in range(n):
    inp = float(input())
    suma += inp
    count += 1

print(f"{suma / count:.2f}")