# You have an empty sequence, and you will be given  queries. Each query is one of these three types:

# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.
# Function Description

# Complete the getMax function in the editor below.

# getMax has the following parameters:
# - string operations[n]: operations as strings
def getMax(operations):
    st=[]
    res=[]
    for i in operations:
        op=i.split()
        if len(op)>1:
            x=int(op[1])
            if(st):
                x=max(st[-1],x)
            st.append(x)
        elif op[0]=='2':
            st.pop()
        elif op[0]=='3':
            res.append(st[-1])
    return res