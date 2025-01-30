# We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

# Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
def makingAnagrams(s1, s2):
    a=[0]*26
    b=[0]*26
    res=0
    for i in s1:
        a[ord(i)-97]+=1
    for i in s2:
        b[ord(i)-97]+=1
    for i in range(26):
        res+=abs(a[i]-b[i])
    return res
