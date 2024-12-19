import sys
import z3
import re
import heapq
from collections import defaultdict, Counter, deque
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = 'input.txt'
ans = 0
D = open(infile).read().strip()

regs, program = D.split('\n\n')
A,B,C = ints(regs)
program = program.split(':')[1].strip().split(',')
program = [int(x) for x in program]
#print(A,B,C,program)


def run(Ast, part2):
    def getCombo(x):
        if x in [0,1,2,3]:
            return x
        if x==4:
            return A
        if x==5:
            return B
        if x==6:
            return C
        return -1
    A = Ast
    B = 0
    C = 0
    ip = 0
    out = []
    while True:
        if ip>=len(program):
            return out
        cmd = program[ip]
        op = program[ip+1]
        combo = getCombo(op)

        #print(ip, len(program), cmd)
        if cmd == 0:
            A = A // 2**combo
            ip += 2
        elif cmd == 1:
            B = B ^ op
            ip += 2
        elif cmd == 2:
            B = combo%8
            ip += 2
        elif cmd == 3:
            if A != 0:
                ip = op
            else:
                ip += 2
        elif cmd == 4:
            B = B ^ C
            ip += 2
        elif cmd == 5:
            out.append(int(combo%8))
            if part2 and out[len(out)-1] != program[len(out)-1]:
                return out
            ip += 2
        elif cmd == 6:
            B = A // 2**combo
            ip += 2
        elif cmd == 7:
            C = A // 2**combo
            ip += 2

part1 = run(A, False)
print(','.join([str(x) for x in part1]))

Ast = 0
best = 0
while True:
    Ast += 1
    #A = Ast * 8**5 + 0o36017
    A = Ast * 8**9 + 0o676236017
    out = run(A, True)
    if out == program:
        print(A)
        break
    elif len(out) > best:
        #print(A, oct(A), best, len(program))
        best = len(out)
# # Function to read input from a file
# def read_input_file(filename):
#     registers = {}
#     program = []
    
#     with open(filename, "r") as file:
#         for line in file:
#             line = line.strip()
#             if line.startswith("Register A:"):
#                 registers["A"] = int(line.split(":")[1].strip())
#             elif line.startswith("Register B:"):
#                 registers["B"] = int(line.split(":")[1].strip())
#             elif line.startswith("Register C:"):
#                 registers["C"] = int(line.split(":")[1].strip())
#             elif line.startswith("Program:"):
#                 program = list(map(int, line.split(":")[1].strip().split(",")))
    
#     return registers, program

# # Function to simulate the 3-bit computer
# def simulate_program(registers, program):
#     # Registers A, B, C
#     A, B, C = registers["A"], registers["B"], registers["C"]
#     output = []  # To collect outputs
#     ip = 0  # Instruction Pointer
    
#     # Combo operand resolution
#     def resolve_combo(operand):
#         if operand <= 3:  # Literal values 0-3
#             return operand
#         elif operand == 4:
#             return A
#         elif operand == 5:
#             return B
#         elif operand == 6:
#             return C
#         else:
#             return 0  # Reserved 7, treated as no-op
    
#     # Start execution
#     while ip < len(program):
#         opcode = program[ip]
#         operand = program[ip + 1]
        
#         if opcode == 0:  # adv: A = A // (2 ^ combo_operand)
#             A = A // (2 ** resolve_combo(operand))
        
#         elif opcode == 1:  # bxl: B = B XOR literal_operand
#             B = B ^ operand
        
#         elif opcode == 2:  # bst: B = combo_operand % 8
#             B = resolve_combo(operand) % 8
        
#         elif opcode == 3:  # jnz: Jump if A != 0
#             if A != 0:
#                 ip = operand
#                 continue
        
#         elif opcode == 4:  # bxc: B = B XOR C
#             B = B ^ C
        
#         elif opcode == 5:  # out: Output combo_operand % 8
#             output_value = resolve_combo(operand) % 8
#             output.append(output_value)
        
#         elif opcode == 6:  # bdv: B = A // (2 ^ combo_operand)
#             B = A // (2 ** resolve_combo(operand))
        
#         elif opcode == 7:  # cdv: C = A // (2 ^ combo_operand)
#             C = A // (2 ** resolve_combo(operand))
        
#         else:
#             raise ValueError(f"Unknown opcode: {opcode}")
        
#         # Move instruction pointer to the next instruction
#         ip += 2
    
#     return ",".join(map(str, output))  # Return output as a comma-separated string

# # Main function
# def main():
#     input_file = "input.txt"  # Input file name
#     registers, program = read_input_file(input_file)  # Read input
#     result = simulate_program(registers, program)  # Run simulation
#     print("Final Output:", result)

# # Run the main function
# if __name__ == "__main__":
#     main()
