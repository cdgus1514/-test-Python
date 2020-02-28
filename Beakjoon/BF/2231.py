# 분해합

# 256(=245+2+4+5)
# 216 > ?


N = int(input())

num = 0

for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    # print(div_num)
    sum_num = i + sum(div_num)
    # print(sum_num)

    if(sum_num == N):
        num = i
        break

print(num)