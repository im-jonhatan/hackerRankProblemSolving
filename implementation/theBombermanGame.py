# Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.
# Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell , any valid cells (i±1, j) and (i, j±1) are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.
# Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:
# 1. Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
# 2. After one second, Bomberman does nothing.
# 3. After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
# 4. After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
# 5. Bomberman then repeats steps 3 and 4 indefinitely.
# Note that during every second Bomberman plants bombs, the bombs are planted simultaneously(i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.
# Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after N seconds.
# For example, if the initial grid looks like:
#     ...
#     .O.
#     ...
# it looks the same after the first second. After the second second, Bomberman has placed all his charges:
#     OOO
#     OOO
#     OOO
# At the third second, the bomb in the middle blows up, emptying all surrounding cells:
#     O.O
#     ...
#     O.O

# Function Description
# Complete the bomberMan function in the editory below.
# bomberMan has the following parameter(s):
# - int n: the number of seconds to simulate
# - string grid[r]: an array of strings that represents the grid

# Returns
# - string[r]: n array of strings that represent the grid in its final state

# Input Format
# The first line contains three space-separated integers r, c, and n, The number of rows, columns and seconds to simulate.
# Each of the next r lines contains a row of the matrix as a single string of c characters. The . character denotes an empty cell, and the O character(ascii 79) denotes a bomb.

# Constraints
# 1 ≤ r, c ≤ 200
# 1 ≤ n ≤ 10^9

# Subtask
# 1 ≤ n ≤ 200 for 40% of the maximum score.

# Sample Input
#     STDIN           Function
#     ----- --------
#     6 7 3           r = 6, c = 7, n = 3
#     .......         grid = ['.......', '...O...', '....O..',
#     ...O...                '.......', 'OO.....', 'OO.....']
#     ....O..
#     .......
#     OO.....
#     OO.....

# Sample Output
#     OOO.OOO
#     OO...OO
#     OOO...O
#     ..OO.OO
#     ...OOOO
#     ...OOOO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomberMan(n: int, grid: list) -> list:
    # Write your code here
    if n in [0, 1]:
        return grid
    elif n % 2 == 0:
        return ['O' * len(x) for x in grid]
    else:
        #replace symbols
        grid = [x.replace('O', '2') for x in grid]
        grid = [x.replace('.', '0') for x in grid]
        #split rows into list
        grid = [list(map(int, list(x))) for x in grid]

        R = len(grid)
        C = len(grid[0])
        t = 1
        while t < 4 + n % 4:
            t += 1
            #each second check whole grid
            destroyed = []  # for location of cells that will explode
            for r in range(R):
                for c in range(C):
                    #decrease bomb timer (simultaneously with either planting or explosion)
                    if grid[r][c] > 0:
                        grid[r][c] -= 1

                    #plant
                    if t % 2 == 0 and grid[r][c] == 0:
                        grid[r][c] = 3

                    #explode
                    elif grid[r][c] == 0:
                        destroyed.append([r, c])
                        if r < R-1:
                            destroyed.append([r+1, c])
                        if r > 0:
                            destroyed.append([r-1, c])
                        if c < C-1:
                            destroyed.append([r, c+1])
                        if c > 0:
                            destroyed.append([r, c-1])
            if destroyed:
                grid = [[2] * len(x) for x in grid]
                for r, c in destroyed:
                    grid[r][c] = 0

        #convert lists to strings
        grid = [''.join(list(map(str, x))) for x in grid]
        #replace symbols
        grid = [x.replace('2', 'O') for x in grid]
        grid = [x.replace('0', '.') for x in grid]

        return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
