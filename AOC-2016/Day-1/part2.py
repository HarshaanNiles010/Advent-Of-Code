def main(path):
    with open(path) as f:
        data = f.read()
    inputs = list(map(str.strip, data.split(',')))
    location = 0 + 0j
    current_direction = 1j
    visited = set()
    for i in inputs:
        turn_direction = i[0]
        distance = int(i[1:])
        if turn_direction == 'R':
            current_direction *= -1j
        else:
            current_direction *= 1j
        for _ in range(distance):
            location += current_direction
            if location in visited: return abs(location.real) + abs(location.imag)
            visited.add(location)

if __name__ == '__main__':
    path = 'input.txt'
    first_visited = main(path)
    print(first_visited)
