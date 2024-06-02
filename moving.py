r1, r2, r3 = int(input()), int(input()), int(input())
free_space = r1 * r2 * r3

while True:
    box_moved = input()
    if box_moved != "Done":
        box_moved = int(box_moved)
        free_space -= box_moved
        if free_space <= 0:
            print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
            break
    elif box_moved == "Done":
        print(f"{free_space} Cubic meters left.")
        break
