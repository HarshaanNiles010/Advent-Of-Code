import json
import re

with open('input.txt') as f:
    s = f.read()
print(sum(map(int, re.findall(r'-?\d+', s))))