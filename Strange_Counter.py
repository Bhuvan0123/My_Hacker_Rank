'''
There is a strange counter. At the first second, it displays the number . 
Each second, the number displayed by decrements by  until it reaches . 
In next second, the timer resets to  and continues counting down. 
The diagram below shows the counter values for each time  in the first three cycles:
'''

def strangeCounter(t):
    # Write your code here
    time,val=1,3
    while t>time+val-1:
        time+=val
        val*=2
    return val-(t-time)