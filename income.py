account = 0


while True:
    income = input()
    if income != "NoMoreMoney":
        income = float(income)
        if income > 0:
            account += income
            print(f"Increase: {income:.2f}")
        else:
            print("Invalid operation!")
            break
    else:
        break
print(f"Total: {account:.2f}")