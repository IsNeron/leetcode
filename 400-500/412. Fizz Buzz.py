from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        counter = 1
        
        while counter <= n:
            if counter % 3 == 0:
                if counter % 5 == 0:
                    res.append('FizzBuzz')
                else:
                    res.append('Fizz')
            elif counter % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(counter))
            
            counter += 1

        return res




a = Solution()
print(a.fizzBuzz(3)) # ["1","2","Fizz"]
print(a.fizzBuzz(5)) # ["1","2","Fizz","4","Buzz"]
print(a.fizzBuzz(15)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]