# 1. 내림차순 정렬
# 2. 홀수를 찾아서 재정렬

a = [4,3,1,2,6,7,10]
# a = [7, 5, 3, 2, 9, 8, 13, 15, 22, 24, 30]
print(a, end=' -> ')

# 내림차순 정렬
a.sort(reverse=True)

# 재정렬할 홀수 개수 체크
cnt = 0
for i in a:
    if i % 2 != 0:
        cnt +=1

# 홀수 개수만큼 반복
for i in range(cnt):
    # 홀수 찾아서 재정렬
    for j in range(len(a)):
        if a[j] % 2 != 0:
            tmp = a.pop(j)
            a.insert(len(a), tmp)
            break

print(a)