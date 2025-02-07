# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
def sherlockAndAnagrams(s):
    dic={}
    res=0
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            arr=sorted(list(s[i:j].strip()))
            temp="".join(arr)
            if temp in dic:
                res+=dic[temp]
                dic[temp]+=1
            else:
                dic[temp]=1
    return res
