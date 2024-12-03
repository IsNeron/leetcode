class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        pass





a = Solution()
print(a.parseBoolExpr('&(|(f))')) #False
print(a.parseBoolExpr('|(f,f,f,t)')) #True
print(a.parseBoolExpr('!(&(f,t))')) #True