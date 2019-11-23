def solution(stones, k):
    answer = 0
    return answer


###################################################
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
###################################################

cnt = 0
passCnt = 0
jump = 1


while True:
    if stones[cnt] is 0:
        if jump > 3:
            break
        else:
            jump += 1
    else:
        tmp = stones[cnt] - jump
        stones[cnt] = tmp
        cnt += 1

    cnt += 1


print(passCnt)
