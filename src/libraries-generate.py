import random
cards = ["jack", "queen", "king"]

random.shuffle(cards)
for card in cards:
    print(card)


# Manage probability? 
# Yes

# statistics
import statistics

print(statistics.mean([3, 4, 5, 6, 7]))

# arguments being passed in 

import sys

try: 
    print("Hello, " + ' '.join(sys.argv[1:]) + "!")
except IndexError:
    print("Please type your name on the command line.")

