import pathlib

INPUTNAME = 'input.txt'

def part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath(INPUTNAME))
    file = open(path, 'r')

    # Rotations are tuples of (direction, amount)
    rotations = [(d, a) for d, a in ((line[0], int(line[1:])) for line in file.readlines())]
    file.close()

    # Initial setting at 50, range of [0, 99]
    dial = 50
    password = 0

    for direction, amount in rotations:
        # Normalize amount to range [0, 99]
        full_rotations = amount // 100
        password += full_rotations
        amount %= 100

        prev_dial = dial

        match direction:
            case 'L':
                dial -= amount
            case 'R':
                dial += amount
            case _:
                raise ValueError(f'Unknown direction: {direction}')
            
        if (dial < 0 or dial > 100) and prev_dial != 0:
            password += 1
        dial %= 100
        if dial == 0:
            password += 1

    print(f'Password: {password}')


if __name__ == '__main__':
    part1()
