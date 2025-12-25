from typing import List

def generate_paths(path):
    with open(path) as f:
        lines = [i.strip() for i in f.readlines()]
    path_map = {}
    for line in lines:
        t = line.split(" ")
        src = t[0]
        dst = t[2]
        cost = int(t[len(t) - 1])
        path_map[(src, dst)] = cost
    return path_map

def part1_sol(path_map):
    places = list(set(l[0] for l in path_map.keys()))
    # We need to make Kruskal's minimum spanning tree   

if __name__ == '__main__':
    path_map = generate_paths('input.txt')
    part1_sol(path_map)