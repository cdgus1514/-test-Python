# 좌표 정렬하기

# N개 점(X,Y)
# x값을 기준으로 오름차순으로 정렬
# x값이 같으면 y값을 기준으로 오름차순 정렬


## 좌표개수 입력
n = int(input())

position = list()
check = list()

## 좌표입력
for i in range(n):
    position.append(list(input().split()))

## 정수로 변환
for i in range(n):
    check.append(list(map(int, position[i])))

check.sort(key=lambda x: (x[0], x[1]))

for i in check:
    print(i[0], i[1])
