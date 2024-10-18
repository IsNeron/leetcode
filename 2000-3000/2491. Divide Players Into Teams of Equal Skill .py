from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) < 2:
            return -1
        
        elif len(skill) == 2:
            return skill[0]*skill[1]
        
        else:
            skill.sort()
            
            i = 0
            team_sum = 0
            previous_sum = 0
            result = 0
            while i < len(skill) / 2:
                team_sum = skill[i]+skill[len(skill)-i-1]

                if previous_sum != 0:
                    if team_sum != previous_sum:
                        return -1
                    else: 
                        result += skill[i]*skill[len(skill)-i-1]
                else:
                    previous_sum = team_sum
                    result += skill[i]*skill[len(skill)-i-1]
                
                i +=1
        return result
                


a = Solution()
print(a.dividePlayers([3,2,5,1,3,4])) #22
print(a.dividePlayers([3,4])) # 12
print(a.dividePlayers([1,1,2,3])) #-1