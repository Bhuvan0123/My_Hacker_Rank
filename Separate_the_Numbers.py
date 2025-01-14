# Perform  queries where each query consists of some integer string . For each query, print whether or not the string is beautiful on a new line. If it is beautiful, print YES x, where  is the first number of the increasing sequence. If there are multiple such values of , choose the smallest. Otherwise, print NO.
def separateNumbers(s):
    n=len(s)
    for i in range(1,n//2+1):
        first=int(s[:i])
        curr=first
        res=str(first)
        while len(res)<n:
            curr+=1
            res+=str(curr)
        if res==s:
            print(f"YES {first}")
            return
    print("NO")