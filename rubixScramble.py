# This is a cube scrambler

import random

moves = ''
side = ['F', 'R', 'U', "B", 'L', 'D']
direc = [" ","'" ]


while len(moves) < 100:
    moves += str(direc[random.randint(0, 1)])
    moves += str(side[random.randint(0, 5)])
    moves += ', '


print(moves)
