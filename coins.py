user_input = float(input())
user_input *= 100
coins = 0

while True:
    if user_input >= 200:
        user_input -= 200
        coins += 1
    elif user_input >= 100:
        user_input -= 100
        coins += 1
    elif user_input >= 50:
        user_input -= 50
        coins += 1
    elif user_input >= 20:
        user_input -= 20
        coins += 1
    elif user_input >= 10:
        user_input -= 10
        coins += 1
    elif user_input >= 5:
        user_input -= 5
        coins += 1
    elif user_input >= 2:
        user_input -= 2
        coins += 1
    elif user_input >= 1:
        user_input -= 1
        coins += 1
    elif user_input < 0.01:
        print(coins)
        break