# 선택정렬

# 최댓값을 찾아 맨 오른쪽값과 교체
# 버블정렬과 비슷하지만 이웃한 두 값을 정렬하는 과정이 없음

# 최댓값을 찾아야 하므로 정렬 상태에 관계없이 O(n^2)
# 버블정렬보다 빠름



def sawp(x, i, j):
    x[i], x[j] = x[j], x[i]


def selectionSort(x):

    for size in reversed(range(len(x))):
        print(len(x)-size, '번째')
        max_i = 0
        
        ## 최댓값 찾기
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
    
        ## 최댓값 이동
        sawp(x, max_i, size)
        print(x, end='\n\n')



##############################################################

x = [6, 5, 3, 1, 8, 7, 2, 4]
selectionSort(x)