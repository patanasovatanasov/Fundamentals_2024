number_of_orders = int(input())
price, total_price = 0, 0

for orders in range(1, number_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    caps_per_day = int(input())
    if not 0.01 <= capsule_price <= 100.00 or not 1 <= days <= 31 or not 1 <= caps_per_day <= 2000:
        continue
    price = capsule_price * days * caps_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")