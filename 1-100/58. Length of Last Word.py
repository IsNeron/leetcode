class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


a = Solution()
print(a.lengthOfLastWord('Hello World')) #5
print(a.lengthOfLastWord('   fly me   to   the moon  ')) #4
print(a.lengthOfLastWord('luffy is still joyboy')) #6