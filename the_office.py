employee_happiness = map(int, input().split(" "))
factor = int(input())


def score_calculation(x, f):
    multiplied = list(map(lambda xs: xs * f, employee_happiness))
    filtered = list(filter(lambda xs: xs >= (sum(multiplied) / len(multiplied)), multiplied))
    if len(filtered) >= len(multiplied) / 2:
        return f"Score: {len(filtered)}/{len(multiplied)}. Employees are happy!"
    else:
        return f"Score: {len(filtered)}/{len(multiplied)}. Employees are not happy!"


print(score_calculation(employee_happiness, factor))
