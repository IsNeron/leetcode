class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        
        while num >= 1000:
            num -=1000
            answer += 'M'
        
        if num >= 500:
            if num >= 900:
                num -=900
                answer += 'CM'
            else:
                num -=500
                answer += 'D'
        
        while num >= 100:
            if num >= 400:
                num -= 400
                answer += 'CD'
            else:
                num -=100
                answer += 'C'

        if num >= 50:
            if num >= 90:
                num -=90
                answer += 'XC'
            else:
                num -=50
                answer += 'L'
        
        while num >= 10:
            if num >= 40:
                num -= 40
                answer += 'XL'
            else:
                num -=10
                answer += 'X'

        if num >= 5:
            if num >= 9:
                num -=9
                answer += 'IX'
            else:
                num -=5
                answer += 'V'

        while num > 0:
            if num >= 4:
                num -= 4
                answer += 'IV'
            else:
                num -=1
                answer += 'I'
        
        return answer





a = Solution()
print(a.intToRoman(3749)) #MMMDCCXLIX
print(a.intToRoman(58)) #LVIII
print(a.intToRoman(1994)) #MCMXCIV