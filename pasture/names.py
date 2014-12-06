# Name generator, like the one gfycat uses :)

import os
import random

dir = os.path.dirname(os.path.realpath(__file__))

adj_path = os.path.join(dir, 'assets/adjectives.txt')
with open(adj_path, 'r') as f:
    adjectives = [l.strip() for l in f.readlines()]

ani_path = os.path.join(dir, 'assets/animals.txt')
with open(ani_path, 'r') as f:
    animals = [l.strip() for l in f.readlines()]

def random_name():
    """
    There are about 490 million possible combinations here!
    """
    name =  random.choice(adjectives).capitalize()
    name += random.choice(adjectives).capitalize()
    name += random.choice(animals).capitalize()
    return name
