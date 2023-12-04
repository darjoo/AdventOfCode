import re

f = open('input.txt', 'r')
nums = [cards.split(':')[1] for cards in f.readlines()]
f.close()

result = 0

for i, cur_nums in enumerate(nums):
    win, scratched = cur_nums.split('|') 
    winnings = {w for w in re.findall(r'\d+', win)}
    scratched = {s for s in re.findall(r'\d+', scratched)} 
    ww = 1 if len(winnings.intersection(scratched)) else 0
    for x in range(1,len(winnings.intersection(scratched))):
        ww*=2
    result += ww

print(result)