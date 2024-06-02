from math import ceil

serial = str(input("Ime na seriala: "))
pro_serial = int(input("Prodyljitelnost na epizoda: "))
pro_pochivka = int(input("Prodyljitelnost na pochivkata: "))
obqd = pro_pochivka*0.125
otdih = pro_pochivka*0.25
obshto = pro_pochivka - obqd - otdih
if obshto >= pro_serial:
    print(f"You have enough time to watch {serial} and left with {ceil(obshto - pro_serial)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {ceil(pro_serial - obshto)} more minutes.")