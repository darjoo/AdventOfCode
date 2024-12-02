import pathlib

def isSafe(report: list[int]) -> bool:
    diff = set([report[l] - report[l-1] for l in range(1, len(report))])
    if diff <= {1, 2, 3} or diff <= {-1, -2, -3}:
        return True
    return False

def GetTotalSafeReports(reports: list[int]) -> int:
    return sum([any([isSafe(report) for i in range(len(report))]) for report in reports])

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')
    reports = [list(map(int, line.split())) for line in file.readlines()]
    print(GetTotalSafeReports(reports))

Part1()