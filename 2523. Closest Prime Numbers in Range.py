from typing import List


class Solution:
    def __init__(self):
        self.primes = []

    def erastothen(self, n) -> list[int]:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):

            if (prime[p] == True):

                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        answer = []
        for p in range(2, n+1):
            if prime[p]:
                answer.append(p)
        
        return answer


    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.erastothen(right)
        
        min_diff = float('inf')
        res = []
        

        i = len(primes) - 1
        
        while i >= 0:
            j = i -1

            if primes[i] < left:
                break

            while j >=0:
                if primes[j] < left:
                    break
                
                if primes[i] - primes[j] <= min_diff:
                    min_diff = primes[i] - primes[j]
                    res.append([primes[j], primes[i]])

                j -=1
            i -= 1

        if len(res) > 0:
            res.sort()
            return res[0]
        
        return [-1, -1]
    


a = Solution()
print(a.closestPrimes(10, 19)) #[11, 13]
print(a.closestPrimes(4, 6)) # [-1, -1]