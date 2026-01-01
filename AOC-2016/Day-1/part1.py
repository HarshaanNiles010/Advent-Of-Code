def main(path: str):
    with open(path) as f:
        data = f.read()

    inputs = list(map(str.strip, data.split(',')))

    location = 0 + 0j
    current_direction = 1j
    for i in inputs:
        turn_direction = i[0]
        distance = int(i[1:])
        if turn_direction == "R":
            current_direction *= -1j
        else:
            current_direction *= 1j
        location += current_direction * distance
    print(abs(location.real) + abs(location.imag))

if __name__ == '__main__':
    path = 'input.txt'
    main(path)
