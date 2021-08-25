def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [10, 9, 8, 7, 5, 6, 4, 3, 2, 1, 0]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
