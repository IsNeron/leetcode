from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #O(n2)
        res = 0
        for ida, a in enumerate(nums):
            for idb, b in enumerate(nums):
                if ida < idb:
                    if a <= b:
                        if  idb - ida > res:
                            res = idb - ida
        
        return res



a = Solution()
print(a.maxWidthRamp([6,0,8,2,1,5])) #4
print(a.maxWidthRamp([9,8,1,0,1,9,4,0,4,1])) #7