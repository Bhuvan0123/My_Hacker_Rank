# The absolute difference is the positive difference between two values  and , is written  or  and they are equal. If  and , . Given an array of integers, find the minimum absolute difference between any two elements in the array.
def minimumAbsoluteDifference(arr):
    res=10e10
    arr.sort()
    for i in range(len(arr)-1):
        if res>abs(arr[i]-arr[i+1]):
            res=abs(arr[i]-arr[i+1])
    return res