class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for i in range(len(s)):
            if s[i] == '(':
                brackets.append(')')
            elif s[i] == '[':
                brackets.append(']')
            elif s[i] == '{':
                brackets.append('}')
            else:
                if brackets and s[i] == brackets[-1]:
                    brackets.pop()
                else:
                    return False
        
        if brackets:
            return False
        else:
            return True
