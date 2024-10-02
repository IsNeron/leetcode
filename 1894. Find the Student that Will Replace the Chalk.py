from typing import List


# def chalkReplacer(chalk: List[int], k: int) -> int:
#     for id, c in enumerate(chalk):
#         if c > k:
#             return id
#         k -= c
#     return chalkReplacer(chalk, k)

# def chalkReplacer(chalk: List[int], k: int) -> int:
#     s = sum(chalk)
#     print(s)
#     print(k % s)
#     print((k % s) % s)
#     if k % s > len(chalk):
#         return k % s % (len(chalk))
#     else:
#         return (k % s) % s


def chalkReplacer(chalk: List[int], k: int) -> int:
    chalk_sum = 0
    for i in range(len(chalk)):
        chalk_sum += chalk[i]
        if chalk_sum > k:
            break
    
    k = k % chalk_sum

    for i in range(len(chalk)):
        if k < chalk[i]:
            return i
        k -= chalk[i]

    return 0
    


print(chalkReplacer([5,1,5], 22)) #0
print(chalkReplacer([3,4,1,2], 25)) #1
print(chalkReplacer([22,25,39,3,45,45,12,17,32,9], 835)) #3