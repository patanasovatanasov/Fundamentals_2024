n = int(input())

for codes in range(1, n + 1):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88:
        print("GREAT!")
    elif code > 88:
        print("Bye.")
