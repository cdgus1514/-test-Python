# 삽입정렬

# 아직 정렬되지 않은 값을 정렬된 배열 사이에 끼워넣는 과정을 반복 

# 버블정렬처럼 이미 정렬되어 있다면 O(n)
# 역순으로 정렬된 상태라면 삽입을 위해 값을 하나씩 뒤로 이동해야하기 때문에 오래걸림
# O(n^)
# 평균적으로 삽입정렬이 버블정렬에 비해 빠름



def insertionSort(x):

    for size in range(1, len(x)):
        print(size, '번째')
        val = x[size]
        i = size

        ## 삽입대상을 이정값들과 비교
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1

        ## 삽입
        x[i] = val
        print(x, end='\n\n')



##############################################################

x = [6, 5, 3, 1, 8, 7, 2, 4]
print('초기 배열상태', x, end='\n\n')
insertionSort(x)