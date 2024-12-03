import re

def process_corrupted_memory(memory):
    # Regex patterns for valid instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    mul_enabled = True  # `mul` instructions start enabled
    total_sum = 0

    # Scan through the memory for instructions
    for instruction in re.finditer(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', memory):
        match = instruction.group(0)

        if do_pattern.fullmatch(match):
            mul_enabled = True
        elif dont_pattern.fullmatch(match):
            mul_enabled = False
        elif mul_pattern.fullmatch(match):
            if mul_enabled:
                x, y = map(int, mul_pattern.match(match).groups())
                total_sum += x * y

    return total_sum


# memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# test = process_corrupted_memory(memory)
# print(test)
result = 0
# Example usage
file_path = "input.txt"
with open(file_path, 'r') as file:
        print("reading file data")
        
        for memory in file:
            result += process_corrupted_memory(memory)
            print (result)

print(result)



# import re

# def parse_and_calculate(file_path):
#     # Read the file
#     with open(file_path, 'r') as file:
#         data = file.read()
    
#     # Regular expressions to find instructions
#     mul_pattern = r"mul\((\d+),(\d+)\)"
#     do_pattern = r"do\(\)"
#     dont_pattern = r"don't\(\)"
    
#     # Initial state
#     mul_enabled = True
#     total_sum = 0
#     print(f"Total sum variable : {total_sum}")
#     # Split the input into lines and process each line
#     for line in data.splitlines():
#         # Check for do() and don't() to update state
#         if re.search(do_pattern, line):
#             mul_enabled = True
#         if re.search(dont_pattern, line):
#             mul_enabled = False
        
#         # Find all mul(x, y) instructions
#         mul_matches = re.findall(mul_pattern, line)
#         if mul_enabled:
#             for x, y in mul_matches:
#                 total_sum += int(x) * int(y)
#             print(total_sum)
    
#     return total_sum

# # Path to the input file
# file_path = "input.txt"
# result = parse_and_calculate(file_path)
# print(f"Sum of enabled mul operations: {result}")
