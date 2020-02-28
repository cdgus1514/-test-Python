# C4. Write a code that finds the Nth element of the Fibonacci sequence, defined as
# 피보나치

def fibo(n):
    s = [0, 1]
    for i in range(2, n + 1):
        s.append(s[i - 1] + s[i - 2])

    # print(s)
    print(s[n])


fibo(10)