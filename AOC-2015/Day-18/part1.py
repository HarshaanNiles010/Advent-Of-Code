from typing import List
from collections import defaultdict
def get_lines(path: str) -> List[str]:
    with open(path) as f:
        lines = [i.strip() for i in f.readlines()]
    return lines

def update(lines):
    on = 1
    directions = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
    for i in range(100):
        for j in range(100):
            pass

if __name__ == '__main__':
    input_path = 'input.txt'
    print(get_lines(input_path))