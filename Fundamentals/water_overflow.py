number_or_orders = int(input())
capacity_left = 255


for orders in range(0, number_or_orders):
    order_given = int(input())
    if capacity_left >= order_given:
        capacity_left -= order_given
    else:
        print(f"Insufficient capacity!")
        continue
print(255 - capacity_left)
