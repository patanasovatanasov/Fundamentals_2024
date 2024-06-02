total_sum_expected = int(input())
type_counter = 0
cs = 0
cc = 0
pays_counter_cs, pays_counter_cc = 0, 0

while True:
    item_price = input()
    if item_price == "End":
        print("Failed to collect required money for charity.")
        break
    item_price = int(item_price)

    if type_counter == 0:
        type_counter = 1
        if item_price > 100:
            print("Error in transaction!")
        else:
            cs += item_price
            pays_counter_cs += 1
            print("Product sold!")
    elif type_counter == 1:
        type_counter = 0
        if item_price < 10:
            print("Error in transaction!")
        else:
            cc += item_price
            pays_counter_cc += 1
            print("Product sold!")
    total = cs + cc
    if total >= total_sum_expected:
        print(f"Average CS: {cs / pays_counter_cs:.2f}")
        print(f"Average CC: {cc / pays_counter_cc:.2f}")
        break