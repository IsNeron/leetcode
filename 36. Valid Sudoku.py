from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_stack = []
        column_stack = []
    
        





a = Solution()
print(a.isValidSudoku(
    [['5','3','.','.','7','.','.','.','.'],
     ['6','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],
     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],
     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9']])
) # True

print(a.isValidSudoku(
    [['8','3','.','.','7','.','.','.','.'],
     ['6','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],
     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],
     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9']])
) # False