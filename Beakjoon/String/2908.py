# 상수

# num1 = '734'
# num2 = '893'

num1, num2 = input().split()
num1 = list(num1)
num2 = list(num2)

num1.reverse()
num2.reverse()
num1 = int(''.join(num1))
num2 = int(''.join(num2))


if num1 > num2:
    print(num1)
else:
    print(num2)