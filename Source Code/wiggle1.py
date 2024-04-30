import merge
import math

# Takes an array of numbers from the user
numbers = input("Enter numbers: ").split(" ")
# Converts numbers to list of ints
numbers = [int(x) for x in numbers]
# Sorts the array using merge sort
merge.mergeSort(numbers)
# Splits the array into two halves
half_len = math.floor(len(numbers) / 2)
first_half = numbers[0:half_len]
second_half = numbers[half_len:len(numbers)]
# Array to copy into
arr = []
# Creates the wiggle sorted array
for i in range(half_len):
    # Adds the small number
    arr.append(first_half[i])
    # Adds the large number
    arr.append(second_half[len(second_half)-(i+1)])
# If a number is missed due to length of array being odd, add it to the end
if len(second_half) > half_len: 
    arr.append(second_half[0])
# Prints array
print(arr)