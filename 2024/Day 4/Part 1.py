from collections import defaultdict
import pathlib

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')

    puzzle = defaultdict(str) | {(i, j):char for i, row in enumerate(file) 
                                    for j, char in enumerate(row)}
    keys = list(puzzle.keys())
    direction = [-1,0,1]

    target = list('XMAS')

    count = sum([puzzle[i+di*n, j+dj*n] for n in range(4)] == target 
                    for di in direction for dj in direction for i,j in keys)

    print(count)

Part1()