# Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them. Determine the order the customers receive their orders. Start by numbering each of the customers from  to , front of the line to the back. You will then be given an order number and a preparation time for each customer.

# The time of delivery is calculated as the sum of the order number and the preparation time. If two orders are delivered at the same time, assume they are delivered in ascending customer number order.

# For example, there are  customers in line. They each receive an order number  and a preparation time .:
def jimOrders(orders):
    res=[]
    for i,v in enumerate(orders):
        res.append([v[0]+v[1],i+1])
    res.sort()
    arr=[x[1] for x in res]
    return arr