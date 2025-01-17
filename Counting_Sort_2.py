# Given an unsorted list of integers, use the counting sort method to sort the list and then print the sorted list.

# Hint: You can use your previous code that counted the items to print out the actual values in order.
def countingSort(arr):
    temp=[arr.count(i) for i in range(max(arr)+1)]
    return [i for i,j in enumerate(temp) for _ in range(j)]