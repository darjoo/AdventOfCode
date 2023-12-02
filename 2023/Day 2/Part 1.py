def parseInput(input: str) -> bool:

    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green" 
    # Result in
    # [" 3 blue, 4 red", " 1 red, 2 green", ...]
    sets = input.split(':')[1].split(';')

    for cur_set in sets:
        cur_cubes = cur_set.split(',')

        # [red, green, blue]
        result = [0] * 3

        for cur_cube in cur_cubes:
            _, num, color = cur_cube.split(' ')
            
            match color:
                case 'red':
                    result[0] += int(num)
                    if result[0] > 12:
                        return False
                case 'green':
                    result[1] += int(num)
                    if result[1] > 13:
                        return False
                case 'blue':
                    result[2] += int(num)
                    if result[2] > 14:
                        return False

    return True

filepath = 'C:\\Users\\jooda\\OneDrive\\TechNotes\\Coding Challeges\\AdventOfCode\\2023\\Day 2\\input.txt'
f = open(filepath, 'r')

result = 0
for id, line in enumerate(f.readlines()):
    answer = parseInput(line.rstrip())

    print(f"{line}")
    print(f"Answer: {answer}")
    
    if answer:
        result += id + 1

print(f"Sum of possible games: {result}")
f.close()