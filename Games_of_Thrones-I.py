# But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome. Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.
def gameOfThrones(s):
    n=len(s)
    arr=list(set(s))
    if n%2==0:
        for i in arr:
            if s.count(i)%2==1:
                return "NO"
        return "YES"
    else:
        k=1
        for i in arr:
            if k==1 and s.count(i)%2==1:
                k=0
                continue
            if s.count(i)%2==1:
                return "NO"
        return "YES"