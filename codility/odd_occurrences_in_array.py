# xor연산하기

def solution(A):
    x = 0

    for i in A:
        x ^= i

    return x

A = [9,3,9,3,9,7,9]
print(solution(A))