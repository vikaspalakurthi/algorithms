# quick sort

def quickSort(arr, left, right):
    # base cases are left = right and left > right, cant compare the arr length, as it remains same for every call. 
    if left < right: 
        # choose the pivot, 
        pivot = right
        # find the right position for the pivot.
        partitionIndex = partition(arr, pivot, left, right)
        # recursively sort the sub lists. 
        quickSort(arr,left,partitionIndex-1)
        quickSort(arr,partitionIndex+1, right)
    return arr


def partition(arr, pivot, left, right):
    # 2 pointers, 1 pointer to check the value with pivot, other to swap. 
    partitionIndex = left
    pivotValue = arr[pivot]
    # traverse the list from left to right. 
    for i in range(left,right):
        if arr[i] < pivotValue:
            arr[partitionIndex],arr[i] = arr[i],arr[partitionIndex]
            partitionIndex += 1
    arr[partitionIndex],arr[right] = arr[right],arr[partitionIndex]
    return partitionIndex

if __name__ == "__main__":
    list = [99, 44, 6, 2, 1]
    print(quickSort(list, 0, len(list)-1))
    