with open('input.txt') as f:
    lines = [i.strip().replace(':','').replace(',','').split() for i in f.readlines()]

mp = {}
for line in lines:
    mp[int(line[1])] = {line[2] : int(line[3]), line[4] : int(line[5]), line[6] : int(line[7])}

goal = {'children' : 3,
        'cats' : 7,
        'samoyeds' : 2,
        'pomeranians' : 3,
        'akitas' : 0,
        'vizslas' : 0,
        'goldfish' : 5,
        'trees' : 3,
        'cars' : 2,
        'perfumes' : 1}

for aunt, things in mp.items():
    if all(goal[item] == count for (item, count) in things.items()):
        print(aunt)
        break

# Part two
lt = {'cats', 'trees'}
gt = {'pomeranians', 'goldfish'}
for aunt, items in mp.items():
    found = True
    for (item, count) in items.items():
        if item in lt:
            if count <= goal[item]:
                found = False
                break
        elif item in gt:
            if count >= goal[item]:
                found = False
                break
        else:
            if count != goal[item]:
                found = False
                break
    if found:
        print(aunt)
        break