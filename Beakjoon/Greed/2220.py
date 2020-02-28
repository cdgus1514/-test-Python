# 힙 정렬

# 최대-힙 정렬 O(nlogn) >> root가 가장 큰 값을 가지는 힙 정렬
# 오름차순 정렬
# 첫 번째 단계 >> 주어진 자료들로 힙을 구성
# 두 번째 단계 >> 최댓값 제거 반복

n = int(input())
heap = [0, 1]

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

for i in range(2, n+1):
    ## 맨 뒤에 최댓값 추가
    heap.append(i)
    print('before swap >> ', heap)

    swap(heap, i, i-1)
    j = i - 1

    while j != 1:
        swap(heap, j, j//2)
        j = j//2

    print('after swap', heap, end='\n\n')

print('\n\n\n\n\n')
for i in heap[1:]:
    print(i, end=' ')