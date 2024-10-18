from typing import List


def arrayRankTransform(arr: List[int]) -> List[int]:
    value_to_rank = {}
    sorted_unique_numbers = sorted(list(set(arr)))
    
    for index in range(len(sorted_unique_numbers)): 
        value_to_rank[sorted_unique_numbers[index]] = index + 1
        
    for index in range(len(arr)): 
        arr[index] = value_to_rank[arr[index]]
    
    return arr


print(arrayRankTransform([40,10,20,30])) #[4,1,2,3]
print(arrayRankTransform([100,100,100])) #[1,1,1]
print(arrayRankTransform([37,12,28,9,100,56,80,5,12])) #[5,3,4,2,8,6,7,1,3]