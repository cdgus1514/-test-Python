import itertools

# print("-".join(str(n) for n in range(100)))

# num = "185"
num = "512"
num = list(num)
case = []

for i in range(1, len(num)+1):
    case += list(map(''.join, itertools.permutations(num, i)))
    print(case)


case = list(set(map(int, case)))
case.sort()

print("\n\n")
print(case)
print(len(case))
