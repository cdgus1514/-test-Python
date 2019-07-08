import sys

num = int(input(">> "))

for i in range(num):
    #n1, n2 = map(int, input(">> ").split())
    n1, n2 = map(int, sys.stdin.readline().split())
    print(n1+n2)