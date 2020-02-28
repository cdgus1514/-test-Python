# 수 정렬하기

# 입력된 n개의 수를 오름차순 정렬 O(n^2)



## 개수 입력
n = int(input())

## 숫자 입력(스트링)
num = list()
for i in range(n):
    num.append(input())

## 정수변환 후 정렬
check = list(map(int, num))
check.sort()

for i in check:
    print(i)