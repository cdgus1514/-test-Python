# 한 줄로 서기

# 자기보다 큰사람이 왼쪽으로 몇명이 있었는지만 기억
# N명의 사람이 있고, 키는 1부터 N까지


#
# 4
# 2 1 1 0



N = int(input())
arr = list(map(int, input().split(' ')))

line = []

for i in range(len(arr)-1, -1, -1):
    print(i, end=' >> ')
    line.insert(arr[i], i+1)
    print('arr[i]=', arr[i], ', i+1=', i+1)
    print(line, end='\n\n')

print(*line)