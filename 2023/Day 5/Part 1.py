import re

def NextSrcDst(cur_locs: list, location: list) -> list:
    nxt_loc = []
    for cloc in cur_locs:
        added = False
        for loc in location:
            dst, src, rng = loc
            if cloc >= src and cloc <= src + rng:
                nxt_loc.append(dst + cloc - src)
                added = True
                break
        if not added:
            nxt_loc.append(cloc)
    return nxt_loc

def NextMap(i: int, lines: list, locs: list) -> (int, list):
    i += 2
    nxt_map = []
    while i < len(lines) and lines[i]:
        nxt_map.append(list(map(int, lines[i].split())))
        i += 1

    return (i, NextSrcDst(locs, nxt_map))

lines = [line.rstrip() for line in open("input.txt", "r").readlines()]
seeds = list(map(int, re.findall('\d+', lines[0])))

i = 1
for _ in range(7):
    i, seeds = NextMap(i, lines, seeds)

print(min(seeds))