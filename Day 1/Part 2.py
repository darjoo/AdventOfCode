def getNumberPart2(string: str):
    all_numbers = 'one,two,three,four,five,six,seven,eight,nine'
    rep = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9}
    p1, p2 = 0, 1
    first, second = 0, 0

    while p2 <= len(string):
        number = 0
        if string[p1].isnumeric():
            number = int(string[p1])
        else:  
            while p2 <= len(string) and string[p1:p2] in all_numbers:
                p2 += 1
            if string[p1:p2-1] in rep:
                number = rep[string[p1:p2-1]]

        if number != 0:
            second = number
            if not first:
                first = number

        p1 += 1
        p2 = p1 + 1

    return first * 10 + second

def part2():
    f = open('input.txt', 'r')
    result = 0

    for line in f.readlines():
        result += getNumberPart2(line)

    print(result)
    f.close()

part2()