# A+B - 4

num = int(input(">> "))

if num < 0 and num < 99:
    exit()


n1 = num // 10
n2 = num % 10
cnt = 0
flag = True

while flag:
    n3 = n1 + n2
    n3 = n3 % 10
    str = int("%s%s" % (n2, n3))
    cnt+=1

    if num == str:
        print(cnt)
        break

    else:
        n1 = n2
        n2 = n3


