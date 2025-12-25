from collections import Counter

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

lower_case = list(map(chr, range(65 + 32, 65 + 32 + 26)))

pairs = [a + b for a in lower_case for b in lower_case]
triples = [a + b + a for a in lower_case for b in lower_case]

def is_nice(w):
    return any(w.count(p) > 1 for p in pairs) and any(t in w for t in triples)

print(sum(map(is_nice, lines)))