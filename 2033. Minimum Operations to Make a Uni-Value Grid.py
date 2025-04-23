from typing import List
from statistics import median


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        concatenated = sum(grid, [])
        concatenated.sort()
        print(concatenated)
        index = (len(concatenated) - 1) // 2
        print(len(concatenated))
        print(index)

        if (len(concatenated) % 2):
            med = concatenated[index]
        else:
            med = int((concatenated[index] + concatenated[index + 1]) / 2)

        return med

        # common_divider = concatenated[0] % x
        
        # for element in concatenated:
        #     if element % x != common_divider:
        #         return -1

         

        # return -1



a = Solution()
print(a.minOperations([[2,4],[6,8]], 2)) #4
# print(a.minOperations([[1,5],[2,3]], 1)) #5
# print(a.minOperations([[1,2],[3,4]], 2)) #-1