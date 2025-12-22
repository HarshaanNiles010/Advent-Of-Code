import re
from collections import defaultdict

with open('input.txt') as f:
    data = f.read()

p1 = p2 = 0
pres = defaultdict(int)
pres[0] = 2
for i, a in enumerate(data):
    if i % 2:
        if a == "^":
            p1 += 1j
        elif a == "v":
            p1 -= 1j
        elif a == ">":
            p1 += 1
        elif a == "<":
            p1 -= 1
        pres[p1] += 1
    else:
        if a == "^":
            p2 += 1j
        elif a == "v":
            p2 -= 1j
        elif a == ">":
            p2 += 1
        elif a == "<":
            p2 -= 1
        pres[p2] += 1
print(sum(v > 0 for v in pres.values()))