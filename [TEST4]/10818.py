# 최대, 최소

T = int(input(">> "))
num = [0 for _ in range(T)]


num = input(">> ").split()
max = 0
min = 1000000

for i in range(T):

    if int(num[i]) > max:
        max = int(num[i])
    if int(num[i]) < min:
        min = int(num[i])

print(min, max)