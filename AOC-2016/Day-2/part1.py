def main(path: str):
    with open(path) as f:
        data = [i.strip() for i in f.readlines()]
    
    def location_tokey(loc):
        return loc[0] * 3 + loc[1] + 1
    location = [1, 1]
    keys = []
    for d in data:
        for x in d:
            if x == 'L':location[1] = max(location[1] - 1, 0)
            if x == 'U':location[0] = max(location[0] - 1, 0)
            if x == 'R':location[1] = min(location[1] + 1, 2)
            if x == 'L':location[0] = min(location[0] + 1, 2)
        keys.append(location_tokey(location))
    print(keys)


if __name__ == '__main__':
    path = 'input.txt'
    main(path)
