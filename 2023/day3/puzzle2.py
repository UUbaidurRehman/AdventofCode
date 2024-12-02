import numpy as np

data = open('input2.txt').read().split('\n')

# Find the length of the longest row
max_length = max(len(row) for row in data)

# Pad the shorter rows to have the same length
data_padded = [row.ljust(max_length, '.') for row in data]

# Convert to NumPy array
schematic = np.array([list(row) for row in data_padded], dtype=np.dtype(str))
schematic = np.pad(schematic, 1, mode='constant', constant_values=['.'])

# import numpy as np

# data = open('input2.txt').read().split('\n')
# schematic = np.array([list(row) for row in data], dtype=np.dtype(str))
# schematic = np.pad(schematic, 1, mode='constant', constant_values=['.'])

def has_adjacent_symbol(row, col, length):
    section = schematic[row-1:row + 2, col-1:col + length + 1]
    top = np.all(section[0, :] == '.')
    bottom = np.all(section[2, :] == '.')
    left = np.all(section[:, 0] == '.')
    right = np.all(section[:, -1] == '.')
    return not all([top, bottom, left, right])

shape = schematic.shape
total = 0
gears = []

for row in range(shape[0]):
    col = 0
    while col < shape[1]:
        if ''.join(schematic[row, col:col+3]).isnumeric():
            gears.append([row, col, 3])
            col += 3
        elif ''.join(schematic[row, col:col+2]).isnumeric():
            gears.append([row, col, 2])
            col += 2
        elif ''.join(schematic[row, col:col+1]).isnumeric():
            gears.append([row, col, 1])
            col += 1
        else:
            col += 1

gears = [[row, col, length] for row, col, length in gears if has_adjacent_symbol(row, col, length)]
answer_part1 = sum([int(''.join(schematic[row, col:col+length])) for row, col, length in gears])
print(f'Part 1: {answer_part1}')

stars = [[row, col] for row in range(shape[0]) for col in range(shape[1]) if schematic[row, col] == '*']
gear_ratios = 0

for row_star, col_star in stars:
    neighbors = [[r, c, l] for r, c, l in gears if r - 1 <= row_star <= r + 1 and c - 1 <= col_star <= c + l]
    if len(neighbors) == 2:
        values = [int(''.join(schematic[row, col:col+length])) for row, col, length in neighbors]
        gear_ratios += values[0] * values[1]

print(f'Part 2: {gear_ratios}')