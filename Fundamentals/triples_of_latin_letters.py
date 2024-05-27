num_of_letters = int(input())

for first in range(0, num_of_letters):
    for second in range(0, num_of_letters):
        for third in range(0, num_of_letters):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")
            