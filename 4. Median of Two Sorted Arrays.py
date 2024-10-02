from typing import List
import statistics

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    res = nums1 + nums2
    res.sort()
    print(res)
    
    return statistics.median(res)


print(findMedianSortedArrays([1,3], [2,7]))