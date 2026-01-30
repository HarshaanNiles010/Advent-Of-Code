def main():
    with open('input.txt','r') as f:
        lines = [i.strip() for i in f.readlines()]
    length = 0
    state = 0
    i = 0
    while i < len(lines[0]):
        l = lines[0][i]
        if state == 0 and l == '(':
            state = 1
            chars = ''
        elif state == 1 and l != 'x':
            chars += l # type: ignore
        elif state == 1 and l == 'x':
            state = 2
            reps = ''
        elif state == 2 and l != ')':
            reps += l # type: ignore
        elif state == 2 and l == ')':
            i += int(chars) # type: ignore
            length += int(chars) * int(reps) - 3 - len(chars) - len(reps) # type: ignore
            state = 0
        length += 1
        i += 1
    print(length)
        

if __name__ == '__main__':
    main()
