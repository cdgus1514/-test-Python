# 하노이탑

# 1. 한 번에 한 개의 원판만 다른 탑으로 옮길 수 있음
# 2. 쌓아놓은 원판은 항상 위에 것이 아래보다 작아야 함

## n개의 원판이 있는 경우 이동 횟수는 2^n-1
## 1번 기둥에 위치한 n개의 원판 중, 위에 있는 n-1개의 원판을 2번 기둥으로 옮기기. (n-1, a, c, b)
## 1번 기둥에 남아있는 1개의 원판을 3번 기둥으로 옮기기. (n, a, b, c)
## 2번 기둥에 있는 n-1개의 원판을 3번 기둥으로 옮기기.

## f(n, a, b, c) >> n개의 원판이 a기둥에 있을 때, c 기둥으로


def hanoi(n, a, b, c):
    print('h(%s, %s, %s, %s)' % (n, a, b, c), end=' >> ')

    if n == 1:
        print(a, c, '[n == 1]', end='\n\n')
    else:
        hanoi(n-1, a, c, b)
        print('h(%s, %s, %s, %s)' % (n, a, b, c), end=' >> ')
        print(a, c, '[n != 1]', end='\n\n')
        hanoi(n-1, b, a, c)


n = int(input())

print(2**n-1, end='\n\n')
if(n <= 20):
    hanoi(n, 1, 2, 3)