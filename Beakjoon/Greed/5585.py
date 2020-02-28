# 거스름돈

# 1000엔을 내고 거스드름 주기
# 500, 100, 50, 10, 5, 1


# 물건 가격 입력
n = int(input())

money = 1000 - n
case = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in case:
    ## 나눈 몫
    cnt += money // i
    print('cnt >>', cnt, end=', ')
    ## 나눈 나머지
    money %= i
    print('res >> ', money)

# print(cnt)