def main():
    with open('input.txt') as f:
        lines = [i.strip() for i in f.readlines()]
    #print(lines)
    data = [[] for i in range(8)]
    for line in lines:
        data[0].append(line[0])
        data[1].append(line[1])
        data[2].append(line[2])
        data[3].append(line[3])
        data[4].append(line[4])
        data[5].append(line[5])
        data[6].append(line[6])
        data[7].append(line[7])
    
    def gen_freq_table(dat):
        temp = {}
        for d in dat:
            if d in temp:
                temp[d] += 1
            else:
                temp[d] = 1
        temp = dict(sorted(temp.items(), key=lambda item: item[1]))
        return list(temp.keys())[0]
    
    res = []
    for i in range(8):
        res.append(gen_freq_table(data[i]))
    print(''.join(res))
    
if __name__ == '__main__':
    main()
