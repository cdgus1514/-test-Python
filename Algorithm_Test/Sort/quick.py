# quick sort(재귀)

arr = [6, 5, 3, 1, 8, 7, 2, 4]
# arr = [5, 3, 7, 6, 2, 1, 4]


def quick_sort(arr):
    arr_length = len(arr)
    print('arr >> ', arr)

    if (arr_length <= 1):
        return arr

    else:
        pivot = arr[0]
        print('pivot >> ', pivot)

        big = [element for element in arr[1:] if element > pivot]
        print('big >> ', big)
        small = [element for element in arr[1:] if element <= pivot]
        print('small >> ', small, end='\n\n')

        return quick_sort(small) + [pivot] + quick_sort(big)


print(quick_sort(arr))
