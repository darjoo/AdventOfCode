from collections import Counter
import pathlib

def GetSimilarityScore(left: list, right: dict):
    return sum([l*right[l] for l in left])

def Part2():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    left, right = list(map(sorted, zip(*[map(int, line.split()) for line in file.readlines()])))
    right = Counter(right)

    print(GetSimilarityScore(left, right))

Part2()