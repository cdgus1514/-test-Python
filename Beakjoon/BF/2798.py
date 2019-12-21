# 블랙잭

from itertools import permutations

num, v = map(int, input().split())
card = list(map(int, input().split()))

bf = list(set(permutations(card, 3)))
max = 0

for i in range(len(bf)):
    clac_card = bf[i][0] + bf[i][1] + bf[i][2]
    if clac_card > max and clac_card <= v:
        max = clac_card
        if max == int(v):
            break

print(max)
