# Z

# 2n*2n 2차원 배열
# n배의 배열이 주어졌을 때, (r, c)를 몇번째로 방문하는지
# r과 c는 0보다 크거나 같고, 2^n-1보다 작거나 같은 정수

n, r, c = map(int, input().split())
cnt = 0


def power2(k):
    return 1 << k


def go(n, r, c):
    print('n : %s, r : %s, c : %s' % (n, r, c), end='\n\n')
    if n == 1:  # 2X2 일 때
        return 2*r+c
    else:       # 2X2 이상일 때, n=1 될때까지 쪼개기
        print('(x) %s < %s' %(r, power2(n-1)))

        if r < power2(n-1):         # x좌표가 n-1배열보다 작은 경우
            print('(y) %s < %s' % (c, power2(n-1)))
            if c < power2(n-1):     # y좌표가 n-1배열보다 작은 경우
                return go(n-1, r, c)
            else:
                return go(n-1, r, c-power2(n-1)) + power2(2*n-2)
        else:
            print('(y) %s < %s' % (c, power2(n-1)))
            if c < power2(n-1):
                return go(n-1, r-power2(n-1), c) + power2(2*n-2)*2
            else:
                return go(n-1, r-power2(n-1), c-power2(n-1)) + power2(2*n-2)*3


print(go(n, r, c))




# n, r, c = map(int, input().split())
#
# cnt = 0
#
#
# def divide(size, x, y):
#     global cnt
#
#     print(size, x, y)
#
#     if size <= 2:
#         if x == r and y == c:
#             print(cnt)
#             return
#
#         cnt += 1
#         if x+1 == r and y == c:
#             print(cnt)
#             return
#
#         cnt += 1
#         if x == r and y+1 == c:
#             print(cnt)
#             return
#
#         cnt += 1
#         if x+1 == r and y+1 == c:
#             print(cnt)
#             return
#
#         cnt += 1
#         return
#
#     divide((size//2), x, y)
#     divide((size//2), x, y+(size//2))
#     divide((size//2), x+(size//2), y)
#     divide((size//2), x+(size//2), y+(size//2))
#
#
# divide(2**n, 0, 0)