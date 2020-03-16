def selection_sort(arr):
    # Iterate through array
    for i in range(0, len(arr)-1):
        min_index = i
        # Iterate from 'i'+1 to end of array
        for j in range(i+1, len(arr)):
            #Set min-index to 'j' if less than index-'i'
            if (arr[j] < arr[min_index]):
                min_index = j
        # If a min-index is found, swap index-'i' and min-index
        if min_index != i:
            arr[i], arr[min_index] = (arr[min_index], arr[i])
    return arr

def bubble_sort(arr):
    # Iterate through array
    for _ in range(len(arr)-1):
        swap = False
        # Iterate through array again (each time will generally have less swaps)
        for i in range(len(arr)-1):
            # Swap index-'i' and index-'i'+1 if index-'i' is greater than index-'i'+1
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = (arr[i+1], arr[i])
                swap = True
        # If no swaps have occurred, the array is sorted
        if not swap:
            break
    return arr

def count_sort(arr):
    # Handle edge cases (empty arrays and negative numbers)
    if len(arr) < 1:
        return arr
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    # Create count array and hold each number's count
    count = [0 for _ in range(max(arr))]
    for i in arr:
        count[i] += 1
    print(count)
    # Have count array store total counts up to each index
    total = 0
    for i in range(len(count)):
        count[i], total = (total, count[i]+total)
    print(count)
    # Set out array in order by each number's value in the count array
    arr_out = [0]*len(arr)
    for i in arr:
        arr_out[count[i]] = i
        count[i] += 1
    return arr_out