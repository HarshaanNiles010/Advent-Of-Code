import numpy as np

def find_house(puzzle_input):
    presents = np.zeros(puzzle_input//10)
    for i in range(1, puzzle_input//10):
        for j in range(i, puzzle_input//10, i):
            presents[j] += i * 10
    print(np.argmax(presents >= puzzle_input))

def find_something(n):
    presents = np.zeros(n//10)
    for elf in range(1, n//10):
        for house in range(elf, n//10, elf):
            presents[house] += elf * 11
            if house == 50*elf:
                break
    print(np.argmax(presents >= n))





if __name__ == '__main__':
    puzzle_input = 36000000
    find_house(puzzle_input)
    find_something(puzzle_input)