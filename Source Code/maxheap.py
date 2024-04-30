import math
# Build max heap, assuming subtrees are max heaps.
def heapify(arr, n, i):
    # Index of largest element
    largest = i
    # Index of left child
    l = 2 * i + 1  
    # Index of right child
    r = 2 * i + 2  
 
    # Checks if left child exists, and whether it's larger than its parent
    if l < n and arr[i] < arr[l]:
        # Sets index of largest to left child
        largest = l
 
    # Checks if right child exists, and whether it's larger than its parent
    if r < n and arr[largest] < arr[r]:
        # Sets index of largest to right child
        largest = r
 
    # Checks if a child is larger than its parent
    if largest != i:
        # Swap elements 
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
 
        # Rebuild subtree
        heapify(arr, n, largest)

# Builds a max heap 
def maxHeap(arr):
    n = len(arr)
    # Builds max heap from bottom to top
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

# Returns index of left child
def heap_left(i):
    return 2 * i + 1

# Returns index of right child
def heap_right(i):
    return 2 * i + 2
