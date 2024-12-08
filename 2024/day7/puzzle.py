# # import math
# import sys
# from itertools import product

# sys.setrecursionlimit(10**6)

# with open("input.txt") as f:
#     s = [line.strip() for line in f.read().strip().split("\n")]

# ans = 0

# for line in s:
#     # Split the line and remove the colon from the first element
#     parts = line.split()
#     parts[0] = parts[0].replace(":", "")  # Remove colon from the sum part
    
#     l = list(map(int, parts))
#     n = l.pop(0)  # Test value
#     check = l.pop(0)  # Target value
#     good = False
    
#     for opmask in range(1 << (len(l) - 1)):
#         result = l[0]
        
#         for i in range(len(l) - 1):
#             if (opmask >> i) & 1:
#                 result *= l[i + 1]
#             else:
#                 result += l[i + 1]
        
#         if result == check:
#             good = True
#             break
    
#     ans += good * n

# print(ans)


from itertools import product

# Read input file
with open("input.txt", "r") as file:
    data = file.readlines()
def is_valid(target, numbers):
    if len(numbers) == 1:
        return numbers[0] == target
    if is_valid (target, [numbers[0]+numbers[1]] + numbers[2:]):
        return True
    if is_valid (target, [numbers[0] * numbers[1]] + numbers[2:]):
        return True
    if is_valid(target, [int(str(numbers[0])+str(numbers[1]))] + numbers[2:]):
        return True
    return False
    # if len(numbers) == 0:
    #     return target== 0
    # if target == 0:
    #     return False
    # return is_valid(target-numbers[-1], numbers[:-1]) or target % numbers[-1]==0 and is_valid(target//numbers[-1],numbers[:-1])
# Parse input into a list of equations
equations = []
total = 0
for line in data:
    if line.strip():
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.split()))
        equations.append((target, numbers))
        # print(target)
        # print(type(numbers))
        if is_valid(target, numbers):
            total += target
print(total)

# # Function to evaluate an equation
# def evaluate_expression(target, numbers):
#     """
#     Determine if the target can be achieved by placing operators between numbers.
#     Evaluates left-to-right, without precedence.
#     """
#     n = len(numbers)
#     if n == 1:
#         return numbers[0] == target
    
#     # Generate all combinations of operators (+, *)
#     for ops in product("+-*", repeat=n-1):
#         expr = numbers[0]
#         for i in range(1, n):
#             if ops[i-1] == "+":
#                 expr += numbers[i]
#             elif ops[i-1] == "*":
#                 expr *= numbers[i]
#         if expr == target:
#             return True
#     return False

# # Process equations to find valid ones
# valid_equations = []
# for target, numbers in equations:
#     if evaluate_expression(target, numbers):
#         valid_equations.append(target)

# Calculate the total calibration result
# total_calibration_result = sum(valid_equations)

# print(total_calibration_result)
