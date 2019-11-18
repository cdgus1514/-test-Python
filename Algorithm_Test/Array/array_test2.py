# 가장 큰 수

import itertools

# def solution(numbers):
    
#     case = list(itertools.permutations(numbers, len(numbers)))
#     for i in range(len(case)):
#         if case[i][0] == 0:
#             case.remove(case[i])

#     comp = []
#     tmp = ''

#     for i in range(len(case)):
#         for j in range(len(case[i])):
#             tmp += str(case[i][j])
    
#         comp.append(tmp)
#         tmp = ''
    
#     return max(comp)



def solution(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))




##########################################################
# numbers = [6,10,2]
numbers = [3,30,34,5,9]

print(solution(numbers))




    