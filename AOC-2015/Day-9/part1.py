from typing import List
from itertools import permutations

def generate_paths(path):
    with open(path) as f:
        lines = [i.strip().split() for i in f.readlines()]
    # Path map
    d = {}
    # Adj List
    for line in lines:
        d[line[0], line[2]] = int(line[4])
        d[line[2], line[0]] = int(line[4])
    
    places = list(set(i[0] for i in d.keys()))

    return [places, d]

def shortest_path(places, d):
    shortest = float('inf')
    for p in permutations(places):
        length = sum(d[p[i], p[i + 1]] for i in range(len(p) - 1))
        shortest = min(shortest, length)
    print(shortest)

if __name__ == '__main__':
    paths = generate_paths('input.txt')
    shortest_path(paths[0], paths[1])