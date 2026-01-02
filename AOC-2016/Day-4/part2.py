from collections import defaultdict
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
        temp = dict(sorted(temp.items(), key=lambda item: item[0]))
        temp = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
        res = "".join(list(temp.keys())[:5])
        return res
    
    def get_decrypt(room, cipher_key):
        result =  []
        for text in room:
            temp = []
            for ch in text:
                if 'a' <= ch <= 'z':
                    decrypted = chr((ord(ch) - ord('a') - cipher_key) % 26 + ord('a'))
                    temp.append(decrypted)
                else:
                    temp.append(ch)
            result.append(''.join(temp))
        return result

    for i,data in enumerate(rooms_data):
        room = data[:-1]
        temp = list(data[-1].replace(']','').strip().split('['))
        cipher_key = int(temp[0])
        check_sum = temp[1]
        if get_freq_table(room) == check_sum:
            decrypt = get_decrypt(room, cipher_key)
            print(i,decrypt)
            if 'north' in decrypt:
                print(f"decrypt is: {decrypt} and the index is: {rooms_data.index(data)}")
        

if __name__ == '__main__':
    main()
