the_animals = input()
animals = the_animals.split(", ")

for _ in range(len(animals)):
    print(enumerate(animals))
    if animals[_] == "wolf":
        if _ == 0:
            print(f"Oi! Sheep number {_ + len(animals) - 1}! You are about to be eaten by a wolf!")
        elif _ == len(animals) - 1:
            print(f"Please go away and stop eating my sheep")
        elif _ > 0:
            print(f"Oi! Sheep number {_ + 2}! You are about to be eaten by a wolf!")
