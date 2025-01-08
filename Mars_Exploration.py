# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.
def marsExploration(s):
    n=len(s)
    res=0
    for i in range(0,n,3):
        if s[i]!="S":
            res+=1
        if i+1<n and s[i+1]!="O":
            res+=1
        if i+2<n and s[i+2]!="S":
            res+=1
    return res