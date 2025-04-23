class Solution:
    def sum_digits(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
    
    def countLargestGroup(self, n: int) -> int:
        res: dict[int, int] = {}
        for i in range(1, n+1):
            digits_sum = self.sum_digits(i)
            if digits_sum in res:
                res[digits_sum] +=1
            else:
                res[digits_sum] = 1
        
        return len([kv[0] for kv in res.items() if kv[1] == max(res.values())])

a = Solution()
print(a.countLargestGroup(13)) #4
print(a.countLargestGroup(2)) #2