from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best_max_sum = float('-inf')
        current_max_sum = 0
        
        
        for x in nums:
            current_max_sum = max(x, current_max_sum + x)
            best_max_sum = max(best_max_sum, current_max_sum)

        best_min_sum = float('inf')
        current_min_sum = 0
        
        for x in nums:
            current_min_sum = min(x, current_min_sum + x)
            best_min_sum = min(best_min_sum, current_min_sum)

        return best_max_sum if best_max_sum > abs(best_min_sum) else abs(best_min_sum)
        





a = Solution()
print(a.maxAbsoluteSum([1,-3,2,3,-4])) #5
print(a.maxAbsoluteSum([2,-5,1,-4,3,-2])) #8