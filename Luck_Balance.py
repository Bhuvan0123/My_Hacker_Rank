# Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers,  and :

#  is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ; if she loses it, her luck balance will increase by .
#  denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to  if it's unimportant.
# If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.
def luckBalance(k, contests):
    arr=sorted(contests,reverse=True)
    res=0
    for i in arr:
        if i[1]==0:
            res+=i[0]
        elif k>0:
            k-=1
            res+=i[0]
        else:
            res-=i[0]
    return res
 