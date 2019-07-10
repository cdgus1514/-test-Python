# 평균은 넘겠찌
# score[i][1:] 사용 가능

import sys

score = []
sum = 0
cnt = 0

C = int(input(">> "))

# 데이터 입력
for i in range(C):
    score.append(sys.stdin.readline().split())

# 테스트 평균 구하기
for i in range(C):
    sum = 0; avg = 0 ; cnt = 0
    for j in range(1,len(score[i])):
        s = int(score[i][0])
        sum += int(score[i][j])

    avg = sum/s

    # 테스트 중 평균 이상자 비율 출력
    for k in range(1, len(score[i])):
        if int(score[i][k]) > int(avg):
            cnt += 1

    print("%.3f" % ((cnt/s)*100)+"%")


'''

for i in range(int(input())):
    list_input = list(map(int, input().split(' ')))
    ave = sum(list_input[1:]) / list_input[0]
    count = 0
    for j in list_input[1:]:
        if j > ave:
            count += 1
    print(str('%.3f' % round(count / list_input[0] * 100, 3)) + '%')
'''