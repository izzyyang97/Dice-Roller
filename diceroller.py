import random

# To get the dice unicode characters
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌---------┐"
"│         │"
"│         │"
"│         │"
"└_________┘"

dice_art = {
    1: ("┌---------┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└_________┘"),
    2: ("┌---------┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└_________┘"),
    3: ("┌---------┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└_________┘"),
    4: ("┌---------┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└_________┘"),
    5: ("┌---------┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└_________┘"),
    6: ("┌---------┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└_________┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# This gets the following dice in vertical order, which takes up more space to see the dice.
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#       print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = "")
    print()
# end = serves to be an empty string to prevent long dice art
# Above, the print is to escape interloop, as it prints a new line

for die in dice:
    total += die
print(f"total: {total}")