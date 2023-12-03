def GetLocalParts(input: list[int], position: int) -> (list[int], int):
    parts_sum = 0
    # Replace values in list once completed
    # Check left
    if position-1 >= 0:
        if input[0][position-1] > 0:
            parts_sum += input[0][position-1]
            num = input[0][position-1]
            
            for i in range(position-1, 0, -1):
                if input[0][i] != num:
                    break
                input[0][i] = 0

    # Check right
    if position+1 < len(input[0]):
        if input[0][position+1] > 0:
            parts_sum += input[0][position+1]
            num = input[0][position+1]

            for i in range(position+1, len(input[0])):
                if input[0][i] != num:
                    break
                input[0][i] = 0

    # Check bottom
    if input[1][position] > 0:
        parts_sum += input[1][position]
        num = input[1][position]

        for i in range(position, len(input[1])):
            if input[1][i] != num:
                break
            input[1][i] = 0

        for i in range(position-1, 0, -1):
            if input[1][i] != num:
                break
            input[1][i] = 0

    # Check bottom left
    if position-1 >= 0:
        if input[1][position-1] > 0:
            parts_sum += input[1][position-1]
            num = input[1][position-1]

            for i in range(position-1, 0, -1):
                if input[1][i] != num:
                    break
                input[1][i] = 0

    # Check bottom right
    if position+1 < len(input[0]):
        if input[1][position+1] > 0:
            parts_sum += input[1][position+1]
            num = input[1][position+1]

            for i in range(position+1, len(input[1])):
                if input[1][i] != num:
                    break
                input[1][i] = 0

    return input, parts_sum
    

def GetParts(input: list[str]) -> int:
    part_sum = 0
    for idx, c in enumerate(input[0]):
        if c == -1:
            input, ps = GetLocalParts(input, idx)
            part_sum += ps
    
    for idx, c in enumerate(input[1]):
        if c == -1:
            input, ps = GetLocalParts(input[::-1], idx)
            part_sum += ps
            input = input[::-1]

    return input, part_sum

def BuildNumbers(input: list[str]) -> list[int]:
    numbers = []
    p1, p2 = -1, -1
    num = 0
    for idx, c in enumerate(input):
        if c.isnumeric():
            num *= 10
            num += int(c)
            if p1 == -1:
                p1 = idx
                p2 = idx+1
            else:
                p2 = idx+1
        else:
            for _ in range(p1, p2):
                numbers.append(num)
            if c == '.':
                numbers.append(0)
            else:
                numbers.append(-1)
            num = 0
            p1, p2 = -1, -1

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
        print(check_cur)
        result += ss
        check_cur.pop(0)

print(f"Sum of parts: {result}")
f.close()