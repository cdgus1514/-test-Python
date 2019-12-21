# 문자열 반복

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)

    for i in range(len(S)):
        print(R*S[i], end='')
    print()