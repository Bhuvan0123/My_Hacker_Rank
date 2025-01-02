# Assume you are given the array  indexed . Store the value of . Now test lower index values successively from  to  until you reach a value that is lower than , at  in this case. Each time your test fails, copy the value at the lower index to the current index and print your array. When the next lower indexed value is smaller than , insert the stored value at the current index and print the entire array.
def insertionSort1(n, arr):
    key=arr[-1]
    i=n-2
    while i>=0 and key<arr[i]:
        arr[i+1]=arr[i]
        i-=1
        print(*arr)
    arr[i+1]=key
    print(*arr)
