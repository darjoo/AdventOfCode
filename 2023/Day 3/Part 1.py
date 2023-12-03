def ReplaceWithZeros(input: list[int], start: int, end: int, num: int) -> list[int]:
    for i in range(start, end, 1 if start < end else -1):
        if input[i] != num:
            break
        input[i] = 0

    return input

def GetLocalParts(input: list[int], position: int) -> (list[int], int):
    parts_sum = 0
    # Replace values in list once completed
    # Check left
    if position-1 >= 0:
        if input[0][position-1] > 0:
            parts_sum += input[0][position-1]
            input[0] = ReplaceWithZeros(input[0], position-1, 0, input[0][position-1])

    # Check right
    if position+1 < len(input[0]):
        if input[0][position+1] > 0:
            parts_sum += input[0][position+1]
            input[0] = ReplaceWithZeros(input[0], position+1, len(input[0]), input[0][position+1])

    # Check bottom
    if input[1][position] > 0:
        parts_sum += input[1][position]
        input[1] = ReplaceWithZeros(input[1], position+1, len(input[1]), input[1][position])
        input[1] = ReplaceWithZeros(input[1], position, 0, input[1][position])

    # Check bottom left
    if position-1 >= 0:
        if input[1][position-1] > 0:
            parts_sum += input[1][position-1]
            input[1] = ReplaceWithZeros(input[1], position-1, 0, input[1][position-1])

    # Check bottom right
    if position+1 < len(input[0]):
        if input[1][position+1] > 0:
            parts_sum += input[1][position+1]
            input[1] = ReplaceWithZeros(input[1], position+1, len(input[1]), input[1][position+1])

    return input, parts_sum
    

def GetParts(input: list[int]) -> (list[int], int):
    part_sum = 0
    for idx, (c0, c1) in enumerate(zip(input[0], input[1])):
        ps = 0
        if c0 == -1:
            input, ps = GetLocalParts(input, idx)

        if c1 == -1:
            input, ps = GetLocalParts(input[::-1], idx)
            input = input[::-1]

        part_sum += ps

    return input, part_sum

def BuildNumbers(input: list[str]) -> list[int]:
    numbers = []
    num, p1, p2 = 0, -1, -1
    for idx, c in enumerate(input):
        if c.isnumeric():
            num = (num * 10) + int(c)
            if p1 == -1:
                p1 = idx
                p2 = idx+1
            else:
                p2 = idx+1
        else:
            for _ in range(p1, p2):
                numbers.append(num)
            numbers.append(0 if c == '.' else -1)
            num, p1, p2 = 0, -1, -1

    if p1 != -1:
        for _ in range(p1, p2):
            numbers.append(num)

    return numbers

f = open('input.txt', 'r')

check_cur = []
result = 0
for line in f.readlines():
    check_cur.append(BuildNumbers(list(line.rstrip())))
    if len(check_cur) == 2:
        check_cur, ss = GetParts(check_cur)
        result += ss
        check_cur.pop(0)

print(f"Sum of parts: {result}")
f.close()