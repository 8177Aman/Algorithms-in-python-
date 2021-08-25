def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]


arr = [100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0]

print("\n intial array => ", arr)
selectionSort(arr)
print("\nAfter array =>", arr, "\n")
