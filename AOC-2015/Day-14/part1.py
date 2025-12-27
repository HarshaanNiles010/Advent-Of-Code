from collections import defaultdict

with open('input.txt') as f:
    lines = [i.strip().split() for i in f.readlines()]

def get_distance(vel, time_travel, time_rest, max_time):
    time = 0
    dist = 0
    while True:
        for _ in range(time_travel):
            dist += vel
            time += 1
            if time == max_time:
                return dist
        time += time_rest
        if time >= max_time:
            return dist

best = -float('inf')

for line in lines:
    distance = get_distance(int(line[3]), int(line[6]), int(line[-2]), 2503)
    best =  max(best, distance)
print(best)
