import re

f = open('input.txt', 'r')
nums = [cards.split(':')[1] for cards in f.readlines()]
f.close()

cards = [1] * len(nums)

for i, cur_nums in enumerate(nums):
    for nc in range(i,i+len(re.findall(r'\b(\d+)\b(?=.*\b\1\b)', cur_nums))):
        cards[nc+1] += cards[i]

print(sum(cards))