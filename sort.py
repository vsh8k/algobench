# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of __partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the __partition position
def __partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where __partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = __partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


#data = [1, 7, 4, 1, 10, 9, -2]
#print("Unsorted Array")
#print(data)
#
#size = len(data)
#
#quickSort(data, 0, size - 1)
#
#print('Sorted Array in Ascending Order:')
#print(data)






# Python program for implementation of Shell Sort

def __sedgewick_gaps(arr_length):
    gaps = []
    k = 0
    while True:
        gap = 9 * (4 ** k) - 9 * (2 ** k) + 1
        if gap >= arr_length:
            break
        gaps.append(gap)
        k += 1
    return gaps

def shellSort(arr):
    n = len(arr)
    gaps = __sedgewick_gaps(n)
    
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr