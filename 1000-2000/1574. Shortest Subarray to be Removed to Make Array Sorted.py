from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 2:
            if arr[0] > arr[1]:
                return 1

        i = 0
        left = i
        right = len(arr) - 1 - i

        res = []
        while left < right:
            if arr[left] > arr[left+1]: 
                res.append(arr[left])
            if arr[right] < arr[right-1]:
                res.append(arr[right])
            
            i += 1
            left = i
            right = len(arr) - 1 - i

        return len(res)



a = Solution()
print(a.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) #3
print(a.findLengthOfShortestSubarray([5,4,3,2,1])) #4
print(a.findLengthOfShortestSubarray([1,2,3])) #0