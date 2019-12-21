# X에서 Y로 이동
# 고정된 D 만큼 점프
## 최소 점프 횟수 찾기

def solution(X,Y,D):
    add = 0

    if (X-Y) // D != 0:
        add += 1

    return (Y-X) // D + add


X = 10
Y = 85
D = 30

print(solution(X,Y,D))