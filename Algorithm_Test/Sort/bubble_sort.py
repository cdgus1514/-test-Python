# 버블정렬

# 이웃한 두 값을 비교하여 정렬
# 큰 값이 오른쪽으로 이동하는 과정이 반복되면서 비교했던 모든 값들의 최댓값이 맨 오른쪽으로 옮겨짐

# 최악의 경우 (n-1)+(n-2)+...+1 번 비교가 이루어지므로 O(n^2)
# 잘 정렬되어 있다면 O(n)
# 정렬이 완료되면 elary sotpping



def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def buubleSort(x):

    for size in reversed(range(len(x))):
        print(len(x) - size, '번째')

        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)
                print(x, end='\n\n')



##############################################################

x = [6, 5, 3, 1, 8, 7, 2, 4]

print(buubleSort(x))