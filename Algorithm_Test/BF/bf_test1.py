## 모의고사
# O(n)

def solution(answer):    
    person = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    # 사람 수 만큼 점수 리스트 생성
    score = [0] * len(person)

    for i in range(len(answer)):
        if answer[i] == person[0][i%5]:
            score[0] += 1
        if answer[i] == person[1][i%8]:
            score[1] += 1
        if answer[i] == person[2][i%10]:
            score[2] += 1
    
    return [i + 1 for i, v in enumerate(score) if v == max(score)]


#############################################################################
m1 = [1,2,3,4,5]
m2 = [2,1,2,3,2,4,2,5]
m3 = [3,3,1,1,2,2,4,4,5,5]

## 테스트 케이스
# answer = [1, 2, 3, 4, 5]
answer = [1, 3, 2, 4, 2]
# answer = [4, 4, 4, 5, 1]
#############################################################################

print(solution(answer))