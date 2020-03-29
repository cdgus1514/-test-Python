# 토너먼트 만들기

# 랭킹이 높은 사람이 반드시 이김
# 부전승이 많더라도 최소한의 랭킹 차이를 가지는 토너먼트 만들기

# 랭킹이 낮은 선수(높은숫자)가 토너먼트에 자주 올라갈수록 합이 크게나옴
# 1. 랭킹이 가장 낮은 선수 찾기
# 2. 찾은 선수의 좌/우 선수와 차이의 최소값 찾기
# 3. 최소값을 구한 후 랭킹이 낮은 선수는 제거하고  그 다음으로 랭킹이 낮은 선수를 찾아 1-2과정 반복


n = int(input())
line = list(map(int, input().split()))
result = 0

for i in range(len(line)-1):
    target = max(line)          ## 가장 큰 숫자 찾기
    idx = line.index(target)    ## 찾은 숫자의 인덱스 찾기
    # print('target >>', target, 'index >>', idx, 'length >>', len(line), end='\n\n')

    if idx == 0:                ## 가장 큰 수가 첫 번째 인덱스인 경우
        result += line[idx] - line[idx+1]
    elif idx == len(line)-1:    ## 가장 큰 수가 마지막 인덱스인 경우
        result += line[idx] - line[idx-1]
    else:
        L = line[idx] - line[idx+1]
        R = line[idx] - line[idx-1]
        result += min(L, R)

    line.pop(idx)
    target -= 1

print(result)