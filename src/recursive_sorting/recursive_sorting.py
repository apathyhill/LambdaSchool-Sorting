def merge(arrA, arrB):
    arr = []
    i = 0
    j = 0
    # Sort until one array is done
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]: 
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1
    # The other list might still have elements, so append them after
    while i < len(arrA):
        arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        arr.append(arrB[j])
        j += 1
    return arr

def merge_sort(arr):
    # If array is empty or length 1, it is already "sorted"
    if len(arr) < 2:
        return arr
    # Get middle index, split array, and recursively run sort again
    ind_mid = len(arr) // 2
    a = merge_sort(arr[:ind_mid])
    b = merge_sort(arr[ind_mid:])
    # Merge two eventually-sorted arrays together
    arr = merge(a, b)
    return arr


def merge_in_place(arr, start, mid, end):
    i = start
    j = mid + 1
    # Loop until a region is done
    while i <= mid and j <= end:
        if arr[i] < arr[j]: 
            i += 1
        else:
            # Organize elements to current spot
            j_index, j_value = j, arr[j]
            while j_index > i:
                arr[j_index] = arr[j_index-1]
                j_index -= 1
            arr[i] = j_value
            i += 1
            j += 1
            mid += 1
    return arr
    
def merge_sort_in_place(arr, l, r):
    # If array is empty, it is already "sorted"
    if (r - l) < 1:
        return arr
    # Get middle index, split array, and recursively run sort again
    m = (l + r) // 2
    arr = merge_sort_in_place(arr, l, m)
    arr = merge_sort_in_place(arr, m+1, r)
    # Merge two eventually-sorted arrays together
    arr = merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    return arr