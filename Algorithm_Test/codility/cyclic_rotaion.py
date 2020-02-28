# 배열을 k번 회전시키기

def solution(A, K):
    if len(A) == 0:
        return A
    else:
        K = K % len(A)
        print('len(A) >> ', len(A))
        print('K >>', K, end="\n\n")

    print(A[-K:])
    print(A[:-K], end="\n\n")
    return A[-K:] + A[:-K]

# A = [3,8,9,7,6]
A = [1,2,3,4]
K = 4

# [6,3,8,9,7]
# [7,6,3,8,9]
# [9,7,6,3,8]

print(solution(A,K))