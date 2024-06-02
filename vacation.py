excursion = float(input())
nalichni = float(input())
spend_counter = 0
days = 0

while True:
    doing = input()
    how_much = float(input())
    days += 1
    if doing == "spend":
        if nalichni < how_much:
            nalichni = 0
        else:
            nalichni -= how_much
        spend_counter += 1
        if spend_counter == 5:
            print("You can't save the money.")
            print(days)
            break
    elif doing == "save":
        nalichni += how_much
        if spend_counter > 0:
            spend_counter = 0
        if nalichni >= excursion:
            print(f"You saved the money for {days} days.")
            break
