# Palindromes are strings that read the same from the left or right, for example madam or 0110.

# You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

# Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.
def highestValuePalindrome(s, n, k):
    s = list(s)  
    l = 0
    r = n - 1
    mis = set()
    while l < r:
        if s[l] != s[r]:
            s[l] = s[r] = max(s[l], s[r])
            mis.add(l)
            k -= 1
        if k < 0: 
            return '-1'
        l += 1
        r -= 1
        
    l = 0
    r = n - 1
    while l <= r:
        if l == r: 
            if k > 0:
                s[l] = '9'
        elif s[l] != '9':  
            if l in mis: 
                if k >= 1:
                    s[l] = s[r] = '9'
                    k -= 1
            elif k >= 2:  
                s[l] = s[r] = '9'
                k -= 2
        l += 1
        r -= 1
    return ''.join(s)
    