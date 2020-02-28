# 블랙잭

from itertools import permutations

# 카드개수, 합 입력
num, v = map(int, input().split())
# 카드입력
card = list(map(int, input().split()))
print('card >>', card)

bf = list(set(permutations(card, 3)))
print('combination >>', bf)
print('length >>', len(bf))

max = 0

for i in range(len(bf)):
    print(i,'번째')
    clac_card = bf[i][0] + bf[i][1] + bf[i][2]
    print('calc_card >>', clac_card)

    if clac_card > max and clac_card <= v:
        max = clac_card
        if max == int(v):
            break

print(max)
