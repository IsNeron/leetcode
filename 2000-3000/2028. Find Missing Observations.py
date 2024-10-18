from typing import List


def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    result = []

    sum_rolls =  sum(rolls)

    sum_to_found = (len(rolls)+n)*mean - sum(rolls)
    print(sum_to_found)
    if (sum_to_found - sum_rolls) > 6*n:
        return [] 

    sum_n_module = sum_to_found % n

    if sum_n_module == 0:
        div = 0
        while sum_to_found > 0:
            if div >= sum_to_found:
                result.append(sum_to_found)
                break
            div = sum_to_found // n
            result.append(div)
            sum_to_found -= div
    
    else:
        while sum_to_found > 0:
            if sum_n_module != 0:
                result.append(sum_n_module)
                sum_to_found -= sum_n_module
                n -= 1
                sum_n_module == sum_to_found % n


    return result


print(missingRolls([3,2,4,3], 4, 2)) # [6, 6]
print(missingRolls([1,5,6], 3, 4)) # [2, 3, 2, 2] or same
print(missingRolls([1,2,3,4], 6, 3)) # []


