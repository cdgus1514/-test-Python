# 다트게임

# 정규표현식 사용
import re

db = {'S': '**1', 'D': '**2', 'T': '**3', '#': '*-1'}


def solution(dartResult):
    answer = ''
    for i in re.sub('([SDT][*#]?)', '\g<1> ', dartResult).split():
        if i[-1] == '*':
            if answer:
                answer = answer[:-1] + '*2+'
            i += '2'

        for j in db.keys():
            i = i.replace(j, db[j])

        answer += i + "+"

    print(answer[:-1])
    return eval(answer[:-1])


################################################################################
dartResult = '1S2D*3T'
# dartResult = '1D#2S*3S'
print(solution(dartResult))
################################################################################
