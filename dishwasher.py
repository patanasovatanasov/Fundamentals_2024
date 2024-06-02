ditergent = 750
ditergent_pieces = int(input())
total_ditergent = ditergent * ditergent_pieces
dish= 5
pot = 15
load_count = 0
total_load_dish = 0
total_load_pot = 0

while True:
    load = input()
    load_count += 1
    if load == "End":
        print(f"Detergent was enough!")
        print(f"{total_load_dish} dishes and {total_load_pot} pots were washed.")
        print(f"Leftover detergent {total_ditergent} ml.")
        break
    elif load_count < 3:
        load = int(load)
        total_load_dish += load
        total_ditergent -= load * dish
        if total_ditergent < 0:
            print(f"Not enough detergent, {abs(total_ditergent)} ml. more necessary!")
            break
    elif load_count == 3:
        load_count = 0
        load = int(load)
        total_load_pot += load
        total_ditergent -= load * pot
        if total_ditergent < 0:
            print(f"Not enough detergent, {abs(total_ditergent)} ml. more necessary!")
            break
