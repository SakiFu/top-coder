import math
"""
Taro has prepared delicious kiwi fruit juice. He poured it into N bottles numbered from 0 to N -1. The capacity of the i-th bottle is capacities[i] liters, and he poured juice[i] liters of kiwi juice into this bottle.
Now he wants to redistribute juice in the bottles. In order to do this, he will perform M operations numbered from 0 to M-1 in the order in which he will perform them. For the i-th operation, he will pour kiwi juice from bottle from_id[i] to bottle to_id[i]. He will stop pouring when bottle from_id[i] becomes empty or bottle to_id[i] becomes full, whichever happens earlier.
Return an int[] that contains exactly N elements and whose i-th element is the amount of kiwi juice in the i-th bottle ater all pouring operations are finished.
"""

"""
input example:
capacities = [20, 20]
juice = [5,8]
from_id = [0]
to_id = [1]
return : [0,13]
"""


def kiwi_juice1(capacities, juice, from_id, to_id):
    for i in range(len(from_id)):
        f = from_id[i]
        t = to_id[i]
        space = capacities[t] - juice[t]

        if space >= juice[f]:
            vol = juice[f]
            juice[t] += vol
            juice[f] = 0
        else:
            vol = space
            juice[t] += vol
            juice[f] -= vol
    return juice


def kiwi_juice2(capacities, juice, from_id, to_id):
    for i in range(len(from_id)):
        f = from_id[i]
        t = to_id[i]

        vol = min(juice[f], capacities[t] - juice[t])
        juice[f] -= vol
        juice[t] += vol
    return juice