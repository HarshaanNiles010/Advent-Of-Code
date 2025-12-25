from typing import List
from ast import literal_eval
def generate_lines(path: str) -> List[str]:
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def part1(lines: List[str]):
    t = 0
    for l in lines:
        t += 2
        escaped = False
        for s in l:
            if not escaped and s == '\\':
                escaped = True
            elif escaped:
                if s == '\\' or s == '"':
                    t += 1
                elif s == 'x':
                    t += 3
                escaped = False
    return t

def part1_diff_method(lines: List[str]):
    t = 0
    for line in lines:
        t += len(line) - len(literal_eval(line))
    return t


if __name__ == '__main__':
    lines = generate_lines('input.txt')
    x = part1(lines)
    y = part1_diff_method(lines)
    assert(x == y)