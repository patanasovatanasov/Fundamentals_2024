number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input()
while command != "End":
    tokens = command.split(" ")
    key = tokens[0]
    index_at = tokens[1]
    if key == "add":
        train[-1] += int(index_at)
    elif key == "insert":
        train[int(index_at)] += int(tokens[2])
    elif key == "leave":
        train[int(index_at)] -= int(tokens[2])
    command = input()
print(train)