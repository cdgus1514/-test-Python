# 동전 0

# 동전은 총 N개의 종류가 있고, 동전을 적절히 사용하여 동전 개수의 최솟값 구하기

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000


n, value = map(int, input().split())


money = []
for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)
cnt = 0

for i in money:
    if i > value:
        pass
    else:
        cnt += value // i
        value %= i

print(cnt)