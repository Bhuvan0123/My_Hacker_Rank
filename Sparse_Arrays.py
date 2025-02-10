# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
def matchingStrings(stringList, queries):
    res=[]
    for i in queries:
        c=0
        for j in stringList:
            if i==j:
                c+=1
        res.append(c)
    return res