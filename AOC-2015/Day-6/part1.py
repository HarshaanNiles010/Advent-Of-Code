import re
import numpy as np

# Online Solution by fuglede on github https://github.com/fuglede/adventofcode
with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

is_on = np.zeros((1000,1000), dtype=bool)

for l in lines:
    n = [int(x) for x in re.findall(r'\d+', l)]
    if 'on' in l:
        is_on[n[0]:n[2] + 1, n[1]:n[3] + 1] = 1
    elif 'off' in l:
        is_on[n[0]:n[2] + 1, n[1]:n[3] + 1] = 0
    else:
        is_on[n[0]:n[2] + 1, n[1]:n[3] + 1] = ~is_on[n[0]:n[2] + 1, n[1]:n[3] + 1]

print(np.sum(is_on))


# My solution