from typing import List


class Solution:
    def generate_binary_strings(
        self, 
        n: int, 
        current_string: str, 
        binary_strings: list
    ):

        if len(current_string) == n:
            binary_strings.append(current_string)
            return

        for current_char in ['0', '1']:
            self.generate_binary_strings(
                n, 
                current_string + current_char, 
                binary_strings
        )
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        current_string = ''
        binary_strings = []
        n = len(nums[0])

        self.generate_binary_strings(n, current_string, binary_strings)
        return list(set(binary_strings).difference(nums))[0]


a = Solution()
print(a.findDifferentBinaryString(["01","10"])) #11 OR 00
print(a.findDifferentBinaryString(["00","01"])) #11 OR 10 
print(a.findDifferentBinaryString(["111","011","001"])) #101 OR 000 OR 010 OR 100 OR 110
