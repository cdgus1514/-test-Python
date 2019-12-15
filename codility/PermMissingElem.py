# N개의 다른 1 ~ n+1 범위의 정수로 이루어진 배열 존재
# 배열에 누락된 정수를 찾아 출력


# def solution(A):
#     if A == '':
#         return 1
#
#     A.sort()
#     start = A[0]
#     end = A[-1]
#
#     for i in range(start, end):
#         if i in A:
#             pass
#         else:
#             return i

# def solution(A):
#     result = len(A) + 1 # 5
#
#     for N in range(0, len(A)):
#         result ^= (N+1) ^ A[N]
#         print(result)
#
#     return result


#
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

