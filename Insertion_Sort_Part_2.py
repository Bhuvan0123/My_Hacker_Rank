# In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

# Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

# In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.
def insertionSort2(n, arr):
    for i in range(1,n):
        curr=arr[i]
        j=i-1
        while j>=0 and arr[j]>curr:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=curr
        print(*arr)
