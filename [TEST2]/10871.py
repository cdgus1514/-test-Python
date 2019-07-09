# X보다 작은 수
# input = n, x
import sys

N, X = map(int, input(">> ").split())

list1 = [0 for _ in range(N)]
list2 = []

list1=(sys.stdin.readline().split())


for i in range(N):

    if X > int(list1[i]):
        list2.append(list1[i])
    else:
        pass


for i in range(len(list2)):
    print(list2[i], end=" ")
