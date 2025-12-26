def expand(s):
    new_s = ''
    c = 0
    curr = s[0]
    for i in range(len(s)):
        if(i > 0 and s[i] != curr):
            new_s += f'{c}{s[i - 1]}'
            curr = s[i]
            c = 0
        c += 1
    new_s += f'{c}{curr}'
    return new_s



def part2_sol(code):
    for _ in range(50):
        code = expand(code)
    print(len(code))

if __name__ == '__main__':
    actual_code = '3113322113'
    test_code = '1'
    part2_sol(actual_code)