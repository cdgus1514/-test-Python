## 소수찾기

import itertools

def solution(numbers):
    p = list(numbers)
    a = []

    for i in range(1, len(p)+1):
        a += list(map(''.join, itertools.permutations(p, i)))

    # 중복제거
    a = list(set(map(int, a)))
    a.sort()

    cnt = 0
    for i in a:
        if i < 2:
            pass
        elif i == 2:
            cnt += 1
        else:
            for j in range(2,i):
                if i % j == 0:
                    break;
                elif i == j+1:
                    cnt += 1
    return cnt




##############################################################################
# numbers = "17"
# numbers = "011"
numbers = "0721910"
print(solution(numbers))
##############################################################################

# numbers로 생성될 수 있는 모든 경우를 담아두고 하나씩 판별


# p = list(numbers)
# a = []
# print(p)

# for i in range(1, len(p)+1):
#     a += list(map(''.join, itertools.permutations(p, i)))
#     print(a)

# # 중복제거
# a = list(set(map(int, a)))
# print(a, end="\n\n")

# a.sort()
# print(a)

# cnt = 0
# for i in a:
#     if i == 1 or i == 0:
#         pass
    
#     else:
#         if i % 2 == 0:
#             if i == 2:
#                 cnt += 1
#         elif i % 3 == 0:
#             if i == 3:
#                 cnt += 1
#         else:
#             cnt += 1

# print(cnt)


'''
# 짝수 제거(에라토스테네스의 체)
p = set([i for i in range(3, n+1, 2)])

for i in range(3, n+1, 2):
    if i in p:
        p -= set([i for i in range(i*2, n+1, i)])

len(p) + 1
'''