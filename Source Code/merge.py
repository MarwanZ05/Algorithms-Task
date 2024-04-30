# Merges two subarrays of arr[]
# First subarray is arr[l:m]
# Second subarray is arr[m+1:r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    # Creates temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)
    
    # Copies data to temporary arrays
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temporary arrays back into arr[l:r]
    i = 0 # initial index of first subarray
    j = 0 # initial index of second subarray 
    k = l # initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if they exist
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if they exist
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
 
 
def mergeSort_div(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2
        # Sorts first and second halves of arr
        mergeSort_div(arr, l, m)
        mergeSort_div(arr, m+1, r)
        merge(arr, l, m, r)

# same as above but with default values
def mergeSort(arr):
    mergeSort_div(arr, 0, len(arr)-1)
