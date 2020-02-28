# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의.
# d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터라고 한다. 91은 101의 제네레이터
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 반대로 제네레이터가 없는 숫자들을 셀프 넘버라 이름 붙였다. (1, 3, 5, 7, 9, 20, 31 ...)

## Question
# 1 이상 5000 이하 모든 셀프 넘버들의 합을 구하라


def d(n):
    for i in str(n):
        n += int(i)

    return n


a = set(list(range(1,5000)))
b = set()

for i in a:
    b.add(d(i))

print(b, end="\n\n")

result = sum(a-b)
print(result)