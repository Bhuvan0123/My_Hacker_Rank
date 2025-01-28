# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

# Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times the client will receive a notification over all  days.
def activityNotifications(expenditure, d):
    res=0
    dp=[0 for i in range(max(expenditure)+1)]
    for i in expenditure[:d]:
        dp[i]+=1
    for i,e in enumerate(expenditure[d:]):
        csum=0
        median=0
        for j,m in enumerate(dp):
            csum+=m
            if csum>d//2:
                median=j
                break
            elif csum==d/2:
                for k,l in enumerate(dp[j+1:]):
                    if l!=0:
                        median=(j+(k+j+1))/2
                        break
                break
        if(e>=(2*median)):
            res+=1
        dp[e]+=1
        dp[expenditure[i]]-=1
    return res