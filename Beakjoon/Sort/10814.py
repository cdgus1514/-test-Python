# 나이순 정렬

# 가입한 사람들의 나이순으로 정렬, 나이가 같으면 먼저 가입한 사람순으로 정렬
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung


# import sys
#
# # 사용자 수 입력
# n = int(sys.stdin.readline())
n = int(input())

# 사용자 정보 입력 후 정렬
user = []
for i in range(n):
    # user.append(list(sys.stdin.readline().split()))
    age, name = map(str, input().split())
    age = int(age)
    user.append((age, name))

user.sort(key=lambda x: (x[0]))

for i in range(n):
    print(user[i][0], user[i][1])