data = open('input.txt', 'r').read().strip().split('\n')
data = list(list(x) for x in data)
m, n = len(data), len(data[0])
def spin_north(data):
    ndata = [['.'] * n for _ in range(m)]
    for j in range(n):
        to_place = 0
        for i in range(m):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = i + 1
            elif data[i][j] == 'O':
                ndata[to_place][j] = 'O'
                to_place += 1
    return ndata

def spin_west(data):
    ndata = [['.'] * n for _ in range(m)]
    for i in range(m):
        to_place = 0
        for j in range(n):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = j + 1
            elif data[i][j] == 'O':
                ndata[i][to_place] = 'O'
                to_place += 1
    return ndata

def spin_south(data):
    ndata = [['.'] * n for _ in range(m)]
    for j in range(n):
        to_place = m - 1
        for i in reversed(range(m) ):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = i - 1
            elif data[i][j] == 'O':
                ndata[to_place][j] = 'O'
                to_place -= 1
    return ndata

def spin_east(data):
    ndata = [['.'] * n for _ in range(m)]
    for i in range(m):
        to_place = n - 1
        for j in reversed(range(n) ):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = j - 1
            elif data[i][j] == 'O':
                ndata[i][to_place] = 'O'
                to_place -= 1
    return ndata

# part 1
ndata = spin_north(data)
print("Part 1:", sum( (m - i) for i in range(m) for j in range(n) if ndata[i][j] == 'O') )

# part 2
TIMES = 10 ** 9
ndata, recur = data[:], {}
for x in range(TIMES):
    # spin a cycle
    ndata = spin_north(ndata)
    ndata = spin_west(ndata)
    ndata = spin_south(ndata)
    ndata = spin_east(ndata)

    tuple_data = tuple(tuple(x) for x in ndata)
    if tuple_data in recur:
        diff = x - recur[tuple_data]
        TIMES = (TIMES - x) % diff - 1
        break
    recur[tuple_data] = x

for x in range(TIMES):
    # spin a cycle
    ndata = spin_north(ndata)
    ndata = spin_west(ndata)
    ndata = spin_south(ndata)
    ndata = spin_east(ndata)

print("Part 2:", sum( (m - i) for i in range(m) for j in range(n) if ndata[i][j] == 'O') )