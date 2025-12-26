def increase(s, i):
    if s[i] == 'z':
        s[i] = 'a'
        increase(s, i - 1)
    else:
        s[i] = chr(ord(s[i]) + 1)

def has_three(s):
    streak = 1
    for i in range(1, len(s)):
        if (ord(s[i - 1]) == ord(s[i]) - 1):
            streak += 1
            if streak == 3:
                return True
        else:
            streak = 1
    return False

def has_no_iol(s):
    return 'i' not in s and 'o' not in s and 'l' not in s

def has_double(s):
    in_pair = True
    pairs = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            if in_pair:
                pairs += 1
                if pairs == 2:
                    return True
                in_pair = False
            else:
                in_pair = True
        else:
            in_pair = True
    return False

def part1_sol(code):
    while True:
        increase(code, len(code) - 1)
        if has_double(code) and has_no_iol(code) and has_three(code):
            return ''.join(code)

if __name__ == '__main__':
    current_password = list('abcdefgh')
    actual_password = list('hxbxxyzz')
    print(part1_sol(actual_password))