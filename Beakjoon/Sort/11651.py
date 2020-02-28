# 좌표 정렬하기2

# N개 점(X,Y)
# y값을 기준으로 오름차순으로 정렬
# y값이 같으면 x값을 기준으로 오름차순 정렬


# 점 개수 입력
n = int(input())

position = list()
check = list()

# 좌표 입력
for i in range(n):
    position.append(list(input().split()))

# 정수로 변환
for i in range(n):
    check.append(list(map(int, position[i])))

# 정렬
check.sort(key=lambda x: (x[1], x[0]))

for i in check:
    print(i[0], i[1])