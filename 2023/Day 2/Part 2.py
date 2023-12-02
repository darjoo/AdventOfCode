from functools import reduce

def PowerOfSet(input: str) -> bool:
    # [red, green, blue]
    result = [0] * 3

    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" 
    # Result in
    # [" 3 blue, 4 red", " 1 red, 2 green", ...]
    sets = input.split(':')[1].split(';')

    for cur_set in sets:
        cur_cubes = cur_set.split(',')

        for cur_cube in cur_cubes:
            _, num, color = cur_cube.split(' ')
            num = int(num)
            match color:
                case 'red':
                    if result[0] < num:
                        result[0] = num
                case 'green':
                    if result[1] < num:
                        result[1] = num
                case 'blue':
                    if result[2] < num:
                        result[2] = num

    return reduce((lambda x, y: x* y), result)

f = open('input.txt', 'r')

result = 0
for id, line in enumerate(f.readlines()):
    result += PowerOfSet(line.rstrip())

print(f"Sum of power sets: {result}")
f.close()