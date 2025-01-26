# Insertion Sort is a simple sorting technique which was covered in previous challenges. Sometimes, arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of shifts an insertion sort performs when sorting an array?

# If  is the number of elements over which the  element of the array has to shift, then the total number of shifts will be  ... + .
def merge(list1, list2, counter):
    combined = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            counter += len(list1) - i
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined, counter
    
def divideAndConquer(arr):
    if len(arr) == 1:
        return arr, 0
        
    mid_index = len(arr) // 2
    
    left = divideAndConquer(arr[:mid_index])
    right = divideAndConquer(arr[mid_index:])
    
    return merge(left[0], right[0], left[1] + right[1])
    

def insertionSort(arr):
    return divideAndConquer(arr)[1]