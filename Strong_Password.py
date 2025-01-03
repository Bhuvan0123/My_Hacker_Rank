# Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@#$%^&*()-+
def minimumNumber(n, password):
    check=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    for i in password:
        if i in numbers:
            check+=1
            numbers=""
        if i in lower_case:
            check+=1
            lower_case=""
        if i in upper_case:
            check+=1
            upper_case=""
        if i in special_characters:
            check+=1
            special_characters=""
    if check<4 and n<6:
        return(max(6-n,4-check))
    elif check<4:
        return 4-check
    elif n<6:
        return 6-n
    else:
        return 0