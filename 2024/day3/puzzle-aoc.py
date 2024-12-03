# import pyperclip
import re

# def printc(s):
#     print(s)
#     pyperclip.copy(str(s))

# Function to extract numbers from mul instructions
def nums(s):
    """Extract two numbers from a string in the format 'mul(a,b)'."""
    match = re.match(r"mul\((\d+),(\d+)\)", s)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

# Read the input file
with open("input.txt") as f:
    s = f.read().strip()

ans = 0

# Find valid instructions: mul(a,b), do(), don't()
x = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s)

g = True  # Indicates if multiplication instructions are enabled

# Process each instruction
for y in x:
    if y == "do()":
        g = True
    elif y == "don't()":
        g = False
    else:
        if g:
            a, b = nums(y)
            if a is not None and b is not None:
                ans += a * b

# Output the final result
print(ans)
# printc(ans)





# from adventofcode import *
# import pyperclip 
# import sys
# import re
# # sys.setrecursionlimit(1000000)
# # ans = res = 0 
# def printc(s):
#     print(s)
#     pyperclip.copy(str(s))

# with open ("input.txt") as f:
#     s = f.read().strip()

# def nums(s):
#     """Extract two numbers from a string in the format 'mul(a,b)'."""
#     match = re.match(r"mul\((\d+),(\d+)\)", s)
#     if match:
#         return int(match.group(1)), int(match.group(2))
#     return None, None

# ans = 0 
# x= re.findall("mul\(\d+,\d+\) | do\(\) | don't \(\)",s)

# g = True 
# for y in x:
#     if y == "do()":
#         g = True
#     elif y == "don't()":
#         g = False
#     else:
#         if g :
#             a,b = nums(y)
#             ans += a*b
# printc(ans)