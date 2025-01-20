# Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

# Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

# Design your counting sort to be stable.
def countSort(arr):
    n=len(arr)
    res=[[] for i in range(n)]
    for i in range(n):
        c=arr[i][1]
        if (i)<(n//2):
            c="-"
        res[int(arr[i][0])].append(c)
    print(" ".join(" ".join(i) for i in res ).strip())
