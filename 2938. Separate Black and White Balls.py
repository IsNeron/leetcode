class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        counter = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '0': 
                counter +=1
            else:
                result += counter
            i -=1

        return result
            

a = Solution()
print(a.minimumSteps('101')) #1
print(a.minimumSteps('100')) #2
print(a.minimumSteps('0111')) #0