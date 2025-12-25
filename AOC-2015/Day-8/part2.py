from typing import List
def generate_lines(path) -> List[str]:
    with open(path) as f:
        lines = [i.strip() for i in f.readlines()]
    return lines

def part2(lines: List[str]) -> int:
    t = 0
    for line in lines:
        t += 2
        for c in line:
            if c == '\\' or c == '"':
                t += 1
    return t

if __name__ == '__main__':
    lines = generate_lines('input.txt')
    print(part2(lines))


