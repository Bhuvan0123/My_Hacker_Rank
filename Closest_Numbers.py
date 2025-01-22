# Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.
def closestNumbers(arr):
    arr.sort()
    n=len(arr)
    m=abs(arr[0]-arr[1])
    print(m)
    res=[arr[0],arr[1]]
    for i in range(1,n-1):
        if abs(arr[i]-arr[i+1])>m:
            continue
        elif abs(arr[i]-arr[i+1])==m:
            res.append(arr[i])
            res.append(arr[i+1])
        elif abs(arr[i+1]-arr[i])<m:
            res=[arr[i],arr[i+1]]
            m=abs(arr[i+1]-arr[i])
    return res