import math
import re

def PowerOfSet(input: str) -> bool:
    result = {'red':0, 'green':0, 'blue':0}

    pulls = re.findall("(\d+) (\w+)", input)
    for num, color in pulls:
        result[color] = max(result[color], int(num))

    return math.prod(result.values())

f = open('input.txt', 'r')

result = 0
for line in f.readlines():
    result += PowerOfSet(line.rstrip())

print(f"Sum of power sets: {result}")
f.close()