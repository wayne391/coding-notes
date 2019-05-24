class Solution:
    def isValid(self, s):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        try:
            for c in s:
                if c in '([{':
                    stack.append(c)
                else:
                    c_ = stack.pop()
                    assert brackets[c_] == c
        except (IndexError, AssertionError):
            return False
        return len(stack) == 0
