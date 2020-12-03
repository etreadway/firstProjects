# This is a cube scrambler

import random

side = ['F', 'R', 'U', "B", 'L', 'D']
prime = [" ","'" ]

moves = ''
while len(moves) < 100:
    moves += str(side[random.randint(0, 5)])
    moves += str(prime[random.randint(0, 1)])
    moves += ', '


print(moves)
