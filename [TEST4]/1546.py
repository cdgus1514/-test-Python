# 평균

import sys

max = 0
sum = 0

# 과목 수
T = int(input(">> "))

#데이터 입력
score = list(map(int, sys.stdin.readline().split()))

for i in score:
    if max < i:
        max = i

for i in range(T):
    calc = (score[i]/max)*100
    score[i]=calc

    sum += score[i]


#print(sum, max)

avg = sum/T
print("%.2f" % avg)