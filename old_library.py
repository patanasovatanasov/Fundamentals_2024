wanted = input()
counter = 0

while True:
    book = input()
    if book == wanted:
        print(f"You checked {counter} books and found it.")
        break
    elif book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    else:
        counter += 1
        continue
