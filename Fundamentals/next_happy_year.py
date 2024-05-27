this_year = int(input())

while True:
    this_year += 1
    digits_set = {int(digit) for digit in str(this_year)}
    if len(digits_set) == len(str(this_year)):
        print(this_year)
        break
