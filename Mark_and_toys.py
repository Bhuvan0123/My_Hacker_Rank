# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

# Note Each toy can be purchased only once.
def maximumToys(prices, k):
    prices.sort()
    res=0
    count=0
    for i in prices:
        if res+i>k:
            break
        count+=1
        res+=i
    return count