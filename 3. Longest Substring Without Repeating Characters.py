def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    stack = []

    for c in s:
        if c in stack:
            if res < len(stack):
                res = len(stack)
            stack = [stack[-1]]
            stack.append(c)
        else:
            stack.append(c)
            res = len(stack)
    return res




print(lengthOfLongestSubstring('abcabcbb')) #3
print(lengthOfLongestSubstring('bbbbb')) #1
print(lengthOfLongestSubstring('pwwkew')) #3
print(lengthOfLongestSubstring(' ')) #0
print(lengthOfLongestSubstring('au')) #2
print(lengthOfLongestSubstring('dvdf')) #3