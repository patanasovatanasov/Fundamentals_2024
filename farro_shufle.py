original_deck = input().split()
shuffles = int(input())
deck1 = []
deck2 = []
deck_range = int(len(original_deck) / 2)

for _ in range(shuffles):
    for cards in range(deck_range):
        deck1.append(original_deck[cards])
    for cards in range(deck_range, len(original_deck), 1):
        deck2.append(original_deck[cards])
    original_deck.clear()
    for i in range(deck_range):
        original_deck.append(deck1.pop(0))
        original_deck.append(deck2.pop(0))


print(original_deck)
