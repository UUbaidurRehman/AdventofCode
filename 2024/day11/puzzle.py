# from collections import deque

# def blink_stones(stones, blinks):
#     stones = deque(stones)  # Use deque for efficient popping and appending
#     for _ in range(blinks):
#         new_stones = deque()
#         while stones:
#             stone = stones.popleft()
#             if stone == 0:
#                 new_stones.append(1)
#             elif len(str(stone)) % 2 == 0:
#                 # Split the stone into two parts
#                 digits = str(stone)
#                 mid = len(digits) // 2
#                 left = int(digits[:mid])
#                 right = int(digits[mid:])
#                 new_stones.extend([left, right])
#             else:
#                 # Multiply by 2024
#                 new_stones.append(stone * 2024)
#         stones = new_stones
#     return len(stones)

# # Initial stone arrangement
# stones = [9694820, 93, 54276, 1304, 314, 664481, 0, 4]

# # Number of blinks
# blinks = 25

# # Calculate the number of stones after 25 blinks
# result = blink_stones(stones, blinks)
# print(result)
from collections import Counter

def process_stone(stone):
    """Apply the transformation rules to a single stone."""
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        digits = str(stone)
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        return [left, right]
    else:
        return [stone * 2024]

def blink_stones_optimized(stones, blinks):
    """Simulate the blinking process for a large number of iterations."""
    # Use a Counter to track the number of each type of stone
    stone_counts = Counter(stones)
    
    for i in range(blinks):
        new_counts = Counter()
        # print(new_counts)
        for stone, count in stone_counts.items():
            # print(stone, end= " okay ")
            # print(count)
            transformed_stones = process_stone(stone)
            # print(new_counts)
            # print(f"*****{transformed_stones}*****")
            for new_stone in transformed_stones:
                new_counts[new_stone] += count
        stone_counts = new_counts
        # print (f"##{new_counts}##")
        # print (f"------blink-No: {i} -------------No.-stones---{stone_counts}---------------------")

    # Total number of stones
    return sum(stone_counts.values())

# Initial stone arrangement
stones = [9694820, 93, 54276, 1304, 314, 664481, 0, 4]

# Number of blinks
blinks = 1

# Calculate the number of stones after 75 blinks
result = blink_stones_optimized(stones, blinks)
print(result)
