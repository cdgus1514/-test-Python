# 잃어버린 괄호

# 최대 길이가 50인 식의 괄호를 모두 지움
# 이 식의 최소값을 만들기


from itertools import permutations


arr = list(input().split('-'))
num = []
result = 0

for i in arr:
    cnt = 0
    tmp = i.split('+')

    for j in tmp:
        cnt += int(j)

    num.append(cnt)


result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)