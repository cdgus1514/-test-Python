# N개의 다른 1 ~ n+1 범위의 정수로 이루어진 배열 존재
# 배열에 누락된 정수를 찾아 출력


def solution(A):
    return sum(range(len(A)+2)) - sum(A)

A = [2,3,1,5,4,8,7,11,9,10]
print(solution(A))

#
# print(len(A))
#
# print(sum(range(7+2)))
# print(sum(range(9)))
# print(sum(A))
#
test = list(range(10+2))
print(test)
# print(sum(test))

