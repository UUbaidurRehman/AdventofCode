import sys
import os
import time
from typing import List, Tuple, Dict, Set
from collections import namedtuple

# Direction mappings
DIRECTION_MAP = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}

# Direction offsets: Up, Right, Down, Left
DIRECTION_OFFSETS = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1)   # Left
]

# Struct-like classes for Position and State
Position = namedtuple('Position', ['row', 'col'])
State = namedtuple('State', ['row', 'col', 'direction'])


def parse_grid(file_path: str) -> List[List[str]]:
    """Parses the grid from the given file."""
    grid = []
    with open(file_path, 'r') as infile:
        for line in infile:
            trimmed = line.strip()
            if trimmed:
                grid.append(list(trimmed))

    if not grid:
        raise RuntimeError("The grid is empty.")

    # Ensure all rows have the same length
    cols = len(grid[0])
    for row in grid:
        if len(row) != cols:
            raise RuntimeError("Inconsistent row lengths in the grid.")

    return grid


def find_guard(grid: List[List[str]]) -> Tuple[Position, int]:
    """Finds the guard's starting position and direction."""
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in DIRECTION_MAP:
                guard_pos = Position(r, c)
                guard_dir = DIRECTION_MAP[cell]
                grid[r][c] = '.'  # Clear the starting position
                return guard_pos, guard_dir
    raise RuntimeError("Guard not found in the grid.")


def get_possible_obstructions(grid: List[List[str]], guard_pos: Position) -> List[Position]:
    """Retrieves all possible obstruction positions excluding the guard's starting position and already obstructed cells."""
    possible = [
        Position(r, c)
        for r in range(len(grid))
        for c in range(len(grid[0]))
        if (r != guard_pos.row or c != guard_pos.col) and grid[r][c] == '.'
    ]
    return possible


def simulate_movement(grid: List[List[str]], start_pos: Position, start_dir: int) -> bool:
    """Simulates the guard's movement on the grid."""
    visited_states: Set[State] = set()
    r, c, direction = start_pos.row, start_pos.col, start_dir

    while True:
        current_state = State(r, c, direction)
        if current_state in visited_states:
            return True  # Loop detected
        visited_states.add(current_state)

        dr, dc = DIRECTION_OFFSETS[direction]
        new_r, new_c = r + dr, c + dc

        # Check boundaries
        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
            return False  # Guard exits the grid

        if grid[new_r][new_c] == '#':
            # Turn right if obstacle ahead
            direction = (direction + 1) % 4
        else:
            # Move forward
            r, c = new_r, new_c


def count_distinct_positions_visited(grid: List[List[str]], guard_pos: Position, guard_dir: int) -> int:
    """Counts the number of distinct positions visited by the guard without any obstructions."""
    visited_positions: Set[Position] = {guard_pos}

    current_pos = guard_pos
    current_dir = guard_dir

    while True:
        dr, dc = DIRECTION_OFFSETS[current_dir]
        new_r, new_c = current_pos.row + dr, current_pos.col + dc

        # Check boundaries
        if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
            break  # Guard exits the mapped area

        if grid[new_r][new_c] == '#':
            # Turn right if obstacle ahead
            current_dir = (current_dir + 1) % 4
        else:
            # Move forward
            current_pos = Position(new_r, new_c)
            visited_positions.add(current_pos)

    return len(visited_positions)


def count_obstruction_positions(grid: List[List[str]], guard_pos: Position, guard_dir: int):
    """Counts the number of obstruction positions that cause the guard to loop indefinitely."""
    total_start_time = time.time()

    possible_obstructions = get_possible_obstructions(grid, guard_pos)

    print("time, denominator")
    print(f"{time.time() - total_start_time:.9f} {len(possible_obstructions)}")

    print("batch, batch time, cumulative time")

    loop_count = 0
    total = len(possible_obstructions)

    batch_size = 1000
    cumulative_time = 0

    for idx, obstruction in enumerate(possible_obstructions, start=1):
        grid[obstruction.row][obstruction.col] = '#'  # Place obstruction

        if simulate_movement(grid, guard_pos, guard_dir):
            loop_count += 1

        grid[obstruction.row][obstruction.col] = '.'  # Remove obstruction

        if idx % batch_size == 0 or idx == total:
            batch_time = time.time() - total_start_time - cumulative_time
            cumulative_time += batch_time
            print(f"{idx} {batch_time:.9f} {cumulative_time:.9f}")

    total_time = time.time() - total_start_time

    print("answer, answer time")
    print(f"{loop_count} {total_time:.9f}")


if __name__ == "__main__":
    file_path = "input.txt" 
    try:
        grid = parse_grid(file_path)
        guard_pos, guard_dir = find_guard(grid)

        distinct_positions = count_distinct_positions_visited(grid, guard_pos, guard_dir)
        print(f"Number of distinct positions visited: {distinct_positions}")

        count_obstruction_positions(grid, guard_pos, guard_dir)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
