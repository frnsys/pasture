# Name generator, like the one gfycat uses :)

import random

with open('app/assets/adjectives.txt', 'r') as f:
    adjectives = [l.strip() for l in f.readlines()]

with open('app/assets/animals.txt', 'r') as f:
    animals = [l.strip() for l in f.readlines()]

def random_name():
    """
    There are about 490 million possible combinations here!
    """
    name =  random.choice(adjectives).capitalize()
    name += random.choice(adjectives).capitalize()
    name += random.choice(animals).capitalize()
    return name
