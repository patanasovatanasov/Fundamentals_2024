budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
loaf_price = flour_price + eggs_price + milk_price

colored_egg_counter = 0
loaf_counter = 0

while budget >= loaf_price:
    loaf_counter += 1
    colored_egg_counter += 3
    budget -= loaf_price

    if loaf_counter % 3 == 0:
        colored_egg_counter -= (loaf_counter - 2)

print(
    f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_egg_counter} eggs and {budget:.2f}BGN left.")
