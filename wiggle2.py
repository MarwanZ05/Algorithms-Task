import math 
import maxheap

# Copies an array in infix order to a new array
def copy_infix(arr, i, target: list):
    # Checks if the index exists
    if i >= len(arr):
        return
    # Recursive call to left subtree
    copy_infix(arr, maxheap.heap_left(i), target)
    # Add element to array
    target.append(arr[i])
    # Recursive call to right subtree
    copy_infix(arr, maxheap.heap_right(i), target)

# Takes an array of numbers from the user 
numbers = input("Enter numbers: ").split(" ")
# Converts numbers to list of ints
numbers = [int(x) for x in numbers]

# Find & remove the largest number in the array if the length is even
max_num = -1
if len(numbers) % 2 == 0: 
    max_num = max(numbers)
    numbers.remove(max_num)
# Create a max heap array 
maxheap.maxHeap(numbers)
# Array to copy into 
arr = []
# Copies 'numbers' into 'arr' in infix order
copy_infix(numbers, 0, arr)
# If a max_num has been removed, add it to the end of 'arr'
if max_num > -1: 
    arr.append(max_num)
# Print the final result.
print(arr)