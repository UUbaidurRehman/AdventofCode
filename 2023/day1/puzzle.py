

def calib():
    with open("input.txt", "r") as file:
        rows = file.readlines()
        totalsum = 0
        for row in rows:
            digits = [int (char) for char in row if char.isdigit()]
            num = int(f"{digits[0]}{digits[-1]}")
            totalsum +=num
    return totalsum

print (calib())