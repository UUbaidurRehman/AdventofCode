def check_word(grid, x, y, dx, dy, word, rows, cols):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
            return False
    return True

def count_XMAS(grid, rows, cols):
    target_word = "XMAS"
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal-right-down
        (1, -1),  # Diagonal-left-down
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal-left-up
        (-1, 1)   # Diagonal-right-up
    ]

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if check_word(grid, r, c, dx, dy, target_word, rows, cols):
                    count += 1
    return count

def count_all_XMAS_patterns(grid, rows, cols):
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            center = grid[r][c]
            top_left = grid[r - 1][c - 1]
            top_right = grid[r - 1][c + 1]
            bottom_left = grid[r + 1][c - 1]
            bottom_right = grid[r + 1][c + 1]

            if center == 'A':
                # Pattern 1: M.S
                if top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S':
                    count += 1
                # Pattern 2: S.M
                if top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M':
                    count += 1
                # Pattern 3: M.M
                if top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S':
                    count += 1
                # Pattern 4: S.S
                if top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M':
                    count += 1

    return count

def main():
    file_path = "input_file.txt"

    # Read the grid from the file
    try:
        with open(file_path, 'r') as file:
            grid = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: Unable to open file.")
        return

    rows, cols = len(grid), len(grid[0])

    # Count occurrences of "XMAS"
    xmas_count = count_XMAS(grid, rows, cols)
    print(f"Count of XMAS: {xmas_count}")

    # Count all X-MAS patterns
    xmas_patterns = count_all_XMAS_patterns(grid, rows, cols)
    print(f"Total X-MAS patterns: {xmas_patterns}")

if __name__ == "__main__":
    main()




# import sys
# import re
# from collections import defaultdict, Counter
# import pyperclip as pc

# def pr(s):
#     print(s)
#     pc.copy(s)

# sys.setrecursionlimit(10**6)
# infile = sys.argv[1] if len(sys.argv) > 2 else 'input_file.txt'
# ans = 0
# D = open(infile).read().strip()

# G = D.split('\n')
# R = len(G)

# C = len(G[0])

# for r in range(R):
#     for c in range(C):
#         if c + 3 < C and G[r][c] == 'X' and G[r][c + 1] == 'M' and G[r][c + 2] == 'A' and G[r][c + 3] == 'S':
#             ans += 1
#         if r + 3 < R and G[r][c] == 'X' and G[r + 1][c] == 'M' and G[r + 2][c] == 'A' and G[r + 3][c] == 'S':
#             ans += 1
#         if r + 3 < R and c + 3 < C and G[r][c] == 'X' and G[r + 1][c + 1] == 'M' and G[r + 2][c + 2] == 'A' and G[r + 3][c + 3] == 'S':
#             ans += 1
#         if c + 3 < C and r + 3 < R and G[r][c] == 'X' and G[r + 1][c + 1] == 'M' and G[r + 2][c + 2] == 'S' and G[r + 3][c + 3] == 'X':
#             ans += 1
#         if c + 3 < C and r - 3 >= 0 and G[r][c] == 'S' and G[r - 1][c + 1] == 'M' and G[r - 2][c + 2] == 'A' and G[r - 3][c + 3] == 'X':
#             ans += 1
#         if r - 3 >= 0 and c + 3 < C and G[r][c] == 'S' and G[r - 1][c + 1] == 'M' and G[r - 2][c + 2] == 'A' and G[r - 3][c + 3] == 'S':
#             ans += 1

# pr(ans)
