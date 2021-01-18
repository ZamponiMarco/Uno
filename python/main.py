import random

f2 = open('deck.txt', 'w')
colors = ['red', 'green', 'blue', 'yellow']
cards_count = {'0': 1, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, 'reverse': 2, 'stop': 2, 'plus2': 2}
action = {'plus4': 4, 'change': 4}

cards = []

for color in colors:
    for card in cards_count:
        count = cards_count[card]
        for i in range(count):
            cards.append(f"card({card}, {color})")

for card in action:
    count = action[card]
    for i in range(count):
        cards.append(f"card({card}, all)")

random.shuffle(cards)
cards.append('>')

f2.write(" | " . join(cards))
f2.close()
