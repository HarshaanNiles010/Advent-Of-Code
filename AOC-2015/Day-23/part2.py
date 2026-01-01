from collections import defaultdict

with open('input.txt') as f:
    lines = [i.strip().replace(',', '').split() for i in f.readlines()]

def run(regs_expr):
    res = 0
    while True:
        if res >= len(lines):
            return regs_expr['b']
        ins = lines[res]
        if ins[0] == 'inc': regs_expr[ins[1]] += 1
        elif ins[0] == 'tpl': regs_expr[ins[1]] *= 3
        elif ins[0] == 'hlf': regs_expr[ins[1]] //= 2
        elif ins[0] == 'jmp': res += int(ins[1]) - 1
        elif ins[0] == 'jie':
            if regs_expr[ins[1]] % 2 == 0: res += int(ins[2]) - 1
        elif ins[0] == 'jio':
            if regs_expr[ins[1]] == 1: res += int(ins[2]) - 1
        res += 1

regs_expr = defaultdict(int)
regs_expr['a'] = 1
print(run(regs_expr))