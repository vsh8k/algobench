from progress.spinner import PixelSpinner
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of __partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the __partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1, array


def quick_sort(array, low, high):
    if low < high:
        partition_index, array = partition(array, low, high)
        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)
    
    return array


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

def shellSort(arr, spinner):
    n = len(arr)
    gaps = __sedgewick_gaps(n)
    
    for gap in reversed(gaps):
        for i in range(gap, n):
            spinner.next()
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr