import pathlib

def GetTotalDistance(left, right):
    return sum([abs(l-r) for l, r in zip(left, right)])

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    left, right = list(map(sorted, zip(*[map(int, line.split()) for line in file.readlines()])))
    
    print(GetTotalDistance(left, right))

Part1()