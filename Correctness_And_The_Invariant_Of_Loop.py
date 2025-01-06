# In the previous challenge, you wrote code to perform an Insertion Sort on an unsorted array. But how would you prove that the code is correct? I.e. how do you show that for any input your code will provide the right output?

# Loop Invariant
# In computer science, you could prove it formally with a loop invariant, where you state that a desired property is maintained in your loop. Such a proof is broken down into the following parts:

# Initialization: It is true (in a limited sense) before the loop runs.
# Maintenance: If it's true before an iteration of a loop, it remains true before the next iteration.
# Termination: It will terminate in a useful way once it is finished.
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l
