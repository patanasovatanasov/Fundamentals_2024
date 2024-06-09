def calculations(operator, number1, number2):
    if operator == "multiply":
        return int(number1 * number2)
    elif operator == "divide":
        return int(number1 / number2)
    elif operator == "add":
        return int(number1 + number2)
    elif operator == "subtract":
        return int(number1 - number2)

oper = input()
num1 = int(input())
num2 = int(input())
print(calculations(oper, num1, num2))