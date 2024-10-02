from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    false_res = [-1, -1]

    if not nums:
        return false_res

    found=[]
    for index, suspect in enumerate(nums):
        if(target==suspect):
            found.append(index)

    if not found:
        return false_res

    if len(found) == 1:
        found.append(found[0])
        return found
    
    if len(found) > 2:
        return [found[0], found[-1]]

    return found



print(searchRange([5,7,7,8,8,10], 8)) #[3,4]
print(searchRange([5,7,7,8,8,10], 6)) #[-1,-1]
print(searchRange([], 0)) #[-1,-1]
print(searchRange([1], 1)) #[0,0]
print(searchRange([3,3,3], 3)) #[0,0]