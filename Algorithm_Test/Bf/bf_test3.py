## 숫자야구

import itertools

def solution(baseball):
    p = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    s, b = 0, 0

    test = list(p)

    for i in range(len(baseball)):
        question_str = str(baseball[i][0])

        for j in p:
            for k in range(len(j)):
                if int(question_str[k]) == j[k]:
                    s += 1
                if int(question_str[k]) in j:
                    b += 1
            
            if not(s == baseball[i][1] and b == baseball[i][1] + baseball[i][2]):
                if j in test:
                    test.remove(j)
            
            s, b = 0, 0

    return (len(test))


########################################################
baseball = [[123,1,1], [356,1,0], [327,2,0], [489,0,1]]
print(solution(baseball))
########################################################
