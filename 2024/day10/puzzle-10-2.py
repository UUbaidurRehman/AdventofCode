import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict

def read_map(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append([int(ch) for ch in line])
    return grid

def neighbors(r, c, rows, cols):
    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def count_paths(r, c, grid, dp, rows, cols):
    # If already computed, return it
    if dp[r][c] != -1:
        return dp[r][c]

    current_height = grid[r][c]

    # Base case: if height is 9, exactly one trail ends here
    if current_height == 9:
        dp[r][c] = 1
        return 1

    # Otherwise, sum over neighbors with height current_height+1
    total_paths = 0
    next_height = current_height + 1
    for nr, nc in neighbors(r, c, rows, cols):
        if grid[nr][nc] == next_height:
            total_paths += count_paths(nr, nc, grid, dp, rows, cols)

    dp[r][c] = total_paths
    return total_paths

def main():
    grid = read_map("input.txt")
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Identify all trailheads (cells with height 0)
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    # dp[r][c] = number of distinct hiking trails from cell (r, c) to any height-9 cell
    dp = [[-1]*cols for _ in range(rows)]

    total_rating = 0
    for (tr, tc) in trailheads:
        rating = count_paths(tr, tc, grid, dp, rows, cols)
        total_rating += rating

    print(total_rating)

if __name__ == "__main__":
    main()