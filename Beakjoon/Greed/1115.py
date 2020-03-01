# 순열

# 0부터 N-1까지 모든 정수를 한 번씩 포함하는 순열 존재.
# 순열 A를 이용하여 길이가 같은 B를 구할 수 있다.

# B[0] = 0
# B[i] = A[B[i-1]]
# 배열에 같은 값의 개수 출력

from itertools import permutations
import sys

N = int(input())
P = list(sys.stdin.readline().split())

P_permute = list(permutations(P, N))

cnt = []
for i in range(len(P_permute)):
    Q = [0]
    print(P_permute[i])

    for j in range(1, N):
        Q.append(int(P[Q[j-1]]))

    print(Q, '>> ', (len(P_permute[i]) - len(set(Q))), end='\n\n')
    cnt.append(len(P_permute[i]) - len(set(Q)))

print(len(cnt))
print(min(cnt))