import re

# Specify the path to your file
file_path = "input.txt"

# Read data from the file
with open(file_path, 'r') as file:
    data = file.read().split()

ans = 0

for y, line in enumerate(data):
    for m in re.compile(r"\d+").finditer(line):
        include = False
        for x in range(m.start(), m.end()):
            for y2 in range(y-1, y+2):
                if y2 < 0 or y2 >= len(data):
                    continue
                for x2 in range(x-1, x+2):
                    if x2 < 0 or x2 >= len(line):
                        continue
                    if data[y2][x2] not in (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        include = True
        if include:
            ans += int(m.group())

print(ans)

# def is_part_number(char):
#     return char.isdigit()

# def get_adjacent_numbers(grid, row, col):
#     numbers = []

#     for i in range(row - 1, row + 2):
#         for j in range(col - 1, col + 2):
#             if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i != row or j != col):
#                 if is_part_number(grid[i][j]):
#                     numbers.append(int(grid[i][j]))

#     return numbers

# def sum_adjacent_numbers(grid):
#     total_sum = 0

#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if is_part_number(grid[i][j]):
#                 numbers = get_adjacent_numbers(grid, i, j)
#                 total_sum += sum(numbers)

#     return total_sum

# # Read engine schematic from input file
# with open('input.txt', 'r') as file:
#     engine_schematic = [line.strip() for line in file]

# result = sum_adjacent_numbers(engine_schematic)
# print(result)
