import math

def PowerOfSet(input: str) -> bool:
    # [red, green, blue]
    result = {'red':0, 'green':0, 'blue':0}

    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" 
    # Result in
    # [" 3 blue, 4 red", " 1 red, 2 green", ...]
    sets = input.split(':')[1].split(';')

    for cur_set in sets:
        cur_cubes = cur_set.split(',')

        for cur_cube in cur_cubes:
            _, num, color = cur_cube.split(' ')
            result[color] = max(result[color], int(num))

    return math.prod(result.values())

f = open('input.txt', 'r')

result = 0
for line in f.readlines():
    result += PowerOfSet(line.rstrip())

print(f"Sum of power sets: {result}")
f.close()