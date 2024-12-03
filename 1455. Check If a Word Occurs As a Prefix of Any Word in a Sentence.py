class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(' ')
        len_word = len(searchWord)

        for id, word in enumerate(arr):
            if len(word) < len_word:
                continue
            
            if word[:len_word] == searchWord:
                return id+1
            
            continue

        return -1





a = Solution()
print(a.isPrefixOfWord('i love eating burger', 'burg')) #4
print(a.isPrefixOfWord('this problem is an easy problem', 'pro')) #2
print(a.isPrefixOfWord('i am tired', 'you')) #-1