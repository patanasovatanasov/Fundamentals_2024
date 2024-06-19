some_string = input().split(" ")
new_string = [x for x in some_string if len(x) % 2 == 0]

for x in new_string:
    print(x)