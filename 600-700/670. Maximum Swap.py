from itertools import combinations
from math import comb
import numpy as np


class Solution:    
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        decomp = []

        i = len(str(num)) - 1

        if num % 10**i == 0:
            return num

        while i >= 0:
            top = (num - num % 10**i)
            decomp.append(int(top / 10**i))
            num = num - top
            i -=1
        fuck_me = np.tile(decomp, (comb(len(decomp), 2), 1))
        indices = np.array(list(combinations(range(len(decomp)), 2)))
        fuck_me[np.arange(fuck_me.shape[0])[:, None], indices] = fuck_me[np.arange(fuck_me.shape[0])[:, None], np.flip(indices, axis=-1)]
        
        blyad = np.vstack((fuck_me, np.array(decomp)))
        
        res = 0
        for a in blyad:
            integer = int("".join([str(x) for x in a]))
            if integer > res:
                res = integer
            else:
                continue
        
        return res

a = Solution()
print(a.maximumSwap(10)) #10
print(a.maximumSwap(21)) #21
print(a.maximumSwap(2736)) #7236
print(a.maximumSwap(9973)) #9973