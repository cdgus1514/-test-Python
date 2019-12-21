# 이진수로 변환 후 0의 길이가 가장 긴 값을 출력

def solution(N):
    # write your code in Python 3.6
    return len(max(format(N, 'b').strip('0').split('1')))


N = 328
print(solution(N))
