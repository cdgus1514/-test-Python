# C6. Write a code for finding a maximum prime factor of given natural number N.
# 가장 큰 소수값 찾기

def check_prime(n):
    check = []

    for i in range(1, n + 1):
        cnt = 0

        # 소수찾기(자기자신 외 나뉘어지면 소수 X)
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            check.append(i)

    # print(check)
    print(check[len(check) - 1])


check_prime(100)