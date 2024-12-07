# create a function to simulate the porbability of each outcome in a dice roll
from random import randint
from collections import Counter

def simulate_dice_roll(*dices, iterations=1_000_000):
    counter = Counter()
    for _ in range(iterations):
        counter[sum([randint(1, sides) for sides in dices])] += 1

    ordered_counter = dict(counter.most_common())
    for key, value in ordered_counter.items():
        print(f"Value: {key}, value: {round((value / iterations) * 100, 2)}")

simulate_dice_roll(4, 6, 6)