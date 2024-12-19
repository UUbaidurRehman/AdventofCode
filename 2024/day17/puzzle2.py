# Function to read input from a file
def read_input_file(filename):
    registers = {}
    program = []
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Register A:"):
                registers["A"] = int(line.split(":")[1].strip())
            elif line.startswith("Register B:"):
                registers["B"] = int(line.split(":")[1].strip())
            elif line.startswith("Register C:"):
                registers["C"] = int(line.split(":")[1].strip())
            elif line.startswith("Program:"):
                program = list(map(int, line.split(":")[1].strip().split(",")))
    
    return registers, program

# Function to simulate the 3-bit computer
def simulate_program(registers, program):
    A, B, C = registers["A"], registers["B"], registers["C"]
    output = []  # To collect outputs
    ip = 0  # Instruction Pointer
    
    # Combo operand resolution
    def resolve_combo(operand):
        if operand <= 3:  # Literal values 0-3
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            return 0  # Reserved 7, treated as no-op
    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        
        if opcode == 0:  # adv: A = A // (2 ^ combo_operand)
            A = A // (2 ** resolve_combo(operand))
        elif opcode == 1:  # bxl: B = B XOR literal_operand
            B = B ^ operand
        elif opcode == 2:  # bst: B = combo_operand % 8
            B = resolve_combo(operand) % 8
        elif opcode == 3:  # jnz: Jump if A != 0
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc: B = B XOR C
            B = B ^ C
        elif opcode == 5:  # out: Output combo_operand % 8
            output_value = resolve_combo(operand) % 8
            output.append(output_value)
        elif opcode == 6:  # bdv: B = A // (2 ^ combo_operand)
            B = A // (2 ** resolve_combo(operand))
        elif opcode == 7:  # cdv: C = A // (2 ^ combo_operand)
            C = A // (2 ** resolve_combo(operand))
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
        
        ip += 2  # Move to the next instruction
    
    return output

# Function to find the lowest valid value for register A
def find_register_a_for_self_replicating_program(program):
    for a_value in range(1, 10**7):  # Search for the lowest positive A (reasonable upper bound)
        registers = {"A": a_value, "B": 0, "C": 0}
        output = simulate_program(registers, program)
        
        # Check if output matches the program
        if output == program:
            return a_value
    return None

# Main function
def main():
    input_file = "input.txt"  # Input file name
    registers, program = read_input_file(input_file)  # Read input
    
    # Find the value of A that causes the program to output itself
    result = find_register_a_for_self_replicating_program(program)
    
    if result is not None:
        print("The lowest positive initial value for register A:", result)
    else:
        print("No valid value for register A found within the search range.")

# Run the main function
if __name__ == "__main__":
    main()
