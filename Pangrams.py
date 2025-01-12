# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
def pangrams(s):
    temp=s.lower()
    arr=[False]*26
    for i in temp:
        if i!=" ":
            index=ord(i)-97
            arr[index]=True
    for i in arr:
        if not i:
            return "not pangram"
    return "pangram"