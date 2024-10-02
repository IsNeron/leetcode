romans = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

def intToRoman(num: int) -> str:
    res = []    
    b = int(str(num)[:1])
    if b not in (4, 9):








print(intToRoman(3749)) #MMMDCCXLIX
print(intToRoman(58)) #LVIII
print(intToRoman(1994)) #MCMXCIV

