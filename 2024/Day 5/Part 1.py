import pathlib

def Part1():
    path = str(pathlib.Path(__file__).resolve().parent.joinpath('input.txt'))
    file = open(path, 'r')

    rules = set[tuple[int, int]]()
    updates = list[int]()
    isRules = True

    for line in file:
        if line.strip() == "":
            isRules = False
            continue
        if isRules:
            before, after = map(int, line.strip().split('|'))
            rules.add((before, after))
        else:
            updates.append(list(map(int, line.strip().split(','))))

    result = 0

    for update in updates:
        pairs = set[tuple[int, int]]()
        for idx in range(1, len(update)):
            pairs.add((update[idx-1], update[idx]))

            inter = rules.intersection(pairs)

        if len(inter) == len(pairs):
            result += update[len(update) // 2]
    print(f"Result: {result}")

Part1()