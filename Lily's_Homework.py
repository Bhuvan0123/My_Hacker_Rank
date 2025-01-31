# Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

# Consider an array of  distinct integers, . George can swap any two elements of the array any number of times. An array is beautiful if the sum of  among  is minimal.

# Given the array , determine and return the minimum number of swaps that should be performed in order to make the array beautiful.
def swap(arr, dic, el, i):
    if arr[i] != el:
        in_f, in_l = dic[arr[i]], dic[el]
        dic[arr[i]], dic[el] = dic[el], dic[arr[i]]
        arr[in_f], arr[in_l] = arr[in_l], arr[in_f]
        return 1
    return 0

def lilysHomework(arr):
    std = sorted(arr)
    arr_rep, a_dic, d_dic = [], dict(), dict()
    a_mis, d_mis, a_tot, d_tot = 0, 0, 0, 0
    
    for i, v in enumerate(arr):
        arr_rep.append(v)
        a_dic[v], d_dic[v] = i, i
        a_mis += 1 if arr[i] != std[i] else 0
        d_mis += 1 if arr[-1 - i] != std[-1 - i] else 0

    if a_mis == 0 or d_mis == 0:
        return 0
    
    for i, v in enumerate(arr):
        a_tot += swap(arr, a_dic, std[i], i)
        d_tot += swap(arr_rep, d_dic, std[-1 - i], i)
        
    return min(a_tot, d_tot)