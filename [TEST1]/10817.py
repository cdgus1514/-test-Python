A, B, C = (map(int, input(">> ").split()))

max = 0

if A > B:
    max = A

    if B > C:
        print(B)
    else:
        print(C)

else:
    max = B

    if A > C:
        print(A)
    else:
        print(C)