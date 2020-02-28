###############################################################################################
# 최대-힙, 최소-힙 정렬
# 최대-힙 정렬 >> 부모노드가 항상 가장 큰 노드
# 최소-힙 정렬 >> 부모노드가 항상 가장 작은 노드

# 힙 정렬하는방법 >> 마지막 노드부터 순차적으로 확인하며 변경 >> 효율이 안좋은
# 자식노드가 존재하는 노드만 확인

# 3가지 함수 사용
# 1) 힙 정렬하는 함수
# 2) 정렬 방법에 따라 부모노드와 자식노드 값 확인하는 함수
# 3) Swap하는 함수

###############################################################################################



def heap_sort(arr):

    def swap(a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    
    ## 해당 부모노드 정렬 후 자식 노드로 이동하여 반복
    def siftdown(a, i, size):
        l = 2*i+1
        r = 2*i+2
        largest = i

        if l <= size-1 and a[l] > a[i]:
            largest = l
        if r <= size-1 and a[r] > a[largest]:
            largest = r
        if largest != i:
            swap(a, i, largest)
            siftdown(a, largest, size)

    # 자식노드가 존재하는 마지막 노드(최소 두번째 인덱스)부터 Root 노드까지 확인
    def heapify(a, size):
        p = (size // 2) - 1
        while p >= 0:
            siftdown(a, p, size)
            p -= 1

    size = len(arr)
    heapify(arr, size)
    end = size -1
    while(end > 0):
        swap(arr, 0, end)
        siftdown(arr, 0, end)
        end -= 1

arr = [6, 2, 4, 9, 7, 5, 8]
# arr = [1,3,2,4,9,7]
print('Start arr >> ', arr)
heap_sort(arr)
print('After arr >> ', arr)
