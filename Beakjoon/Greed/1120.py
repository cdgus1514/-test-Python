# 문자열

# 길이가 N으로 같은 문자열 X와 Y가 존재
# i는 X와 Y의 차이 개수 최소화

# adaabc aababbc


A, B = map(str, input().split(' '))
MIN = 50

for i in range(0, len(B)-len(A)+1):
    cnt = 0

    for j in range(0, len(A)):
        print('A[', j, '] : ', A[j], '  B[', j+i, '] : ', B[j+i])
        if A[j] != B[j+i]:
            cnt += 1

    MIN = min(MIN, cnt)

print(MIN)