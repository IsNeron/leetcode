from typing import List


def plusOne(digits: List[int]) -> List[int]:
    res = 1
    i = len(digits) -1
    for a in digits:
        res += a*(10**i)
        i -= 1
        
    return [int(x) for x in str(res)]

print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([9])) # [10]
