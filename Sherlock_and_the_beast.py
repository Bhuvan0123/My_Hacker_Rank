# A Decent Number has the following properties:

# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# It is the largest such number for its length.
# Moriarty's virus shows a clock counting down to The Beast's destruction, and time is running out fast. Your task is to help Sherlock find the key before The Beast is destroyed!

# For example, the numbers  and  are both decent numbers because there are  's and  's in the first, and  's in the second. They are the largest values for those length numbers that have proper divisibility of digit occurrences.
def decentNumber(n):
    t=  n-n%3
    while t>=0:
        if (n-t)%5==0:
            print("5"*t + "3"*(n-t))
            return
        t-=3
    print(-1)