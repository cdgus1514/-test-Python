# 뒤집기

# 0과 1로 이루어진 문자열에 있는 모든 숫자를 같게 만들려고한다.
# 문자열 S가 주어졌을 때, 최소 횟수출력

# 문자가 달라지는 곳을 기준으로 세그먼트를 나눈 후 세그먼트의 개수 절반

# 0001100

card = input()
card = list(card)

print(card)

cnt = 0
flag = ''
for i in card:
    if i == '0' and flag == '':
        cnt += 1
        flag = i
    elif i == '1' and flag == '':
        cnt += 1
        flag = i

    elif i == '0' and flag == i:
        pass
    elif i == '1' and flag == i:
        pass

    elif i == '0' and flag != i:
        cnt += 1
        flag = i
    elif i == '1' and flag != i:
        cnt += 1
        flag = i

print(cnt // 2)