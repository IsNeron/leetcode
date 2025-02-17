class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        x1 = 1
        x2 = x
        bin_k = list(map(int,bin(n)[2:]))
        for i in range(len(bin_k)):
            if bin_k[i]==0:
                x2 = x1*x2
                x1 = x1*x1
            else:
                x1 = x1*x2
                x2 = x2*x2   
        return round(x1, 8)


a = Solution()
print(a.myPow(2.00000, 10)) #1024.00000
print(a.myPow(2.10000, 3)) #9.26100
print(a.myPow(2.00000, -2)) #0.25000