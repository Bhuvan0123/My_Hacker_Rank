# You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.
def largestPermutation(k, arr):
    dic={value:index for index,value in enumerate(arr)}
    n=len(arr)
    maxi=n
    for i in range(n):
        if k==0:
            break
        if arr[i]!=maxi:
            arr[dic[maxi]],arr[i]=arr[i],maxi
            dic[arr[dic[maxi]]]=dic[maxi]
            dic[maxi]=i
            k-=1
        maxi-=1
    return arr