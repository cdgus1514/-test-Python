# A+B - 5
import sys

flag = True

while flag:
    N ,M = map(int, sys.stdin.readline().split())

    if N==0 and M==0:
        #flag = False
        break

    print("%d" % (N+M))

