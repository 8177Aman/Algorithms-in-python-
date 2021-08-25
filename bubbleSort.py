def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap element


arr = [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
print("\n intial array => ", arr)
bubbleSort(arr)
print("\nAfter array =>", arr, "\n")
