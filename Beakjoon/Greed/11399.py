# ATM

# ATM앞에 N명의 사람이 줄서있고, 앞사람이 돈뽑는 시간이 누적
# 최소한의 시간으로 출금할 수 있도록 만들기


import sys

n = int(input())
val = list(map(int, sys.stdin.readline().strip().split()))


total = 0
# val.sort()
print(val)

for i in range(len(val)):
    total += sum(val[0:i+1])

print(total)