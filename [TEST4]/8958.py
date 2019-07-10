# OX퀴즈
# O일때, cnt++
# X일때, cnt=0

ox = []
cnt = 0
score = 0


# 테스트 케이스
T = int(input(">> "))


# 데이터 입력 ( 리스트 안에 리스트)
for i in range(T):
    str = input(">> ")
    ox.append(list(str))


# 점수 체크
for i in range(T):
    cnt=0; score=0
    for j in range(len(ox[i])):
        if ox[i][j] == "O":
            cnt+=1
            score+=cnt
        else:
            cnt=0

    print(score)


#for i in range(len(test))
