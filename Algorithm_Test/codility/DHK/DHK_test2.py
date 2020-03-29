# N 개의 정수로 구성된 배열 A가 주어지면 가장 큰 값 X를 반환합니다.이 값은 정확히 X 배입니다.
# 그러한 값이 없으면 함수는 0을 반환해야합니다.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    check = list(set(A))
    cnt = dict()
    result = dict()

    del check[check.index(1)]
    print(check, end="\n\n")

    # 각각의 인덱스 값과 배수를 딕셔너리로 저장
    for i in check:
        if A.count(i) == 1:
            pass
        else:
            cnt[i] = A.count(i)

    # 배수값이 1보다 큰 값이 없으면 0으로 리턴
    if len(cnt) == 0 or max(cnt.resultues()) <= 1:
            return 0

    for k, v in cnt.items():
        value = k ** v
        result[k] = value

    max_v = max(result.values())

    for k, v in result.items():
        if v == max_v:
            return k



# A = [7, 1, 2, 8, 2]
A = [3, 1, 4, 1, 5]
print(solution(A))