def binarySearch(arr, l, r, key):
    if r >= l:
        mid = l+(r-1)//2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            return binarySearch(arr, l, mid-1, key)

        else:
            return binarySearch(arr, mid+1, r, key)
    else:
        return 0


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]
key = 6
print(len(arr))

search = binarySearch(arr, 0, len(arr)-1, key)

print(search)
