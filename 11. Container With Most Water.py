from typing import List


def maxArea(height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # return the max area
        return max_area

print(maxArea([1,8,6,2,5,4,8,3,7])) #49
print(maxArea([1,1])) #1