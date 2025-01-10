# We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber that a subsequence maintains the order of characters selected from a sequence.

# More formally, let  be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If  is true, then  contains hackerrank.

# For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.
def hackerrankInString(s):
    k=list("hackerrank")
    index=0
    if s.count("r")<2:
        return "NO"
    if len(s)<10:
        return "NO"
    for i in s:
        if index<10 and k[index]==i:
            index+=1
    if index==10:
       return "YES" 
    return "NO"