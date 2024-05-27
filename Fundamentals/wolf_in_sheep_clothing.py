animals = input()

animal_list = animals.split(", ")

for animal in range(len(animal_list)):
    if animal_list[animal] == "wolf":
        if 0 <= animal < len(animal_list) - 1:
            print(f"Oi! Sheep number {len(animal_list) - (animal + 1)}! You are about to be eaten by a wolf!")
        elif animal == len(animal_list) - 1:
            print(f"Please go away and stop eating my sheep")
