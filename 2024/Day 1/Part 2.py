from collections import defaultdict
import pathlib

def GetSimilarityScore(left: defaultdict, right: defaultdict):
    return sum([abs(l*right[l]) for l in left])

def Part2():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    left, right = [], defaultdict(int)
    for line in file.readlines():
        left_value, right_value = [int(v.strip()) for v in line.split()]
        left.append(left_value)
        right[right_value] += 1

    print(GetSimilarityScore(left, right))

Part2()