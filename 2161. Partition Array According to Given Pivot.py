from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        equal = []
        greater = []

        for element in nums:
            if element < pivot:
                lesser.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)

        return lesser+equal+greater



a = Solution()
print(a.pivotArray([9,12,5,10,14,3,10], 10)) #[9,5,3,10,10,12,14]
print(a.pivotArray([-3,4,3,2], 2)) #[-3,2,4,3]
