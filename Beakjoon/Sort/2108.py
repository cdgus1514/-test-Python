# 통계학

# 1. 산술평균 : N개의 수의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 오름차순 배열의 중앙값
# 3. 최빈값 : N개의 수들 중 가장 많이  나타난값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 사이

# 5
# -1
# -2
# -3
# -1
# -2


import sys, statistics
from collections import Counter

## 입력 개수
n = int(input())

## 데이터 입력
val = []
for i in range(n):
    val.append(int(sys.stdin.readline()))
    

## 1. 산술평균(수소점 반올림)
print(round(sum(val)/len(val)))

## 2. 중앙값
val.sort()
print(statistics.median(val))

## 3. 최빈값 >> Counter() : 배열의 각 값에 대해 빈도수를 dict로 만들어줌
mode_dict = Counter(val)
# print(mode_dict)
modes = mode_dict.most_common() # 튜플 형식으로 최빈값부터 2번째로 자주 나오는 숫를 반환
print(modes)

if len(modes) > 1:
    ## 빈도수가 같은경우 두번째로 작은 값 출력
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])
else:
    print(modes[0][0])


## 4. 범위
val_max = max(val)
val_min = min(val)

if len(val) < 2:
    print(val_max - val_min)
else:
    if val_min < 0:
        print(val_max - val_min)
    else:
        print(val_max + val_min)