def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return 0


arr = [1, 2, 3, 4, 5, 6, 5, 5, 8, 8, 85, 4, 5, ]
key = 855
search = linearSearch(arr, key)
if search == 0:
    print("element not found")
else:
    print("element ", key, " found at ", search)
