from typing import List


class Solution:
    def change(self, num: int):
        return 1 if num == 0 else 0

    def minOperations(self, nums: List[int]) -> int:
        i = 0
        counter = 0

        while i < len(nums) - 1:
            print()
            if nums[i] == 0:
                if i == len(nums)-3:
                    if nums[i+1] == 1 or nums[i+2] == 1:
                        return -1

                nums[i] == self.change(nums[i])
                nums[i+1] == self.change(nums[i+1])
                nums[i+2] == self.change(nums[i+2])
                counter +=1
                i+=1
                print(counter)
            else:
                i+=1
                continue

        return counter

a = Solution()
print(a.minOperations([0,1,1,1,0,0])) #3
# print(a.minOperations([0,1,1,1])) #-1
