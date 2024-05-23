command = ''
while True:
    command = input()
    if command == "SoftUni":
        continue
    if command == "End":
        break
    for chars in range(len(command)):
        print(f"{command[chars] * 2}", end="")
    print("")
