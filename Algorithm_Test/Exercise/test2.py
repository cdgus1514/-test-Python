# v = [[1, 4], [3, 4], [3, 10]]
v = [[1, 1], [2, 2], [1, 2]]


check1 = []
check2 = []
result = []

for i in range(len(v)):
    check1.append(v[i][0])
    check2.append(v[i][1])

check1.sort()
for i in check1:
    if check1.count(i) == 1:
        result.append(i)

check2.sort()
for i in check2:
    if check2.count(i) == 1:
        result.append(i)


print(result)
