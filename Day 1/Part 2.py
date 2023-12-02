def getNumberPart2(string: str):
    numbers = [0] * len(string)
    all_numbers = 'one,two,three,four,five,six,seven,eight,nine'
    rep = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9}
    p1, p2 = 0, 1
    first, second = 0, 0

    while p2 <= len(string):
        if string[p1].isnumeric():
            numbers[p1] = int(string[p1])
        else:  
            while p2 <= len(string) and string[p1:p2] in all_numbers:
                p2 += 1
            if string[p1:p2-1] in rep:
                numbers[p1] = rep[string[p1:p2-1]]

        if numbers[p1] != 0:
            second = numbers[p1]
            if not first:
                first = numbers[p1]

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