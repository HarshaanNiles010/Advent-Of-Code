ing = [[4,-2,0,0,5], [0,5,-1,0,8], [-1,0,5,0,6], [0,0,-2,2,1]]

def get_score(a, b, c, d, cal_const):
    score = 1
    if cal_const:
        cals = ing[0][4]*a + ing[1][4]*b + ing[2][4]*c + ing[3][4]*d
        if cals != 500:
            return 0
        
    for i in range(4):
        x = ing[0][i]*a + ing[1][i]*b + ing[2][i]*c + ing[3][i]*d
        if x <= 0:
            return 0
        score *= x
    return score

def solve(part_two):
    best = -float('inf')
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                best = max(best, get_score(a,b,c,d,part_two))
    return best

print(solve(False))
print(solve(True))