# 자물쇠와 열쇠

# 0, 90, 180, 270도 4가지 키 존재
# 패딩을 넣어 key와 lock 계산
# key와 lock을 더해서 모두 1되도록 만들기


def init(M):
    res = []
    for m in range(M):
        temp = []
        for n in range(M):
            temp.append(0)
        res.append(temp)

    return res


def solution(key, lock):
    M = len(key)
    N = len(lock)
    key = [key]

    # 4가지 key 생성
    for i in range(3):
        new_key = init(M)
        for p in range(M):
            for q in range(M):
                new_key[q][M-1-p] = key[-1][p]


###################################################
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
###################################################
