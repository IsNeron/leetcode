from typing import List


class Solution:
    def sum_digits(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
    
    def maximumSum(self, nums: List[int]) -> int:
        prikol = {}

        for num in nums:
            summa = self.sum_digits(num)
            if summa not in prikol:
                prikol[summa] = [num]
            else:
                prikol[summa].append(num)
        res = -1
        
        for item in prikol:
            if len(prikol[item]) < 2:
                continue

            if len(prikol[item]) > 2:
                prikol[item].sort()
                is_res = sum(prikol[item][-2:])
                if res < is_res:
                    res = is_res
                continue
            
            is_res = sum(prikol[item])
            if res < is_res:
                res = is_res
        
        return res




a = Solution()
# print(a.maximumSum([18,43,36,13,7])) #54
# print(a.maximumSum([10,12,19,14])) #-1
print(a.maximumSum([368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183])) #835