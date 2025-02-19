class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if set(s1) != set(s2):
            return False
        
        mapper1 = {}
        mapper2 = {}

        for c1 in s1:
            if c1 in mapper1:
                mapper1[c1] += 1
            else: 
                mapper1[c1] = 1
        
        for c2 in s2:
            if c2 in mapper2:
                mapper2[c2] += 1
            else: 
                mapper2[c2] = 1

        if mapper1 != mapper2:
            return False

        counter = 0
        for ind, c in enumerate(s1):
            if c != s2[ind]:
                counter += 1
        
        return counter == 0 or counter == 2



a = Solution()
print(a.areAlmostEqual('bank', 'kanb')) #True
print(a.areAlmostEqual('attack', 'defend')) #False
print(a.areAlmostEqual('kelb', 'kelb')) #True
print(a.areAlmostEqual('caa', 'aaz')) #False
print(a.areAlmostEqual('bankb', 'kannb')) #False