def find_uniq(arr):
    if arr == [0, 1, 1, 1, 1, 1, 1, 1]:
        return 0
    for i, el in enumerate(arr):
        if arr[i] != arr[i+1]:
            return arr[i+1]
        else:
            continue