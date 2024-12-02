import re
from collections import defaultdict

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data

# Include your file path
file_path = r"input.txt"
D = read_file(file_path)
L = D.split('\n')
ans = 0 

t, d = L
times = [int(x) for x in t.split(':')[1].split()]
dist = [int(x) for x in d.split(':')[1].split()]

T = ''
for t in times:
    T += str(t)
T = int(T)
D = ''
for d in dist:
    D += str(d)
D = int(D)

def f(t, d):
    ans = 0
    for x in range(t + 1):
        dx = x * (t - x)
        if dx >= d:
            ans += 1
    return ans

ans = 1
for i in range(len(times)):
    ans *= f(times[i], dist[i])
print(ans)
print(f(T, D))