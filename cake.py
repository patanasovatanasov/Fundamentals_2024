cake_h = int(input())
cake_l = int(input())

pieces = cake_l * cake_h
pieces_taken = 0

while True:
    pieces_taken = input()
    if pieces_taken == "STOP":
        if pieces != 0:
            print(f"{pieces} pieces are left.")
            break
    pieces_taken = int(pieces_taken)
    pieces -= pieces_taken
    if pieces <= 0:
        print(f"No more cake left! You need {abs(pieces)} pieces more.")
        break
