from collections import defaultdict
import re

with open('input.txt') as f:
    lines = [x.strip().split() for x in f.readlines()]

replacements = [(x[0], x[2]) for x in lines[:-2]]
initial = lines[-1][0]


# Part one
def make_combinations(s):
    combinations = set()
    for r in replacements:
        for m in re.finditer(r[0], s):
            yield s[:m.start()] + r[1] + s[m.end():]


print(len(set(make_combinations(initial))))