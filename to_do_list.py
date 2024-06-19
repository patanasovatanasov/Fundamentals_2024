notebook = [0] * 10
command = input()

while command != "End":
    tokens = command.split("-")
    prior = int(tokens[0]) - 1
    note = tokens[1]
    notebook.pop(prior)
    notebook.insert(prior, note)
    command = input()

notebook = [note for note in notebook if note != 0]
print(notebook)