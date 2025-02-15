# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    res=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                res+=i.lower()
            else:
                res+=i.upper()
        else:
            res+=i
    return res