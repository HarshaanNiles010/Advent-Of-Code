# These are not my solutions, I have understood the solutions provided but I am too lazy to write
# The original author is Fuglede on github: https://github.com/fuglede

from itertools import combinations, count
import numpy as np



with open('input.txt') as f:
    lines = [int(i.strip()) for i in f.readlines()]

def solve(part_one):
    s = sum(lines)
    target = s // 3 if part_one else s //4
    for i in count():
        c = combinations(lines, i)
        m = float('inf')
        for g1 in c:
            if sum(g1) != target:
                continue
            m = min(m, np.prod(g1))
        if m < float('inf'):
            return m


print(solve(False))