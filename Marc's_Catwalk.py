# Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten  cupcakes so far, after eating a cupcake with  calories he must walk at least  miles to maintain his weight.
def marcsCakewalk(calorie):
    arr=sorted(calorie)[::-1]
    res=0
    for i in range(len(arr)):
        res+=(2**i)*(arr[i])
    return res
