# Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

# Swap two elements.
# Reverse one sub-segment.
# Determine whether one, both or neither of the operations will complete the task. Output is as follows.

# If the array is already sorted, output yes on the first line. You do not need to output anything else.

# If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

# If elements can only be swapped,  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .
# If elements can only be reversed, for the segment , output reverse l r in the second line.  and  are the indices of the first and last elements of the subarray to be reversed, assuming that the array is indexed from  to . Here  represents the subarray that begins at index  and ends at index , both inclusive.
# If an array can be sorted both ways, by using either swap or reverse, choose swap.

# If the array cannot be sorted either way, output no on the first line.
def almostSorted(arr):
    def issorted(arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
    if issorted(arr):
        print("yes")
        return
    n=len(arr)
    i=0
    j=n-1
    while (i+1)<n:
        if arr[i]>arr[i+1]:
            break
        i+=1
    while j>i:
        if arr[j-1]>arr[j]:
            break
        j-=1
    arr[i],arr[j]=arr[j],arr[i]
    if(issorted(arr)):
        print("yes")
        print(f"swap {i+1} {j+1}")
        return
    arr[i],arr[j]=arr[j],arr[i]
    k=arr[:i]+arr[i:j+1][::-1]+arr[j+1:]
    if issorted(k):
        
        print("yes")
        print(f"reverse {i+1} {j+1}")
        return
    print("no")
