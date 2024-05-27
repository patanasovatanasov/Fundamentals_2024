string_given = input()
string_given = string_given.lower()
counter = 0

if "sun" in string_given:
    counter += string_given.count("sun")
if "water" in string_given:
    counter += string_given.count("water")
if "fish" in string_given:
    counter += string_given.count("fish")
if "sand" in string_given:
    counter += string_given.count("sand")
print(counter)