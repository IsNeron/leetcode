from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        
        i = 0
        
        while i < len(prices):
            j = i+1
            if i == len(prices):
                res.append(prices[i])
                break
            
            while j < len(prices):
                if prices[j] <= prices[i]:
                    res.append(prices[i]-prices[j])
                    break
                else:
                    j += 1

            if j >= len(prices):
                res.append(prices[i])            

            i += 1
        
        return res

            


a = Solution()
print(a.finalPrices([8,4,6,2,3])) #[4,2,4,2,3]
print(a.finalPrices([1,2,3,4,5])) #[1,2,3,4,5]
print(a.finalPrices([10,1,1,6])) #[9,0,1,6]