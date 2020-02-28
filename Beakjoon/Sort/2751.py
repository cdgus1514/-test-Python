# 수 정렬하기2

# 오름차순으로 정렬 >> 수의 개수가 많을경우 해결해야하는 방법 O(nlongn)
# 5
# 4
# 3
# 2
# 1

import sys

# 개수 입력
n = int(input())

odd = []
even = []

# 홀/짝 분리 후 내림차순 정렬
for i in range(n):
    val = int(sys.stdin.readline())
    if val %2 == 0:
        even.append(val)
    else:
        odd.append(val)

odd.sort(reverse=True)
even.sort(reverse=True)
# print(odd, even)


try:
    for i in range(n):
        if odd[-1] < even[-1]:
            print(odd.pop())
        else:
            print(even.pop())
except:
    if len(odd) == 0:
        for i in range(len(even)):
            print(even.pop())
    else:
        for i in range(len(odd)):
            print(odd.pop())