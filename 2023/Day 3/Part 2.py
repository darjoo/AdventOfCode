import re

def RemoveLeftRight(r: int, c: int, value: int) -> None:
    for i in range(c, -1, -1):
        if numbers.get((r, i), -1) == value:
            numbers.pop((r, i))
        else:
            break
    for i in range(c+1, row_len):
        if numbers.get((r, i), -1) == value:
            numbers.pop((r, i))
        else:
            break

def UpdateSymbols(r, c, value):
    symbols[(r, c)][0] += 1
    symbols[(r, c)][1] *= value

def FindGearRatio() -> None:
    for (r, c) in symbols.keys():

        for cr in (r-1, r, r+1):
            for cc in (c-1, c, c+1):
                if (cr, cc) in numbers:
                    UpdateSymbols(r, c, numbers[(cr, cc)])
                    RemoveLeftRight(cr, cc, numbers.get((cr, cc)))

# def BuildMaps(row: int, input: list[int]) -> None:
#     for idx, value in enumerate(input):
#         if value == -1:
#             symbols[(row, idx)] = [0, 1]
#         elif value > 0:
#             numbers[(row, idx)] = value

def BuildNumbers(r, input: list[str]) -> list[int]:
    for match in re.finditer(r'\d+', str(input)):
        numbers[(r, idx)] = int(match.group(0))
    for idx, c in enumerate(input):
        
        if c not in '0123456789.':
            symbols[(r, idx)] = [0, 1]


    # cur_numbers = []
    # num, p1, p2 = 0, -1, -1
    # for idx, c in enumerate(input):
    #     if c.isnumeric():
    #         num = (num * 10) + int(c)
    #         if p1 == -1:
    #             p1 = idx
    #             p2 = idx+1
    #         else:
    #             p2 = idx+1
    #     else:
    #         for _ in range(p1, p2):
    #             cur_numbers.append(num)
    #         cur_numbers.append(0 if c == '.' else -1)
    #         num, p1, p2 = 0, -1, -1

    # if p1 != -1:
    #     for _ in range(p1, p2):
    #         cur_numbers.append(num)

    # return cur_numbers

f = open('Coding Challeges\\AdventOfCode\\2023\\Day 3\\input.txt', 'r')
# f = open('input.txt', 'r')

check_cur = []
numbers = dict()
symbols = dict()
row_len = 0
result = 0
for idx, line in enumerate(f.readlines()):
    row_len = len(line.rstrip())
    cur_line = BuildNumbers(idx, list(line.rstrip()))
    # BuildMaps(idx, cur_line)
FindGearRatio()

for (r, c) in symbols.keys():
    if symbols[(r, c)][0] == 2:
        result += symbols[(r, c)][1]
print(f"Sum of gear ratios: {result}")
f.close()