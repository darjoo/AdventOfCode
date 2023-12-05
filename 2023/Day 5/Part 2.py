import re, math

def IntervalCheck(src: list, dst: list) -> (list, list):
    new_src = []
    new_dst = []
    
    # Src completely inside
    if dst[1] <= src[0] and src[1] <= dst[1] + dst[2]:
        new_dst.append([dst[0] + src[0] - dst[1], dst[0] + src[0] - dst[1] + src[2], src[2]])
    
    # Dst completely inside
    elif src[0] <= dst[1] and dst[1] + dst[2] <= src[1]:
        # before
        new_src.append([src[0], dst[1]-1, dst[1] - src[0]])

        # inside
        new_dst.append([dst[0], dst[0] + dst[2]-1, dst[2]])

        # after
        new_src.append([dst[1] + dst[2], src[1], src[1] - dst[1] - dst[2]+1])

    # Src Before and inside
    elif src[0] < dst[1] and dst[1] <= src[1] < dst[1] + dst[2]:
        new_dst_range = src[1] - dst[1] + 1
        new_dst.append([dst[0], dst[0] + new_dst_range-1, new_dst_range])

        new_src_range = dst[1] - src[0]
        new_src.append([src[0], dst[1] - 1, new_src_range])

    # Src Inside and after
    elif dst[1] <= src[0] and src[0] <= dst[1] + dst[2] < src[1]:
        new_dst_start = src[0] - dst[1] + dst[0]
        new_dst_range = dst[1] + dst[2] - src[0]
        new_dst.append([new_dst_start, new_dst_start + new_dst_range - 1, new_dst_range])

        new_src_start = dst[1] + dst[2]
        new_src_range = src[2] - new_dst_range
        new_src.append([new_src_start, new_src_start + new_src_range - 1, new_src_range])

    # Src Completely outside
    elif src[1] < dst[1] or dst[1] + dst[2] < src[0]:
        new_src.append(src)

    return (new_src, new_dst)

def NextSrcDst(source: list, destination: list) -> list:
    nxt_loc = []

    for dest in destination:
        new_src = []
        for src in source:
            ns, nd = IntervalCheck(src, dest)
            new_src.extend(ns)
            nxt_loc.extend(nd)

        source = new_src
    nxt_loc.extend(source)
    return nxt_loc

def NextMap(i: int, lines: list, locs: list) -> (int, list):
    i += 2
    nxt_map = []
    while i < len(lines) and lines[i]:
        nxt_map.append(list(map(int, lines[i].split())))
        i += 1

    return (i, NextSrcDst(locs, nxt_map))

lines = [line.rstrip() for line in open("input.txt", "r").readlines()]
preseeds = list(map(int, re.findall('\d+', lines[0])))
seeds = []

for i in range(0, len(preseeds), 2):
    seeds.append([preseeds[i], preseeds[i] + preseeds[i+1], preseeds[i+1]])

i = 1
for _ in range(7):
    i, seeds = NextMap(i, lines, seeds)

lowest = math.inf

for seed in seeds:
    lowest = min(lowest, seed[0])

print(lowest)