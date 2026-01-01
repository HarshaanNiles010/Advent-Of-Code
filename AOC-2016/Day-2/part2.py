def main():
    with open('input.txt') as f:
        dirs = [x.strip() for x in f.readlines()]
    location = (-2, 0)
    keys = []
    key_map = {
        (0, 2): 1,
        (-1, 1): 2,
        (0, 1): 3,
        (1, 1): 4,
        (-2, 0): 5,
        (-1, 0): 6,
        (0, 0): 7,
        (1, 0): 8,
        (2, 0): 9,
        (-1, -1): 'A',
        (-1, 0): 'B',
        (-1, 1): 'C',
        (0, -2): 'D'
    }
    left_edges = [(-2, 0), (-1, 1), (0, 2), (-1, -1), (0, -2)]
    right_edges = [(2, 0), (1, 1), (0, 2), (1, -1), (0, -2)]
    top_edges = [(-2, 0), (-1, 1), (0, 2), (1, 1), (2, 0)]
    bottom_edges = [(-2, 0), (-1, -1), (0, -2), (1, -1), (2, 0)]
    for d in dirs:
        for x in d:
            new_loc = list(location)
            if x == 'L':
                if location not in left_edges:
                    new_loc[0] -= 1 # type: ignore
            if x == 'U':
                if location not in top_edges:
                    new_loc[1] += 1 # type: ignore
            if x == 'R':
                if location not in right_edges:
                    new_loc[0] += 1 # type: ignore
            if x == 'D':
                if location not in bottom_edges:
                    new_loc[1] -= 1 # type: ignore
            location = tuple(new_loc)
        keys.append(key_map[location]) # type: ignore
    print(keys)

if __name__ == '__main__':
    main()
