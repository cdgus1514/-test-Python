# 부등호

# '<', '>' 기호가 K개 나열된 순열 존재
# 0부터 9까지 한번씩만 사용하여 주어진 부등호 조건에 맞는 모든 정수 출력

# k개의 부등호 순서를 만족하는 k+1 개의 정수 중 최댓값과 최솟값 찾기

# 2
# < >


# import operator
import sys
# import numpy as np
# from itertools import permutations

n = int(input())
inequality = list(sys.stdin.readline().split())
c = [False] * 10
minN, maxN = '', ''


def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j

    return True


def solve(cnt, s):
    global minN, maxN

    if cnt == n + 1:
        if not len(minN):   # 0
            minN = s
        else:
            maxN = s
        return

    print('\n')
    print(c)
    for i in range(10):
        print('cnt :', cnt, ', i :', i, ', c[i] :', c[i])
        if not c[i]:    # False
            print('s :', s, ', inequality :', inequality[cnt-1], ', i :', i)
            if cnt == 0 or possible(s[-1], str(i), inequality[cnt - 1]):
                c[i] = True
                solve(cnt+1, s + str(i))  # 재귀
                c[i] = False


solve(0, '')
print('%s\n%s' % (maxN, minN))


# print(inequality)
# print(c)
# for j in range(10):
# print(possible('', j, inequality))


# ops = []
# ret = []
#
# for s in inequality:
#     if s == '<':
#         ops.append(operator.lt)
#     else:
#         ops.append(operator.gt)
#
# # num = list(np.arange(0, 10, 1))
# num = [i for i in range(10)]
#
# for c in permutations(num, n+1):
#     check = True
#
#     for i in range(n):
#         if not ops[i](c[i], c[i+1]):
#             check = False
#
#     if check:
#         ret.append(c)
#
# print(''.join([str(i) for i in ret[-1]]))
# print(''.join([str(i) for i in ret[0]]))
