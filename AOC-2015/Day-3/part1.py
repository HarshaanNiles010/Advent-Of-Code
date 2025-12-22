import re
from collections import defaultdict

with open('input.txt') as f:
    data = f.read()

p = 0
pres = defaultdict(int)
pres[0] = 1
for a in data:
    if a == "^":
        p += 1j
    if a == "v":
        p -= 1j
    if a == ">":
        p += 1
    if a == "<":
        p -= 1
    pres[p] += 1
print(sum(v > 0 for v in pres.values()))