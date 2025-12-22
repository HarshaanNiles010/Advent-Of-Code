import re

with open('input.txt') as f:
    data = f.readlines()

sizes = [[int(x) for x in re.findall(r'\d+', s)] for s in data]

print(sum(2*(sum(s) - max(s)) + s[0]*s[1]*s[2] for s in sizes))