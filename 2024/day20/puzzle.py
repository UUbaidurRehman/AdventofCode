from collections import deque

def solve_part2():
    input_filename = "input.txt"
    with open(input_filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Find S and E
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def is_track(ch):
        return ch in ('.', 'S', 'E')

    # BFS to find shortest dist from a given start point
    def bfs(start_pos):
        dist = [[float('inf')] * cols for _ in range(rows)]
        sr, sc = start_pos
        dist[sr][sc] = 0
        queue = deque([start_pos])
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if is_track(grid[nx][ny]) and dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        return dist

    dist_from_S = bfs(start)
    dist_from_E = bfs(end)

    normal_dist = dist_from_S[end[0]][end[1]]
    if normal_dist == float('inf'):
        # No normal path means no cheats can help
        print(0)
        return

    # We'll find cheats that can last up to 20 steps.
    # For each track cell reachable from S, we do a BFS ignoring walls (up to 20 steps)
    # to find reachable track cells.
    # This BFS will track how many steps have been taken.
    # We only care about shortest ignoring-wall distance ≤ 20 to each cell.

    cheats = set()

    # Pre-collect all track cells that are reachable from S to limit starting points
    track_cells_from_S = [(x,y) for x in range(rows) for y in range(cols) 
                          if dist_from_S[x][y] != float('inf') and is_track(grid[x][y])]

    for (sx, sy) in track_cells_from_S:
        # BFS ignoring walls from (sx, sy) up to distance 20
        dist_ignore_walls = [[float('inf')] * cols for _ in range(rows)]
        dist_ignore_walls[sx][sy] = 0
        q = deque([(sx, sy)])
        while q:
            x, y = q.popleft()
            d = dist_ignore_walls[x][y]
            if d == 20:
                # Can't go further than 20 steps
                continue
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    # ignoring walls, so no condition except bounds
                    if dist_ignore_walls[nx][ny] > d + 1:
                        dist_ignore_walls[nx][ny] = d+1
                        q.append((nx, ny))

        # Now check all track cells reachable within ≤20 steps
        base_dist = dist_from_S[sx][sy]
        for fx in range(rows):
            for fy in range(cols):
                d = dist_ignore_walls[fx][fy]
                if d != float('inf') and 1 <= d <= 20 and is_track(grid[fx][fy]):
                    # We have a potential cheat from (sx, sy) to (fx, fy) of length d
                    if dist_from_E[fx][fy] != float('inf'):
                        route_with_cheat = base_dist + d + dist_from_E[fx][fy]
                        saving = normal_dist - route_with_cheat
                        if saving >= 100:
                            cheats.add((sx, sy, fx, fy))

    print(len(cheats))

if __name__ == "__main__":
    solve_part2()

# --------------------------------------------------------------------------------------------------------------
# from collections import deque

# def solve():
#     # The file name is stored in a variable, let's assume it's input_filename
#     input_filename = "input.txt"

#     # Read the map from the file
#     with open(input_filename, 'r') as f:
#         grid = [list(line.rstrip('\n')) for line in f]

#     rows = len(grid)
#     cols = len(grid[0])

#     # Find S and E
#     start = None
#     end = None
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'S':
#                 start = (r, c)
#             elif grid[r][c] == 'E':
#                 end = (r, c)

#     # Directions for movement
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]

#     def is_track(ch):
#         # 'S', 'E', '.' are considered track
#         return ch in ('.', 'S', 'E')

#     # BFS function to find shortest dist from a given start point
#     def bfs(start_pos):
#         dist = [[float('inf')] * cols for _ in range(rows)]
#         sr, sc = start_pos
#         dist[sr][sc] = 0
#         queue = deque([start_pos])
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in directions:
#                 nx, ny = x+dx, y+dy
#                 if 0 <= nx < rows and 0 <= ny < cols:
#                     if is_track(grid[nx][ny]) and dist[nx][ny] > dist[x][y] + 1:
#                         dist[nx][ny] = dist[x][y] + 1
#                         queue.append((nx, ny))
#         return dist

#     # Get dist_from_S and dist_from_E
#     dist_from_S = bfs(start)
#     dist_from_E = bfs(end)

#     # Normal shortest path from S to E
#     normal_dist = dist_from_S[end[0]][end[1]]
#     if normal_dist == float('inf'):
#         # If there's no normal path from S to E, then no cheat can help.
#         print(0)
#         return

#     # We'll find all valid cheats.
#     # A cheat:
#     #   Start from a track cell 'start_node'
#     #   Perform 1 or 2 steps ignoring walls
#     #   End at a track cell 'end_node'
#     #   route_with_cheat = dist_from_S[start_node] + cheat_length + dist_from_E[end_node]
#     #   savings = normal_dist - route_with_cheat
#     # We count how many have savings >= 100

#     cheats = set()  # to store (sx, sy, ex, ey)
#     count = 0

#     for x in range(rows):
#         for y in range(cols):
#             # Only consider this cell as a cheat start if it's reachable and is track
#             if dist_from_S[x][y] == float('inf'):
#                 continue
#             if not is_track(grid[x][y]):
#                 continue

#             base_dist = dist_from_S[x][y]
#             # 1-step cheat
#             for dx, dy in directions:
#                 nx, ny = x+dx, y+dy
#                 if 0 <= nx < rows and 0 <= ny < cols:
#                     # ignoring walls for the cheat step, so no condition here except inside bounds
#                     if is_track(grid[nx][ny]):
#                         # end_node = (nx, ny)
#                         # Check if end_node is reachable from E
#                         if dist_from_E[nx][ny] != float('inf'):
#                             route_with_cheat = base_dist + 1 + dist_from_E[nx][ny]
#                             saving = normal_dist - route_with_cheat
#                             if saving >= 100:
#                                 # record cheat
#                                 if (x,y,nx,ny) not in cheats:
#                                     cheats.add((x,y,nx,ny))

#             # 2-step cheat
#             # For each direction for the first step:
#             for dx1, dy1 in directions:
#                 ix, iy = x+dx1, y+dy1
#                 if 0 <= ix < rows and 0 <= iy < cols:
#                     # first step can go through walls as well
#                     # second step:
#                     for dx2, dy2 in directions:
#                         fx, fy = ix+dx2, iy+dy2
#                         if 0 <= fx < rows and 0 <= fy < cols:
#                             # final cell must be track
#                             if is_track(grid[fx][fy]):
#                                 if dist_from_E[fx][fy] != float('inf'):
#                                     route_with_cheat = base_dist + 2 + dist_from_E[fx][fy]
#                                     saving = normal_dist - route_with_cheat
#                                     if saving >= 100:
#                                         if (x,y,fx,fy) not in cheats:
#                                             cheats.add((x,y,fx,fy))

#     # Count the number of cheats with at least 100 saving
#     print(len(cheats))


# if __name__ == "__main__":
#     solve()