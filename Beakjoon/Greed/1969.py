# DNA

# DNA는 4가지 물질로 이루어져있고 표현할때에는 A, T, G, C로 표현
# Hamming Distance는 같은 길이의 DNA일 경우, 다른 위치의 개수

# N개 길이의 DNA가 주어질 경우, Hamming Distance의 합이 가장 작은 DNA를 구하는 것
# 5 8
# TATGATAC
# TAAGCTAC
# AAAGATCC
# TGAGATAC
# TAAGATGT

import sys

# 입력 개수
n, size = map(int, input().split())

dna = []
result = ''
hd = 0
for i in range(n):
    dna.append(input())

print(dna)
print(dna[0][0])
print(dna[1][0])
print(dna[2][0])
print(dna[3][0])
print(dna[4][0], end='\n\n')

for i in range(size):   # DNA 길이
    cnt = [0, 0, 0, 0]
    for j in range(n):  # 입력받은 DNA의 n번째 뉴클레오티드를 확인
        if dna[j][i] == 'A':
            cnt[0] += 1
        elif dna[j][i] == 'C':
            cnt[1] += 1
        elif dna[j][i] == 'G':
            cnt[2] += 1
        elif dna[j][i] == 'T':
            cnt[3] += 1

    print(cnt)

    Max = max(cnt)
    print('Max >> ', Max)

    idx = cnt.index(Max)
    print('idx >> ', idx)
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'

    hd += n - Max
    print(result, end='\n\n')


print(result)
print(hd)