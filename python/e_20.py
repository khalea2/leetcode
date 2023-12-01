class Solution:
    def isValid(self, s: str) -> bool:
        '''
        NEET CODE SOLUTION
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        '''
        # same soln, but returns false quicker
        # best case faster

        stack = []
        MAP = { '}':'{', ')':'(', ']':'['}

        for c in s:
            if c not in MAP:
                stack.append(c)
                continue
            if not stack or MAP[c] != stack[-1]:
                # less checks
                return False
            stack.pop()

        return not stack
