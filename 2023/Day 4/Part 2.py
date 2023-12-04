import re

f = open('input.txt', 'r')
nums = [cards.split(':')[1] for cards in f.readlines()]
f.close()

cards = [1] * len(nums)

for i, cur_nums in enumerate(nums):
    win, scratched = cur_nums.split('|') 
    winnings = {w for w in re.findall(r'\d+', win)}
    scratched = {s for s in re.findall(r'\d+', scratched)} 

    inter = winnings.intersection(scratched)
    
    for nc in range(i+1, i+1+len(inter)):
        cards[nc] += cards[i]
print(sum(cards))