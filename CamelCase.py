# There is a sequence of words in CamelCase as a string of letters, , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given , determine the number of words in .
def camelcase(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count+1