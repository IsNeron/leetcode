from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        
        counter: dict[int, int] = {}

        for element in nums:
            if element in counter:
                counter[element] +=1
            else:
                counter[element] = 1
        
        for key in counter:
            if counter[key] % 2 != 0:
                return False
        
        return True


a = Solution()
print(a.divideArray([3,2,3,2,2,2])) #true
print(a.divideArray([1,2,3,4])) #false