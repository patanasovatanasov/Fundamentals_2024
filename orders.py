def order(product, quantity):
    price = 0
    if product == "coffee":
        price = quantity * 1.5
    elif product == "water":
        price = quantity * 1.0
    elif product == "coke":
        price = quantity * 1.4
    elif product == "snacks":
        price = quantity * 2.0
    return f"{price:.2f}"

prod = input()
qua = float(input())

print(order(prod, qua))