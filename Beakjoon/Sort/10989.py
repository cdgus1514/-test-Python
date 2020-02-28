# 수 정렬하기3

# N개의 수를 오름차순으로 정렬
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7



import sys

n = int(input())

check = [0]*10001

for i in range(n):
    check[int(sys.stdin.readline())] += 1

for i in range(10001):
    sys.stdout.write('%s\n' %i*check[i])