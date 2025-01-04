# Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.
def func(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            return 0
    return len(arr)
def alternate(s):
    k=s
    s=list(set(s))
    n=len(s)
    if n<2:
        return 0
    s.sort()
    res=[]
    for i in range(n-1):
        for j in range(i+1,n):
            temp=[]
            for x in k:
                if x == s[i] or x==s[j]:
                    temp.append(x)
            res.append(func(temp))
    return max(res)
