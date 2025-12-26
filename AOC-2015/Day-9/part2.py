from itertools import permutations

with open('input.txt') as f:
    lines = [i.strip().split() for i in f.readlines()]
# Map of all the routes
d = {}
# Bidirectional Adj List
for line in lines:
    d[line[0], line[2]] = int(line[4])
    d[line[2], line[0]] = int(line[4])

places = list(set(i[0] for i in d.keys()))

longest = -float("inf")

for p in permutations(places):
    length = sum(d[p[i], p[i + 1]] for i in range(len(p) - 1))
    longest = max(longest, length)

print(longest)