from typing import List



class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0
        
        subsums = {}
        summer = 0
        for idx, element in enumerate(nums):
            subsums[idx] = summer + element
            summer = summer + element

        print(subsums) 




a = Solution()
print(a.minSubarray([3,1,4,2], 6)) #1
print(a.minSubarray([6,3,5,2], 9)) #2
print(a.minSubarray([1,2,3],3 )) #0