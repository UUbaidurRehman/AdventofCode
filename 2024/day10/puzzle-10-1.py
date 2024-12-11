from collections import deque

def read_map(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append([int(ch) for ch in line])
    return grid

def neighbors(r, c, rows, cols):
    # Returns the up/down/left/right neighbors within bounds
    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def find_trailhead_scores(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Identify all trailheads (cells with height 0)
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    total_score = 0

    for start_r, start_c in trailheads:
        # BFS or DFS to find all reachable 9-cells
        visited = set()
        queue = deque()
        queue.append((start_r, start_c))
        visited.add((start_r, start_c))

        # Set to store reachable 9 cells
        reachable_nines = set()

        while queue:
            r, c = queue.popleft()
            current_height = grid[r][c]

            # If we have reached height 9, record the cell
            if current_height == 9:
                reachable_nines.add((r, c))
                # We do not continue further from a height 9 cell, 
                # as the path cannot go beyond 9 in this problem.

            else:
                # Look for neighbors with height exactly current_height + 1
                next_height = current_height + 1
                for nr, nc in neighbors(r, c, rows, cols):
                    if (nr, nc) not in visited and grid[nr][nc] == next_height:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # The trailhead's score is how many unique 9-cells were reached
        trailhead_score = len(reachable_nines)
        total_score += trailhead_score

    return total_score

if __name__ == "__main__":
    grid = read_map("input.txt")
    result = find_trailhead_scores(grid)
    print(result)