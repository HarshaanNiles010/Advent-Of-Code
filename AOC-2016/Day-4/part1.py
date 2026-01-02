import re
from collections import Counter, defaultdict
from typing import List
def main():
    with open('input.txt') as f:
        lines = [i.strip() for i in f.readlines()]
    rooms_data = [line.split('-') for line in lines]
    def get_freq_table(room: List[str]):
        temp = {}
        for r in room:
            for t in r:
                if t in temp:
                    temp[t] += 1
                else:
                    temp[t] = 1
        temp = dict(sorted(temp.items(), key = lambda item: item[0]))
        temp = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
        res = "".join(list(temp.keys())[:5])
        return res
    res = 0
    for data in rooms_data:
        room = data[:-1]
        #print(f"Room: {room}")
        temp = list(data[-1].replace(']','').strip().split('['))
        Id = int(temp[0])
        checkSum = temp[1]
        if get_freq_table(room) == checkSum:
            res += Id
        else:
            continue
    print(f"The result from all the rooms is: {res}")        



if __name__ == '__main__':
    main()
