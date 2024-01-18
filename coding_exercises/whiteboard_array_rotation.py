def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
