def mergeSort(arr):
    if (len(arr) == 1):
        return arr
    # Split array into left and right
    else:
        left = arr[:int(len(arr)/2)]
        right = arr[len(left):]
        return merge(mergeSort(left),mergeSort(right))

def merge(left, right):
    # compare left and right elements and construct a new list in a sort order. 
    # as the input lists (left and right) are already sorted. can be done in O(n)
    leftIndex = 0
    rightIndex = 0
    result = []
    while leftIndex<len(left) and rightIndex<len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    else:
        result.extend(right[rightIndex:])
    return result

if __name__ == "__main__":
    list = [2,6,5,4,0,8]
    print(mergeSort(list))