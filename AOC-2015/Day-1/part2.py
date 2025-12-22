with open('input.txt') as f:
    data = f.read()

print(next(i for i in range(len(data)) if data[:i].count('(') - data[:i].count(')') == -1))