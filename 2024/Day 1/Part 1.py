import pathlib

def GetTotalDistance(left, right):
    return sum([abs(l-r) for l, r in zip(left, right)])

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    left, right = [], []
    for line in file.readlines():
        left_value, right_value = [int(v.strip()) for v in line.split()]
        left.append(left_value)
        right.append(right_value)

    left.sort()
    right.sort()
    
    print(GetTotalDistance(left, right))

Part1()