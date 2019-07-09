# 숫자의 개수

n1 = int(input(">> "))
n2 = int(input(">> "))
n3 = int(input(">> "))

sum = n1*n2*n3
s = str(sum)
list = list(s)

num=[0 for _ in range(10)]


for i in list:

    if i == "0":
        num[0]+=1
    elif i == "1":
        num[1]+=1
    elif i == "2":
        num[2]+=1
    elif i == "3":
        num[3]+=1
    elif i == "4":
        num[4]+=1
    elif i == "5":
        num[5]+=1
    elif i == "6":
        num[6]+=1
    elif i == "7":
        num[7]+=1
    elif i == "8":
        num[8]+=1
    elif i == "9":
        num[9]+=1


for i in num:
    print(i)
