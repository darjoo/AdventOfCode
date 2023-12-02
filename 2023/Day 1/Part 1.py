def getNumberPart1(string: str, end: bool):
    for c in string if not end else string[::-1]:
        if c.isnumeric():
            return int(c)

def part1():
    f = open('input.txt', 'r')
    number = 0
    for  line in f.readlines():
        number += (getNumberPart1(line, False) * 10) + getNumberPart1(line, True)
    print(number)
    f.close()

part1()