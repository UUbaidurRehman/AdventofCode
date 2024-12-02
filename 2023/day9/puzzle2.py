def extrapolate_previous_value(history):
    """
    This function takes a history of values and extrapolates the previous value.
    It generates sequences of differences until they are all zeroes, then works
    backwards to find the previous value.
    """
    sequences = [history]
    while not all(value == 0 for value in sequences[-1]):
        new_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
        sequences.append(new_sequence)

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])

    return sequences[0][0]

def extrapolate_previous_value_from_file(file_path):
    """
    Reads histories from a file and extrapolates the previous value for each history.
    Sums up these extrapolated values and returns the sum.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    histories = [list(map(int, line.strip().split())) for line in lines]

    sum_extrapolated_values = sum(extrapolate_previous_value(history) for history in histories)

    return sum_extrapolated_values


file_path = 'input.txt'
sum_extrapolated_values = extrapolate_previous_value_from_file(file_path)
print(sum_extrapolated_values)