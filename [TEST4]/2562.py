# 최댓값
num = []

for i in range(9):
    num.append(input(">> "))

max = 0
cnt = 0

# max값 찾기
for i in num:
    if max < int(i):
        max = int(i)

# max값 위치 찾기
for i in num:
    if max != int(i):
        cnt+=1


print(max)
print(cnt)