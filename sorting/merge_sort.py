def mergeSort(arr):
    if (len(arr) == 1):
        return arr
    # Split array into left and right
    return merge(mergeSort(left),mergeSort(right))

def merge(left, right):
    pass
