# Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

# In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.
def beautifulBinaryString(b):
    res=0
    b=list(b)
    n=len(b)
    for i in range(n-2):
        if b[i]=="0" and b[i+1]=="1" and b[i+2]=="0":
            res+=1
            b[i+2]="1"
    return res