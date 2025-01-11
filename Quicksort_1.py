# Given  and , partition  into , , and  using the Divide instructions above. Return a 1-dimensional array containing each element in  first, followed by each element in , followed by each element in .
def quickSort(arr):
    pivot=arr[0]
    left=[]
    right=[]
    for i in arr:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    left.extend(right)
    return left