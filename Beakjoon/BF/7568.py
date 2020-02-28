# 덩치

# 인원수 입력
num = int(input())

data = []
for i in range(num):
    kg, cm = map(int, input().split())
    data.append([kg, cm])

print(data, end='\n\n')

## 모든 값과 비교하면서 순위설정
rank = []
for i in range(len(data)):
    size = 0
    tmp = list(data)
    del tmp[i]

    for j in range(len(tmp)):
        if data[i][0] > tmp[j][0] and data[i][1] > tmp[j][1]:
            size += 1
        elif data[i][0] >= tmp[j][0] or data[i][1] >= tmp[j][1]:
            size +=1

        # print('n={}차, j={}번, size = {} '.format(i+1, j+1, size ))
    rank.append(str(num - size))

print(' '.join(rank))