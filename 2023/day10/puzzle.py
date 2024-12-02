# with open('input.txt') as file:
#     lines  = file.read().strip().split('\n')
# answer1 = 0

# grid = {}
# grid2 = {}

# for line_num, line in enumerate(lines):
#     for ch_num, ch in enumerate(line):
#         c = (line_num, ch_num)
#         if ch == 'S':
#             pos = c
#         grid[c] = ch
# grid_rows = line_num
# grid_cols = ch_num

# dird = {'F': {(-1, 0): (0, 1), (0, -1): (1, 0)},
#         '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
#         'J': {(1, 0): (0, -1), (0, 1): (-1, 0)},
#         'L': {(0, -1): (-1, 0), (1, 0): (0, 1)},
#         '|': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
#         '-': {(0, 1): (0, 1), (0, -1): (0, -1)}}

# done = False

# cw_dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
# ccw_dirs = list(reversed(cw_dirs))

# # follow the pipe
# answer1 = 0
# next_dir = None
# while True:
#     # print(f'pos = {pos}')
#     if next_dir is None:
#         for next_dir in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#             dr, dc = next_dir
#             pos2 = (pos[0]+dr, pos[1]+dc)
#             if pos2 in grid and \
#                grid[pos2] in dird and \
#                next_dir in dird[grid[pos2]]:
#                 start_dir = next_dir
#                 break
#     pos = (next_dir[0]+pos[0], next_dir[1]+pos[1])
#     grid2[pos] = grid[pos]
#     answer1 += 1
#     if grid[pos] == 'S':
#         break
#     in_dir = (next_dir[0] * -1, next_dir[1] * -1)
#     in_dirn = ccw_dirs.index(in_dir)
#     next_dir = dird[grid[pos]][next_dir]
#     while True:
#         # mark the empty spaces to right of the pipe
#         in_dirn = (in_dirn + 1) % 4
#         if ccw_dirs[in_dirn] == next_dir:
#             break
#         pos2 = (pos[0]+ccw_dirs[in_dirn][0], pos[1]+ccw_dirs[in_dirn][1])
#         if pos2 not in grid2:
#             grid2[pos2] = '@'
# # flood fill the marked inside regions
# done = False
# while not done:
#     done = True
#     for row in range(grid_rows):
#         for col in range(grid_cols):
#             if (row, col) in grid2 and grid2[(row, col)] == '@':
#                 for dr, dc in ccw_dirs:
#                     row2 = row+dr
#                     col2 = col+dc
#                     if (row2, col2) not in grid2:
#                         grid2[(row2, col2)] = '@'
#                         done = False
# # print the resulting grid and count the marked spaces
# answer2 = 0
# for row in range(grid_rows):
#     for col in range(grid_cols):
#         if (row, col) in grid2:
#             #print(grid2[(row, col)], end='')
#             if grid2[(row, col)] == '@':
#                 answer2 += 1
#         else:
#             end = '' #print('.', end='')
#     #print('')

# answer1 //= 2

# print(f'answer1 = {answer1}')
# print(f'answer2 = {answer2}')

# import time
# import os

# def run(input_file, is_test, supposed_answer1, supposed_answer2):
#     stopwatch = time.time()

#     with open(input_file, 'r') as file:
#         S = [line.strip() for line in file.readlines()]

#     answer1 = 0
#     answer2 = 0

#     X = [['.' for _ in range(len(S[0]))] for _ in range(len(S))]

#     # Find 'S'
#     x, y = 0, 0
#     ready = False
#     while y < len(S) and not ready:
#         while x < len(S[0]) and not ready:
#             ready = S[y][x] == 'S'
#             if not ready:
#                 x += 1
#         if not ready:
#             x = 0
#             y += 1

#     start = (x, y)
#     direction = 0
#     steps = 0
#     ready = False
#     X[y][x] = 'S'
#     if x < len(S[0]) - 1 and S[y][x + 1] in "-J7":
#         direction = 1
#     elif y > 0 and S[y - 1][x] in "|7F":
#         direction = 2
#     elif x > 0 and S[y][x - 1] in "-FL":
#         direction = 3

#     while not ready:
#         c = '.'
#         if direction == 0:
#             c = S[y + 1][x]
#             if c == 'J':
#                 direction = 3
#             elif c == 'L':
#                 direction = 1
#             y += 1
#         elif direction == 1:
#             c = S[y][x + 1]
#             if c == 'J':
#                 direction = 2
#             elif c == '7':
#                 direction = 0
#             x += 1
#         elif direction == 2:
#             c = S[y - 1][x]
#             if c == 'F':
#                 direction = 1
#             elif c == '7':
#                 direction = 3
#             y -= 1
#         elif direction == 3:
#             c = S[y][x - 1]
#             if c == 'F':
#                 direction = 0
#             elif c == 'L':
#                 direction = 2
#             x -= 1

#         X[y][x] = c
#         ready = c == 'S'
#         steps += 1

#     answer1 = steps // 2

#     for i in range(len(X)):
#         inside = False
#         online = '.'
#         for j in range(len(X[0])):
#             cx = X[i][j]
#             if cx in "|JLF7":
#                 if cx == '|':
#                     inside = not inside
#                 elif cx == 'F':
#                     online = 'F'
#                 elif cx == 'L':
#                     online = 'L'
#                 elif cx == '7' and online == 'L':
#                     inside = not inside
#                 elif cx == 'J' and online == 'F':
#                     inside = not inside
#             elif cx == '.':
#                 if inside:
#                     answer2 += 1

#     elapsed_time = time.time() - stopwatch
#     print("Time in milliseconds:", elapsed_time * 1000)

#     if supposed_answer1 > -1:
#         print(f"Part 1: {answer1}, Expected: {supposed_answer1}, Test: {is_test}")

#     if supposed_answer2 > -1:
#         print(f"Part 2: {answer2}, Expected: {supposed_answer2}, Test: {is_test}")


# run("input.txt", True, 8, 0)
# run("input.txt", True, 4, 1)
# run("input.txt", True, 22, 4)
# run("input.txt", False, 0, 0)




# from typing import List, Tuple, Optional
# from collections import set

# with open('input.txt', 'r') as file:
#     input_str = file.readline().strip()
#     input2_str = file.readline().strip()

# def input_str() -> str:
#     return input_str
#     # return """
#     #     ..F7.
#     #     .FJ|.
#     #     SJ.L7
#     #     |F--J
#     #     LJ...
#     # """

# def input2_str() -> str:
#     return input2_str
#     # return """
#     #     FF7FSF7F7F7F7F7F---7
#     #     L|LJ||||||||||||F--J
#     #     FL-7LJLJ||||||LJL-77
#     #     F--JF--7||LJLJ7F7FJ-
#     #     L---JF-JLJ.||-FJLJJ7
#     #     |F|F-JF---7F7-L7L|7|
#     #     |FFJF7L7F-JF7|JL---7
#     #     7-L-JL7||F7|L7F-7F7|
#     #     L.L7LFJ|||||FJL7||LJ
#     #     L7JLJL-JLJLJL--JLJ.L
#     # """

# def parse_grid(input_str: str) -> List[List[str]]:
#     lines = input_str.strip().split('\n')
#     grid = [['.' + line + '.' for line in map(str.strip, lines)]]
#     grid.insert(0, ['.' for _ in range(len(grid[0][0]))])
#     grid.append(['.' for _ in range(len(grid[0][0]))])
#     return [list(line) for line in grid[0]]

# def find_s(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == 'S':
#                 return x, y
#     return None

# def connects(grid: List[List[str]], pos: Tuple[int, int]) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
#     x, y = pos
#     if y >= len(grid) or x >= len(grid[0]):
#         return None
#     item = grid[y][x]
#     if item == '|':
#         return (x, y - 1), (x, y + 1)
#     elif item == '-':
#         return (x - 1, y), (x + 1, y)
#     elif item == 'L':
#         return (x, y - 1), (x + 1, y)
#     elif item == 'J':
#         return (x - 1, y), (x, y - 1)
#     elif item == '7':
#         return (x - 1, y), (x, y + 1)
#     elif item == 'F':
#         return (x, y + 1), (x + 1, y)
#     return None

# def get_pipes(grid: List[List[str]]) -> List[Tuple[int, int]]:
#     s = find_s(grid)
#     curr = s
#     neighbors = [
#         (curr[0] - 1, curr[1]),
#         (curr[0] + 1, curr[1]),
#         (curr[0], curr[1] - 1),
#         (curr[0], curr[1] + 1)
#     ]
#     for n in neighbors:
#         if n == s:
#             continue
#         connect = connects(grid, n)
#         if connect:
#             c1, c2 = connect
#             if c1 == curr or c2 == curr:
#                 curr = n
#                 break
#     pipes = [s]
#     while grid[curr[1]][curr[0]] != 'S':
#         c1, c2 = connects(grid, curr)
#         next_ = c1 if c1 == pipes[-1] else c2
#         pipes.append(curr)
#         curr = next_
#     return pipes

# def search_and_mark(grid: List[List[str]], curr: Tuple[int, int], pipes: set([Tuple[int, int]])) -> List[List[str]]:
#     if curr[1] >= len(grid) or curr[0] >= len(grid[0]):
#         return grid
#     if grid[curr[1]][curr[0]] == 'X':
#         return grid
#     if curr in pipes:
#         return grid
#     neighbors = [
#         (curr[0] - 1, curr[1]),
#         (curr[0] + 1, curr[1]),
#         (curr[0], curr[1] - 1),
#         (curr[0], curr[1] + 1)
#     ]
#     grid[curr[1]][curr[0]] = 'X'
#     for n in neighbors:
#         grid = search_and_mark(grid, n, pipes)
#     return grid

# def count(grid: List[List[str]], c: str) -> int:
#     n = 0
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == c:
#                 n += 1
#     return n

# def part1():
#     input_str_val = input_str()
#     grid = parse_grid(input_str_val)
#     pipes = get_pipes(grid)
#     print(len(pipes) // 2)

# def part2():
#     input2_str_val = input2_str()
#     grid = parse_grid(input2_str_val)
#     s = find_s(grid)
#     pipes = get_pipes(grid)
#     pipe_set = set(pipes)
#     marked_grid = grid
#     prev = (s[0], s[1])
#     points_to_mark = []
#     for i in range(len(pipes)):
#         segment = pipes[i]
#         curr = (segment[0], segment[1])
#         if curr[0] - prev[0] == 1 and curr[1] - prev[1] == 0:
#             points_to_mark.extend([(segment[0], segment[1] + 1), (segment[0] - 1, segment[1] + 1)])
#         elif curr[0] - prev[0] == 0 and curr[1] - prev[1] == 1:
#             points_to_mark.extend([(segment[0] - 1, segment[1] - 1), (segment[0] - 1, segment[1])])
#         elif curr[0] - prev[0] == -1 and curr[1] - prev[1] == 0:
#             points_to_mark.extend([(segment[0], segment[1] - 1), (segment[0] + 1, segment[1] - 1)])
#         elif curr[0] - prev[0] == 0 and curr[1] - prev[1] == -1:
#             points_to_mark.extend([(segment[0] + 1, segment[1]), (segment[0] + 1, segment[1] + 1)])
#         prev = curr
#     for p in points_to_mark:
#         marked_grid = search_and_mark(marked_grid, p, pipe_set)
#     nx = count(marked_grid, 'X')
#     if marked_grid[0][0] == 'X':
#         total = len(marked_grid) * len(marked_grid[0])
#         print(total - nx - len(pipe_set))
#     else:
#         print(nx)

# if __name__ == "__main__":
#     part1()
#     part2()

# from typing import List, Tuple, Optional

# # Renamed conflicting names
# from collections import deque

# with open('input.txt', 'r') as file:
#     input_str = file.readline().strip()
#     input2_str = file.readline().strip()

# def input_str_value() -> str:
#     return input_str

# def input2_str_value() -> str:
#     return input2_str

# def parse_grid(input_str: str) -> List[List[str]]:
#     lines = input_str.strip().split('\n')
#     grid = [['.' + line + '.' for line in map(str.strip, lines)]]
#     grid.insert(0, ['.' for _ in range(len(grid[0][0]))])
#     grid.append(['.' for _ in range(len(grid[0][0]))])
#     return [list(line) for line in grid[0]]

# def find_s(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == 'S':
#                 return x, y
#     return None

# def connects(grid: List[List[str]], pos: Tuple[int, int]) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
#     x, y = pos
#     if y >= len(grid) or x >= len(grid[0]):
#         return None
#     item = grid[y][x]
#     if item == '|':
#         return (x, y - 1), (x, y + 1)
#     elif item == '-':
#         return (x - 1, y), (x + 1, y)
#     elif item == 'L':
#         return (x, y - 1), (x + 1, y)
#     elif item == 'J':
#         return (x - 1, y), (x, y - 1)
#     elif item == '7':
#         return (x - 1, y), (x, y + 1)
#     elif item == 'F':
#         return (x, y + 1), (x + 1, y)
#     return None

# def get_pipes(grid: List[List[str]]) -> List[Tuple[int, int]]:
#     s = find_s(grid)
#     curr = s
#     neighbors = [
#         (curr[0] - 1, curr[1]),
#         (curr[0] + 1, curr[1]),
#         (curr[0], curr[1] - 1),
#         (curr[0], curr[1] + 1)
#     ]
#     for n in neighbors:
#         if n == s:
#             continue
#         connect = connects(grid, n)
#         if connect:
#             c1, c2 = connect
#             if c1 == curr or c2 == curr:
#                 curr = n
#                 break
#     pipes = [s]
#     while grid[curr[1]][curr[0]] != 'S':
#         c1, c2 = connects(grid, curr)
#         next_ = c1 if c1 == pipes[-1] else c2
#         pipes.append(curr)
#         curr = next_
#     return pipes

# def search_and_mark(grid: List[List[str]], curr: Tuple[int, int], pipes: set([Tuple[int, int]])) -> List[List[str]]:
#     if curr[1] >= len(grid) or curr[0] >= len(grid[0]):
#         return grid
#     if grid[curr[1]][curr[0]] == 'X':
#         return grid
#     if curr in pipes:
#         return grid
#     neighbors = [
#         (curr[0] - 1, curr[1]),
#         (curr[0] + 1, curr[1]),
#         (curr[0], curr[1] - 1),
#         (curr[0], curr[1] + 1)
#     ]
#     grid[curr[1]][curr[0]] = 'X'
#     for n in neighbors:
#         grid = search_and_mark(grid, n, pipes)
#     return grid

# def count(grid: List[List[str]], c: str) -> int:
#     n = 0
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == c:
#                 n += 1
#     return n

# def part1():
#     input_str_val = input_str_value()
#     grid = parse_grid(input_str_val)
#     pipes = get_pipes(grid)
#     print(len(pipes) // 2)

# def part2():
#     input2_str_val = input2_str_value()
#     grid = parse_grid(input2_str_val)
#     s = find_s(grid)
#     pipes = get_pipes(grid)
#     pipe_set = set(pipes)
    
#     # Corrected the assignment of marked_grid
#     marked_grid = [row.copy() for row in grid]
    
#     prev = (s[0], s[1])
#     points_to_mark = []
#     for i in range(len(pipes)):
#         segment = pipes[i]
#         curr = (segment[0], segment[1])
#         if curr[0] - prev[0] == 1 and curr[1] - prev[1] == 0:
#             points_to_mark.extend([(segment[0], segment[1] + 1), (segment[0] - 1, segment[1] + 1)])
#         elif curr[0] - prev[0] == 0 and curr[1] - prev[1] == 1:
#             points_to_mark.extend([(segment[0] - 1, segment[1] - 1), (segment[0] - 1, segment[1])])
#         elif curr[0] - prev[0] == -1 and curr[1] - prev[1] == 0:
#             points_to_mark.extend([(segment[0], segment[1] - 1), (segment[0] + 1, segment[1] - 1)])
#         elif curr[0] - prev[0] == 0 and curr[1] - prev[1] == -1:
#             points_to_mark.extend([(segment[0] + 1, segment[1]), (segment[0] + 1, segment[1] + 1)])
#         prev = curr
#     for p in points_to_mark:
#         marked_grid = search_and_mark(marked_grid, p, pipe_set)
#     nx = count(marked_grid, 'X')
#     if marked_grid[0][0] == 'X':
#         total = len(marked_grid) * len(marked_grid[0])
#         print(total - nx - len(pipe_set))
#     else:
#         print(nx)

# if __name__ == "__main__":
#     part1()
#     part2()
