# 10 10     >> 9 25

H, M = (map(int, input(">> ").split()))

if M < 45:
    M = M+(60-45)
    H-=1

print(H, M)