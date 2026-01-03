import re
def main():
    with open('input.txt') as f:
        lines = [i.strip() for i in f.readlines()]
    data = {}
    # Step 1 check if there are any palindromes within the square brackets, if they are, then remove those IP Addresses
    for i,line in enumerate(lines):
        t = re.findall(r"\[\w+\]", line)
        for j in t:
            x = j.replace('[', ' ').replace(']', ' ').strip()
            if x != x[::-1]:data[i] = line
    print(data)
if __name__ == '__main__':
    main()
