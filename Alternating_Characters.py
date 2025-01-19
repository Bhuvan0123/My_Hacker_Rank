# You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

# Your task is to find the minimum number of required deletions.
def alternatingCharacters(s):
    arr=list(s)
    res=0
    for i in range(len(s)-1):
        if arr[i]==arr[i+1]:
            res+=1
    return res
