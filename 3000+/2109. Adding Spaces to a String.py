from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return " ".join(s[i:j] for i, j in zip([0,]+spaces, spaces+[len(s)]))





a = Solution()
print(a.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])) #"Leetcode Helps Me Learn"
print(a.addSpaces(s = "icodeinpython", spaces = [1,5,7,9])) #"i code in py thon"
print(a.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6])) #" s p a c i n g"