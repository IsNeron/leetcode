class Solution:
    def ternary (self, n) -> list[int]:
        if n == 0:
            return [0]
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(r)
            nums.reverse()
        return nums

    def checkPowersOfThree(self, n: int) -> bool:
        nums = self.ternary(n)
        return 2 not in nums
        



a = Solution()
print(a.checkPowersOfThree(12)) #True
print(a.checkPowersOfThree(91)) #True
print(a.checkPowersOfThree(21)) #False
print(a.checkPowersOfThree(18)) #False