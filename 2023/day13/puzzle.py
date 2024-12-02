import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque

def process_grid(grid):
    ans = 0
    R = len(grid)
    C = len(grid[0])

    # vertical symmetry
    for c in range(C - 1):
        badness = 0
        for dc in range(C):
            left = c - dc
            right = c + 1 + dc
            if 0 <= left < right < C:
                for r in range(R):
                    if grid[r][left] != grid[r][right]:
                        badness += 1
        if badness == (1 if part2 else 0):
            ans += c + 1

    for r in range(R - 1):
        badness = 0
        for dr in range(R):
            up = r - dr
            down = r + 1 + dr
            if 0 <= up < down < R:
                for c in range(C):
                    if grid[up][c] != grid[down][c]:
                        badness += 1
        if badness == (1 if part2 else 0):
            ans += 100 * (r + 1)

    return ans

# File path
filename = r"input.txt"

with open(filename) as file:
    grids = []
    current_grid = []

    for line in file:
        if line.strip() == '':
            grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append([c for c in line.strip()])

    if current_grid:  # Add the last grid if file doesn't end with a blank line
        grids.append(current_grid)

for part2 in [False, True]:
    total_ans = 0
    for G in grids:
        total_ans += process_grid(G)
    print(total_ans)