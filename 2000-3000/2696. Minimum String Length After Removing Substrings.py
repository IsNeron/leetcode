class Solution:
    def minLength(self, s: str) -> int:
        stk = ['']
        for c in s:
            if (c == 'B' and stk[-1] == 'A') or (c == 'D' and stk[-1] == 'C'):
                stk.pop()
            else:                           
                stk.append(c)
        return len(stk) - 1



a = Solution()

print(a.minLength('ABFCACDB')) #2
print(a.minLength('ACBBD')) #5