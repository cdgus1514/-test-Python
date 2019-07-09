#별찍기

T = int(input(">> "))

for i in range(T+1):
    for j in range(i):
        print("★", end="")

    print()