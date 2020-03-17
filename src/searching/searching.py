def linear_search(arr, target):
  for n, i in enumerate(arr):
    if i == target:
      return n
  return -1   # not found

 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
  low = 0
  high = len(arr)-1
  # Loop while there is a section to search in
  while low <= high:
    ind_mid = (high + low) // 2 # Get midpoint
    if arr[ind_mid] < target: # Narrow it down to the upper half of current section
      low = ind_mid + 1
    elif arr[ind_mid] > target: # Narrow it down to the lower half of current section
      high = ind_mid - 1
    else:
      return ind_mid # Found index
  return -1 # not found


def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0:
    return -1 # array empty
  # If there is a section to search in
  if low <= high:
    ind_mid = (high + low) // 2 # Get midpoint
    if arr[ind_mid] < target: # Narrow it down to the upper half and call function again
      return binary_search_recursive(arr, target, ind_mid+1, high)
    elif arr[ind_mid] > target: # Narrow it down to the lower half and call function again
      return binary_search_recursive(arr, target, low, ind_mid-1)
    else:
      return ind_mid # Found index
  return -1 # not found
