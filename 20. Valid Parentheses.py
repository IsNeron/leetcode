class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False

        for element in s:
            if element in ('(', '[', '{'):
                stack.append(element)
                continue
            else:
                if len(stack) == 0:
                    return False
                match stack[-1]:
                    case '(':
                        if element != ')':
                            return False
                    case '[':
                        if element != ']':
                            return False
                    case '{':
                        if element != '}':
                            return False
                stack.pop()
                continue
        
        return len(stack) == 0