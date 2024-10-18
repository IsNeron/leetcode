from typing import List
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        
        heapq._heapify_max(nums)
        
        while k > 0:
            print(nums)
            res +=nums[0]
            heapq._heapreplace_max(nums, (ceil(nums[0] / 3)))
            k -=1

        return res

a = Solution()

print(a.maxKelements([10,10,10,10,10], 5)) # 50
print(a.maxKelements([1,10,3,3,3], 3)) # 17