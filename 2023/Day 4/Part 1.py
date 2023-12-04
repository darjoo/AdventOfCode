import re

f = open('input.txt', 'r')
nums = [cards.split(':')[1] for cards in f.readlines()]
f.close()

result = 0

for i, cur_nums in enumerate(nums):
    length = len(re.findall(r'\b(\d+)\b(?=.*\b\1\b)', cur_nums))
    ww = 1 if length else 0
    for x in range(1,length):
        ww*=2
    result += ww

print(result)