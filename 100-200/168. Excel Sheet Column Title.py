class Solution:
    def 


    def convertToTitle(self, columnNumber: int) -> str:
        mapa = {
            1: 'a',
            2: 'b',
            3: 'c',
            4: 'd',
            5: 'e',
            6: 'f',
            7: 'g',
            8: 'h',
            9: 'i',
            10: 'j',
            11: 'k',
            12: 'l',
            13: 'm',
            14: 'n',
            15: 'o',
            16: 'p',
            17: 'q',
            18: 'r',
            19: 's',
            20: 't',
            21: 'u',
            22: 'v',
            23: 'w',
            24: 'x',
            25: 'y',
            26: 'z',
        }
        

        res_len = 1
        res = []

        while columnNumber > 26:
           res_len +=1
           


        print(columnNumber // 26)
        print(columnNumber % 26)
        # if columnNumber < 26:
        #     return mapa[columnNumber]
        





a = Solution()
print(a.convertToTitle(1)) #A
print(a.convertToTitle(28)) #AB
print(a.convertToTitle(701)) #ZY
print(a.convertToTitle(703)) #AAA