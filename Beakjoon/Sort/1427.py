# 소트인사이드

# 입력된 숫자를 내림차순으로 정리 후 출력(스트링



## 입력(스트링)
N = list(input())

## 정수로 변환 후 정렬
check = list(map(int, N))

check.sort(reverse=True)

print(''.join(map(str, check)))
