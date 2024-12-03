import re

def sum_valid_muls(filename):
    # Define a regex pattern for valid `mul(X,Y)` instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total_sum = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Find all matches in the current line
            matches = re.findall(pattern, line)
            # Compute the sum of valid multiplications
            for x, y in matches:
                total_sum += int(x) * int(y)
    
    return total_sum

# Example usage
filename = "input.txt"
result = sum_valid_muls(filename)
print(f"The total sum of valid multiplications is: {result}")
