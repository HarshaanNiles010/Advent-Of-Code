from itertools import permutations

with open('input.txt') as f:
    lines = [i.strip().split() for i in f.readlines()]

mp = {}

for line in lines:
    mp[line[0], line[-1][:-1]] = -int(line[3]) if line[2] == 'lose' else int(line[3])

names = list(set(line[0] for line in lines))

def solve():
    best_match = -float('inf')
    for p in permutations(names):
        value = mp[p[0], p[-1]] + mp[p[-1], p[0]]
        for i in range(len(p) - 1):
            value += mp[p[i], p[i + 1]] + mp[p[i + 1], p[i]]
        best_match = max(best_match, value)
    return best_match

print(solve())

for name in names:
    mp['myself', name] = 0
    mp[name, 'myself'] = 0
names += ['myself']
print(solve())