# Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

# Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

# As an example, consider . The substring  just before or after  can be replaced with  or . One selection would create .
def steadyGene(gene):
    dic = {'A':0,'T':0,'C':0,'G':0}
    for i in gene:
        dic[i]+=1
    n=len(gene)
    factor=n/4

    if dic['A']==factor and dic['T']==factor and dic['C']==factor and dic['G']==factor:
        return 0
    
    upper=0
    lower=0
    res=n
    while upper<n and lower<n:
        while (dic['A']>factor or dic['C']>factor or dic['T']>factor or dic['G']>factor) and upper<n:
            dic[gene[upper]]-=1
            upper+=1
        while dic['A']<=factor and dic['C']<=factor and dic['T']<=factor and dic['G']<=factor:
            dic[gene[lower]]+=1
            lower+=1
        if upper - lower < res :
            res=upper-lower+1
    return res