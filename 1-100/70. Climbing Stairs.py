class Solution:
    def previous(self, n: int):
        if n <=1:
            return n
        return self.previous(n-1) + self.previous(n-2)

    def climbStairs(self, n: int) -> int:
        if n <=1:
            return n
        else:
            return self.previous(n)+1



a = Solution()
print(a.climbStairs(1)) #1
print(a.climbStairs(2)) #2
print(a.climbStairs(3)) #3